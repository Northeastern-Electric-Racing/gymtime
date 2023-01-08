from argparse import ArgumentParser
from gymtime.scrape.fetch import fetch_all_records

parser = ArgumentParser(prog="Gym Time", description="Controlling gym time scraping")
parser.add_argument("-f", "--fetch", action="store_true")
args = parser.parse_args()

if args.fetch:
    gym_counts = fetch_all_records()
