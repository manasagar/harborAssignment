#!/bin/bash
jq '[.[] | select(.age > 25)]' /app/input.txt > /app/output.json



