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
usage: HTTPS JSON REST API search client for Assistance Listing Numbers (ALNs). [-h] aln

positional arguments:
aln         ALN (aka. CFDA #)

options:
-h, --help  show this help message and exit
```

### Multiple Agencies
#### 81.049

##### Python
```py
$ python3 __init__.py 81.049
2025-05-03 23:23:41 EDT (-0400) [INFO] (34141): 2 agencies found. (81.049)
2025-05-03 23:23:41 EDT (-0400) [INFO] (34141):         1) Department of Energy - Office of Science
2025-05-03 23:23:41 EDT (-0400) [INFO] (34141):         2) U.S. National Science Foundation
```

##### cURL
```shell
$ curl -s 'https://api.grants.gov/v1/api/search2' -H 'Content-Type: application/json' -d '{"cfda": "81.049"}' | jq '.data.agencies.[].label'
"Department of Energy - Office of Science"
"U.S. National Science Foundation"
```


### One Agency
#### 47.049

##### Python
```py
$ python3 __init__.py 47.049
2025-05-03 23:23:57 EDT (-0400) [INFO] (34181): 1 agencies found. (47.049)
2025-05-03 23:23:57 EDT (-0400) [INFO] (34181):         1) U.S. National Science Foundation
```

##### cURL
```shell
$ curl -s 'https://api.grants.gov/v1/api/search2' -H 'Content-Type: application/json' -d '{"cfda": "47.049"}' | jq '.data.agencies.[].label'
"U.S. National Science Foundation"
```

---

### Failures

#### 41.049
##### No Agencies
```py
$ python3 __init__.py 41.049
Traceback (most recent call last):
File "/Users/eric/code/alnsearch/__init__.py", line 49, in <module>
assert agency_count > 0, (
    ^^^^^^^^^^^^^^^^
    AssertionError: No agencies found for Assistance Listing Number! (41.049)
```

#### 41.0499
##### Invalid ALN Format
```py
$ python3 __init__.py 41.0499
Traceback (most recent call last):
File "/Users/eric/code/alnsearch/__init__.py", line 25, in <module>
assert fullmatch(pattern=r"^[0-9]{2}\.[0-9]{3}$", string=args.aln), (
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Invalid Assistance Listing Number (ALN, aka. CFDA #) format! (41.0499)
```
