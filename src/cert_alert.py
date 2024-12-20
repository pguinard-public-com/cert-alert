#!/usr/bin/env python3

import argparse
import sys

import requests


def main(domain):
    response = collect_response(domain)
    alert_domains = process_responses(response)
    for record in (alert_domains):
        print(record)
    if len(alert_domains) > 0:
        sys.exit(1)


def collect_response(domain):
    url = 'https://crt.sh/?Identity=' + domain + '&output=json&exclude=expired'
    response = requests.get(url, timeout=300)
    domains = response.json()
    return domains


def process_responses(response):
    non_compliant_domains = []
    if len(response) == 0:
        return ["No domains found for the given domain."]
    for r in response:
        if not amazon_certificate(r) and not vercel_certificate(r):
            non_compliant_domains.append(r)
    return non_compliant_domains


def amazon_certificate(response_record):
    return response_record['issuer_name'].startswith("C=US, O=Amazon, CN=Amazon")


def vercel_certificate(response_record):
    return response_record['issuer_name'].startswith("C=US, O=Let's Encrypt") and response_record['name_value'].endswith(".webapp.public.com")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", type=str, required=True,
                        help="domain to query for CT logs, e.g.: domain.com")
    args = parser.parse_args()
    main(args.domain)
