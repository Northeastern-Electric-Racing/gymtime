from dataclasses import dataclass
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from ..util.decode_string import decode_html_string

# URL = "https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7"
URL = "http://13.60.202.202/connect2/index.php?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7"


def fetch_c2c_html() -> str:
    req = requests.get(URL, headers={"User-Agent": "Mozilla"})
    print(req.status_code)
    if req.status_code != 200:
        raise Exception("Unable to fetch")

    return req.text


@dataclass
class GymCount:
    """Gym count containing gym name, time, and count"""

    c2c_name: str
    percent: int
    count: int
    time: datetime


def fetch_all_records() -> "list[GymCount]":
    soup = BeautifulSoup(fetch_c2c_html(), "html.parser")

    charts_div = soup.select_one(".panel-body")
    if charts_div is None:
        raise Exception("Unable to find charts")

    count_divs = charts_div.select(".col-md-3.col-sm-6")

    gym_counts = []
    for count_div in count_divs:
        elements = list(count_div.select_one("center").children)
        # data-percent only goes up to 100, but data-lastcount goes over
        percent_full = int(round(float(elements[1].attrs["data-lastcount"]))) 

        """There has to be a prettier way to find the gym name
        HTML:
        <div style="text-align:center;">Marino Center - Gymnasium<br/><span s...
        We need "Marino Center - Gymnasium"
        """

        c2c_name = decode_html_string(str(elements[3]).split("<br/>")[0].split(">")[1])
        count = int(str(elements[3]).split("Last Count: ")[1].split("<br/>")[0])
        time_str = str(elements[3]).split("Updated: ")[1].split("<")[0]
        time = datetime.strptime(time_str, "%m/%d/%Y %I:%M %p")

        gym_counts.append(
            GymCount(
                c2c_name=c2c_name,
                percent=percent_full,
                count=count,
                time=time,
            )
        )

    return gym_counts
