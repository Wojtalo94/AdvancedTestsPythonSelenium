import yaml

with open("config/config.yml", "r") as file:
    config = yaml.safe_load(file)
    BASE_URL = config['base_url']

    # test settings
    MAX_WAIT = config["max_wait"]
    HEADLESS = config["headless"]
    FULLSCREEN = config["fullscreen"]
