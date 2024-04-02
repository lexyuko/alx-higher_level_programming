#!/bin/bash
#takes in a url, sends a request to that url, display the suze of the body of the response

curl -sI "$1"  grep 'Content-Length:' cut -d' ' -f2
