import yaml

with open("config/config.yml", "r") as file:
    config = yaml.safe_load(file)
    BASE_URL = config['base_url']
