import yaml

def getYml(args):
    #对从config文件获取信息
    with open('config.yml', 'r', encoding='utf-8') as yml:
        yml = yaml.load(yml, yaml.FullLoader)[args]
        return yml