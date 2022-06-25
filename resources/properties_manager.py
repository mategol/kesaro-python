import win32api
import os

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

def generate_version_file(file_version, company_name, product_name, product_version, original_file_name, file_description, legal_copyright, legal_trademarks):
    if file_version != None:
        file_version = ', '.join(file_version.split('.')) if file_version.count('.') > 0 else file_version

    version_file_content = ["VSVersionInfo(\n",
                            "  ffi=FixedFileInfo(\n",
                            "    filevers=(" + file_version + "),\n" if file_version != None else '',
                            "    mask=0x3f,\n",
                            "    flags=0x0,\n",
                            "    OS=0x4,\n",
                            "    fileType=0x1,\n",
                            "    subtype=0x0,\n",
                            "    date=(0, 0)\n",
                            "    ),\n",
                            "  kids=[\n",
                            "    StringFileInfo(\n",
                            "      [\n",
                            "      StringTable(\n",
                            "        u'040904b0',\n",
                            '        [StringStruct(u"CompanyName", u"' + company_name + '"),\n' if company_name != None else '',
                            '        StringStruct(u"ProductName", u"' + product_name + '"),\n' if product_name != None else '',
                            '        StringStruct(u"ProductVersion", u"' + product_version + '"),\n' if product_version != None else '',
                            '        StringStruct(u"OriginalFilename", u"' + original_file_name + '"),\n' if original_file_name != None else '',
                            '        StringStruct(u"FileDescription", u"' + file_description + '"),\n' if file_description != None else '',
                            '        StringStruct(u"LegalCopyright", u"' + legal_copyright + '"),\n' if legal_copyright != None else '',
                            '        StringStruct(u"LegalTrademarks", u"' + legal_trademarks + '"),\n' if legal_trademarks != None else '',
                            "        ])" if [company_name, product_name, product_version, original_file_name, file_description, legal_copyright, legal_trademarks].count(None) != 7 else '',
                            "]),\n",
                            "    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])\n",
                            "  ]\n",
                            ")"]

    with open('temporary_files/version.txt', 'w', encoding='utf-8') as version_file:
        version_file.write(''.join(version_file_content))

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

    generate_version_file(file_version, company_name, product_name, product_version, original_file_name, file_description, legal_copyright, legal_trademarks)