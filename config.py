from dotenv import load_dotenv
from utils import json_pars
import json
import os

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    TOKEN = os.environ.get('TOKEN')
    GROUP_ID = os.environ.get('GROUP_ID')
    with open("info.json", encoding="UTF-8") as f:
        INFO = dict(json.load(f))
        ADDITIONAL_BUTTONS = json_pars(INFO) 
