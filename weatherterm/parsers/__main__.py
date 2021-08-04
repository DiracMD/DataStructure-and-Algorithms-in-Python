import argparse
import sys
from argparse import ArgumentParser
from typing_extensions import Required
from weatherterm.core import parser_loader
from weatherterm.core import ForecastType
from weatherterm.core import Unit

def _validate_forecast_args(args):
    if args.forecast_option is None:
        err_msg=("One of these arguments must be used: "
                 "-td/--today,-5d/--fivedays,-10d/-tendays,w/--weekend")
        print(f'{argparser.prog}: error:{err_msg}',
        file=sys.stderr)
        sys.exit

parsers=parser_loader.load("./weatherterm/parsers")

argparser=ArgumentParser(
    prog="weatherterm",
    description="Wwather info from weather.com on your terminal")

required=argparser.add_argument_group("required arguments")
required.add_argument("-p","--parser",
                      choices=parsers.keys(),
                      required=True,
                      dest='parser',
                      help=('Specify which parser is going to be used to scrape weather information'))

unit_values=[name.title() for name,value in Unit.__members__.items()]
Unit.__members__.items()
argparser.add_argument("-u","--unit")

##to be continued