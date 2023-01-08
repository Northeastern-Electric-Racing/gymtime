from bs4 import BeautifulSoup
import requests

URL = "https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7"

def fetch_c2c_html()->str:
    req = requests.get(URL)
    if req.status_code!=200:
        raise Exception("Unable to fetch")
    
    return req.text

# def fetch_all_records():