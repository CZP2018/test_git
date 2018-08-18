import yaml
import yaml

with open("../Data/test_data_yml.yml", 'r',encoding="utf-8") as f:
    data = yaml.load(f)
    #print(type(data))  # 打印data类型
    print(data)  # 打印data返回值
