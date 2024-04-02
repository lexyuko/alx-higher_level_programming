#!/bin/bash
#send a delete request to the url passed as the fisrt argument and displays the body
curl -sX DELETE "$1"
