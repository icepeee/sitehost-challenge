# SiteHost Challenge

## Introduction

Firstly, thank you for giving me this opportunity. I have included my answers to both Part 1 and Part 2 of the challenge.

## Part 1: API Integration

In Part 1, I successfully retrieved the list of domains and their associated DNS records using the provided API. The code for this is included in the file `part1_script.py`.

## Part 2: Resolving a Customer Issue

In Part 2, I investigated the issue reported by Alice regarding the website `site.recruitment.shq.nz` being inaccessible.

### Findings

Using a DNS tool, I discovered that the domain `site.recruitment.shq.nz` is pointing to a private IP address (`192.168.1.10`), which is not accessible from the internet. This is likely the cause of the connection issue.

### Response to the Client

I have written a response to Alice explaining the issue and providing instructions on how to update the DNS `A` record to point to the correct public IP address (`120.138.30.179`). The response is included in the file `reply.md`.

### Additional Considerations

While I informed Alice on how to update the DNS records herself, there is also the option for us to update the `A` record directly to speed up the process. However, I thought it would be more beneficial for the client to understand what went wrong and how to resolve such issues in the future.

## Files Included

- `part1_script.py`
- `reply.md`


