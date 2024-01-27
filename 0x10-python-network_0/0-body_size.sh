#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
