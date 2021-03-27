from dotenv import load_dotenv, find_dotenv, set_key
from os import environ

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

# update any ennironment variables


def update_token(name, value):
    environ[name] = value
    set_key(dotenv_file, name, environ[name])
