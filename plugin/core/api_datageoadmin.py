import requests

BASEURL = 'https://data.geo.admin.ch/api/stac/v0.9/collections'

OPTION_MAPPER = {
    'coordsys': 'proj:epsg',
    'resolution': 'eo:gsd',
    'format': 'geoadmin:variant',
}
API_OPTION_MAPPER =  {y:x for x,y in OPTION_MAPPER.items()}


def getDatasetList():
    """Get a list of all available datasets and read out with options the
    dataset supports"""
    datasetList = {}
    collection = call(BASEURL)
    
    if collection and isinstance(collection, dict) and 'collections' in collection:
        for ds in collection['collections']:
            dataset = {
                'id': ds['id'],
                'bbox': ds['extent']['spatial']['bbox'][0],
                'links': ds['links'],
                'options': {}
            }
            options = {}
            for sumName, sumItem in ds['summaries'].items():
                options[API_OPTION_MAPPER[sumName]] = sumItem
                    
            # Get available timestamps
            if 'temporal' in ds['extent']:
                options['timestamp'] = ds['extent']['temporal']['interval'][0]
                options['timestamp'].reverse()

            dataset['options'] = options
            datasetList[dataset['id']] = dataset
        
    return datasetList

def getFileList(dataset, bbox, timestamp, options):
    """Request a list of available files that are within a bounding box and
    have a specified timestamp"""
    params = {
        'bbox': ','.join([str(ext) for ext in bbox]),
        'datetime': timestamp
    }
    url = ''
    for link in dataset['links']:
        if link['rel'] == 'items':
            url = link['href']
            break
    
    items = call(url, params=params)
    
    # Filter list
    fileList, metadata = filterFileListByOptions(items, options)
    return fileList, metadata

def filterFileListByOptions(items, options):
    """Filter a list of file items and only return the ones that match the
    currently selected options"""
    fileList = []
    metadata = {
        'count': 0,
        'size': 0
    }
    if items and isinstance(items, dict) and 'features' in items:
        for item in items['features']:
            # Filter assets so that we only get the one file that matches the
            #  defined options
            file = {}
            for assetId in item['assets']:
                asset = item['assets'][assetId]
                
                # Filter out all files that match the specified options
                optionsMatch = []
                for optionName, optionValue in options.items():
                    optionApiName = OPTION_MAPPER[optionName]
                    
                    optionsMatch.append(optionApiName in asset.keys() and
                                        optionValue == asset[optionApiName])
                
                if sum(optionsMatch) == len(optionsMatch):
                    file['id'] = assetId
                    file['type'] = asset['type']
                    file['href'] = asset['href']
                    fileList.append(file)
                    
                    # Get Metadata if this file
                    meta = getFileMetadata(file['href'])
                    if meta:
                        metadata['count'] += 1
                        metadata['size'] += int(meta.headers['Content-Length'])
    
    return fileList, metadata

def downloadFiles():
    pass

def call(url, params=None):
    """Fire GET call with URL parameters"""
    if params is None:
        params = {}
    params = {
        **params,
        'format': 'json'
    }
    try:
        response = requests.get(url, params=params)
        return response.json()
    
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print('timeout')
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print('too many redirects')
    except requests.exceptions.HTTPError as e:
        raise SystemExit(e)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)


def getFileMetadata(url):
    """Request header files for a certain url"""
    try:
        return requests.head(url)
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print('timeout')
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print('too many redirects')
    except requests.exceptions.HTTPError as e:
        print(f'Somethings fishy with the API: {e}')
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(f'Everything is fucked: {e}')