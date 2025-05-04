# HTTPS ALN/CFDA REST API JSON Search Client

## Background

This is a quick script to query Assistance Listing Numbers (ALN), formerly
known as the Catalog of Federal Domestic Assistance (CFDA) numbers, using the
following HTTPS JSON REST API client.

https://grants.gov/api

Assistance Listing Numbers (ALN), formerly known as the
Catalog of Federal Domestic Assistance (CFDA) Number, are assigned to each
federal assistance program (such as grants).
They are used for government reporting, auditing, and tracking purposes.

## Examples

Assistance Listing Numbers (ALNs, _aka_ CFDAs) are five (`5`) digit numbers,
which are separated by a period (`.`), such as the following:

- `81.049`
- `47.049`

### Help
```py
$ python3 __init__.py -h
usage: HTTPS JSON REST API search client for Assistance Listing Numbers (ALNs) [-h] cfda

positional arguments:
cfda        ALN, formerly CFDA, to search.

options:
-h, --help  show this help message and exit
```

### Multiple Agencies
#### 81.049
```py
$ python3 __init__.py 81.049
2025-05-03 22:24:00 EDT (-0400) [INFO] (30788): 2 agencies found for ALN/CFDA "81.049".
2025-05-03 22:24:00 EDT (-0400) [INFO] (30788):         1. Department of Energy - Office of Science
2025-05-03 22:24:00 EDT (-0400) [INFO] (30788):         2. U.S. National Science Foundation
```

### One Agency
#### 47.049
```py
$ python3 __init__.py 47.049
2025-05-03 22:24:09 EDT (-0400) [INFO] (30804): 1 agencies found for ALN/CFDA "47.049".
2025-05-03 22:24:09 EDT (-0400) [INFO] (30804):         1. U.S. National Science Foundation
```

### Failure
#### 41.049
```py
$ python3 __init__.py 41.049
Traceback (most recent call last):
File "/Users/eric/code/cfda/__init__.py", line 52, in <module>
assert agency_count > 0, f'No agencies found for ALN/CFDA: "{args.cfda}".'
^^^^^^^^^^^^^^^^
AssertionError: No agencies found for ALN/CFDA: "41.049".
```

### cURL

```shell
$ curl -s 'https://api.grants.gov/v1/api/search2' -H 'Content-Type: application/json' -d '{"cfda": "47.049"}' | jq '.data.agencies.[].label'
"U.S. National Science Foundation"
```
```shell
$ curl -s 'https://api.grants.gov/v1/api/search2' -H 'Content-Type: application/json' -d '{"cfda": "81.049"}' | jq '.data.agencies.[].label'
"Department of Energy - Office of Science"
"U.S. National Science Foundation"
```
