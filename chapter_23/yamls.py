import yaml


with open("mcintyre.yaml", "rt") as file:
    text = file.read()

data = yaml.load(text, Loader=yaml.FullLoader)
print(data)
