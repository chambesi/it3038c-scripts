#!/bin/bash
# This scrript downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
PENDING=$(echo $DATA | jq '.[0].pending')
NEGATIVE=$(echo $DATA | jq '.[0].pending')
STATES=$(echo $DATA | jq '.[0].states')
TODAY=$(date)

echo "On $TODAY, there were $PENDING pending COVID tests, $NEGATIVE negative results, and $POSITIVE positive COVID cases in $STATES states."
