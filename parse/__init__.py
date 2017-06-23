from bs4 import BeautifulSoup

def parse_xml(file_name,table_name):
    with open(file_name, "r") as markup:
        soup = BeautifulSoup(markup, "xml")
    table = soup.find_all('table', {'name': table_name})
    
    ret = []

    with open(file_name, "r") as markup:
        soup = BeautifulSoup(markup, "xml")
    table = soup.find_all('table', {'name': table_name})
    for row in table:
        column = row.find_all('column')
        ret_dict = {}
        for value in column:
            key = value['name']
            ret_dict.setdefault(key,[]).append(value.text)
        ret.append(ret_dict)
    return ret

