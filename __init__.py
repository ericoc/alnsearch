#!/usr/bin/env python3
import requests
import logging
from argparse import ArgumentParser

# Logging.
LOG_LEVEL = logging.INFO
logging.basicConfig(
    datefmt="%Y-%m-%d %H:%M:%S %Z (%z)",
    format="%(asctime)s [%(levelname)s] (%(process)d): %(message)s",
    handlers=[logging.StreamHandler()],
    level=LOG_LEVEL
)
logger = logging.getLogger(__name__)

# Parse ALN/CFDA argument.
parser = ArgumentParser(
    "HTTPS JSON REST API search client for Assistance Listing Numbers (ALNs)"
)
parser.add_argument("cfda", help="ALN, formerly CFDA, to search.")
args = parser.parse_args()

# Log the ALN/CFDA number to search, and initialize an empty list of agencies.
logger.debug(f'Searching ALN (CFDA) "{args.cfda}" ...')
agencies = []

# Make API POST request to gather information about the ALN/CFDA number.
try:
    resp = requests.post(
        url="https://api.grants.gov/v1/api/search2",
        headers={
            "Accept": "application/json",
            "User-Agent": "ALN (CFDA) REST API JSON search / ericoc.com v0.1"
        },
        json={"cfda": args.cfda},
    )
    logger.debug(msg=f"API response code: {resp.status_code}")
    logger.debug(msg=vars(resp))
    agencies = resp.json()["data"]["agencies"]

except Exception as req_exc:
    logger.exception(msg="API request failed.", exc_info=req_exc)

# Ensure that at least once agency was found, listing total count.
agency_count = len(agencies) or 0
assert agency_count > 0, f'No agencies found for ALN/CFDA: "{args.cfda}".'
logger.info(msg=f'{agency_count} agencies found for ALN/CFDA "{args.cfda}".')

# Gather the label of each agency that was found.
agency_labels = []
for agency in agencies:
    agency_labels.append(agency["label"])

# Numbered list of each agency label.
for (count, agency_label) in enumerate(iterable=agency_labels, start=1):
    logger.info(f"\t{count}. {agency_label}")
