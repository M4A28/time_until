# time_until (Date Difference Calculator)

## Abstract

This repository contains a Python script that calculates the temporal difference between two specific dates. The output is presented in various units of time, including years, months, days, hours, minutes, and seconds. This tool can be utilized in various academic fields where precise time calculation between two dates is required.

### The script requires the following Python libraries:
- argparse
- termcolor

You can install these with pip:
```bash
pip install termcolor argparse 
```
## Methodology

The script employs Python's built-in `datetime` module to convert the input dates into datetime objects. It then calculates the difference between these two dates. The resulting `timedelta` object is used to calculate the difference in various units of time.

## Usage

1. Clone this repository.
2. Execute the script with the following command:

```bash
python date_difference.py -start YYYY-MM-DD -end YYYY-MM-DD
