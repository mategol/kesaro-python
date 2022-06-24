import win32api

def get_file_properties(source):
    property_names = ('Comments', 'ProductName', 'CompanyName', 'LegalCopyright', 'OriginalFilename', 'ProductVersion', 'FileDescription', 'LegalTrademarks', 'FileVersion')
    properties = {'FileVersion': '', 'StringFileInfo': {'CompanyName': '', 'ProductName': '', 'ProductVersion': '', 'OriginalFilename': '', 'FileDescription': '', 'LegalCopyright': '', 'LegalTrademarks': ''}}

    try:
        fixed_info = win32api.GetFileVersionInfo(source, '\\')
        properties['FileVersion'] = "%d.%d.%d.%d" % (fixed_info['FileVersionMS'] / 65536, fixed_info['FileVersionMS'] % 65536, fixed_info['FileVersionLS'] / 65536, fixed_info['FileVersionLS'] % 65536)
    except:
        pass

    try:
        lang, codepage = win32api.GetFileVersionInfo(source, '\\VarFileInfo\\Translation')[0]
        str_info = {}
        for propName in property_names:
            str_info_path = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
            str_info[propName] = win32api.GetFileVersionInfo(source, str_info_path)
        properties['StringFileInfo'] = str_info
    except:
        pass

    return properties

def clone_file_properties(source):
    source_properties = get_file_properties(source)

    file_version = source_properties['FileVersion']
    company_name = source_properties['StringFileInfo']['CompanyName']
    product_name = source_properties['StringFileInfo']['ProductName']
    product_version = source_properties['StringFileInfo']['ProductVersion']
    original_file_name = source_properties['StringFileInfo']['OriginalFilename']
    file_description = source_properties['StringFileInfo']['FileDescription']
    legal_copyright = source_properties['StringFileInfo']['LegalCopyright']
    legal_trademarks = source_properties['StringFileInfo']['LegalTrademarks']