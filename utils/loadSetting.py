import yaml

def loadSetting():
    # load settings from yaml
    with open("setting.yml", "r") as yml:
        setting = yaml.load(yml)

    return setting