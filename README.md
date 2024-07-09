# SiteHost Challenge

## Introduction

Firstly, thank you for giving me this opportunity. I have included my answers to both Part 1 and Part 2 of the challenge.

## Part 1: API Integration

In Part 1, I successfully retrieved the list of domains and their associated DNS records using the provided API. The code for this is included in the file `part1_script.py`.

## Part 2: Resolving a Customer Issue

In Part 2, I was actually unable to find the hidden HTML comment. I did go to the IP address `120.138.30.179` > inspect source code. However I did not see a hidden comment. 

However I continued on using a DNS tool, and discovered that the domain `site.recruitment.shq.nz` was pointing to a private IP address (`192.168.1.10`), which looked to be the reason why it was not accessible.

Additional considerations --- While I informed Alice on how to update the DNS records herself, I did think we could just update the `A` record for them directly to speed up the process. However, I thought it would be more beneficial for the client to understand what went wrong and how to resolve such issues in the future. 

## Files Included

- `part1_script.py`
- `reply.md`
