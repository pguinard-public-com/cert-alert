# Discover domains with certificates not matching expected domains by searching through Certificate Transparency logs

## What is CT?
Certificate Transparency (CT) is an experimental IETF standard. The goal of it was to allow the public to audit which certificates were created by Certificate Authorities (CA). TLS has a weakness that comes from the large list of CAs that your browser implicitly trusts. If any of those CAs were to maliciously create a new certificate for a domain, your browser would trust it. CT adds benefits to TLS certificate trust: Companies can monitor who is creating certificates for the domains they own. It also allows browsers to verify that the certificate for a given domain is in the public log record.

## What can you find with cert-alert?
cert-alert will query the CT logs for a given domain for nonexpired certificates, and compare ownership to expected known issuing CAs. When there is an unexpected match an exit code 1 is returned.

## Requirements
Python3
`pip3 install -r requirements.txt` 

## Usage

```console
usage: cert_alert.py [-h] -d DOMAIN

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain to query for CT logs, ex: domain.com
```

## Example output

```console
$ python3 cert_alert.py -d public.com
{'issuer_ca_id': 295819, 'issuer_name': "C=US, O=Let's Encrypt, CN=E6", 'common_name': 'email.meet.public.com', 'name_value': 'email.meet.public.com', 'id': 14973457488, 'entry_timestamp': '2024-10-17T14:19:54.063', 'not_before': '2024-10-17T13:21:21', 'not_after': '2025-01-15T13:21:20', 'serial_number': '04848844ca1ce6809f52d2f984fa04060273', 'result_count': 2}
{'issuer_ca_id': 295819, 'issuer_name': "C=US, O=Let's Encrypt, CN=E6", 'common_name': 'email.meet.public.com', 'name_value': 'email.meet.public.com', 'id': 14973445650, 'entry_timestamp': '2024-10-17T14:19:52.07', 'not_before': '2024-10-17T13:21:21', 'not_after': '2025-01-15T13:21:20', 'serial_number': '04848844ca1ce6809f52d2f984fa04060273', 'result_count': 2}
{'issuer_ca_id': 286236, 'issuer_name': 'C=US, O=Google Trust Services, CN=WE1', 'common_name': 'meetcalendar.public.com', 'name_value': 'meetcalendar.public.com', 'id': 14965392799, 'entry_timestamp': '2024-10-17T01:11:55.534', 'not_before': '2024-10-17T00:10:25', 'not_after': '2025-01-15T01:10:20', 'serial_number': '00eb0822dc976388911323c480a9566d84', 'result_count': 2}
{'issuer_ca_id': 286236, 'issuer_name': 'C=US, O=Google Trust Services, CN=WE1', 'common_name': 'meetcalendar.public.com', 'name_value': 'meetcalendar.public.com', 'id': 14965393277, 'entry_timestamp': '2024-10-17T01:10:25.575', 'not_before': '2024-10-17T00:10:25', 'not_after': '2025-01-15T01:10:20', 'serial_number': '00eb0822dc976388911323c480a9566d84', 'result_count': 2}
{'issuer_ca_id': 286242, 'issuer_name': 'C=US, O=Google Trust Services, CN=WR1', 'common_name': 'meetcalendar.public.com', 'name_value': 'meetcalendar.public.com', 'id': 14965384169, 'entry_timestamp': '2024-10-17T01:10:15.482', 'not_before': '2024-10-17T00:10:15', 'not_after': '2025-01-15T01:08:57', 'serial_number': '009495a8f87358114713d7134afbcdfe01', 'result_count': 2}
```
