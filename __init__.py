#!/usr/bin/env python3
import logging
from argparse import ArgumentParser
from re import fullmatch
from requests import post

# Logging.
LOG_LEVEL = logging.INFO
logging.basicConfig(
    datefmt="%Y-%m-%d %H:%M:%S %Z (%z)",
    format="%(asctime)s [%(levelname)s] (%(process)d): %(message)s",
    handlers=[logging.StreamHandler()],
    level=LOG_LEVEL
)
logger = logging.getLogger(__name__)

# Parse ALN (aka. CFDA number) argument.
parser = ArgumentParser(
    "HTTPS JSON REST API search client for Assistance Listing Numbers (ALNs)."
)
parser.add_argument("aln", help="ALN (aka. CFDA #)")
args = parser.parse_args()

# Validate format of ALN (aka. CFDA number) that was submitted.
assert fullmatch(pattern=r"^[0-9]{2}\.[0-9]{3}$", string=args.aln), (
    f"Invalid Assistance Listing Number (ALN, aka. CFDA #) format! ({args.aln})"
)

# Initialize empty list of agencies.
agencies = []

# HTTPS API POST request to gather ALN (aka. CFDA #) information.
try:
    resp = post(
        url="https://api.grants.gov/v1/api/search2",
        headers={
            "Accept": "application/json",
            "User-Agent": "ALN/CFDA REST API JSON Search / ericoc.com v0.1"
        },
        json={"cfda": args.aln},
    )
    agencies = resp.json()["data"]["agencies"]

except Exception as req_exc:
    logger.exception(msg="API request failed.", exc_info=req_exc)

# Ensure at least once agency was found, logging total count.
agency_count = len(agencies) or 0
assert agency_count > 0, (
    f"No agencies found for Assistance Listing Number! ({args.aln})"
)
logger.info(
    f"{agency_count} agencies found. ({args.aln})"
)

# Gather the label of each agency found.
agency_labels = []
for agency in agencies:
    agency_labels.append(agency["label"])

# Number and log the agency labels.
for (count, agency_label) in enumerate(iterable=agency_labels, start=1):
    logger.info(f"\t{count}) {agency_label}")
