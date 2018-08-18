import yaml

def write_yaml():
    data = {'Search_Data': {
        'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
        'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

    with open("../Data/test_data_yaml.yml","w",encoding="utf-8") as f:
        yaml.dump(data,f,encoding="utf-8",allow_unicode=True)

if __name__ == '__main__':
    write_yaml()