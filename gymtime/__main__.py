from argparse import ArgumentParser

parser = ArgumentParser(prog="Gym Time", description="Controlling gym time scraping")
parser.add_argument("-f", "--fetch", action="store_true")
args = parser.parse_args()

if args.fetch:
    ...
    # fetch_current_times()
