#!/bin/bash
# This script downloads covid data and displays it

#Initialize color settings
red="\e[31m"
lr="\e[91m"
grn="\e[32m"
ylw="\e[33m"
bol="\e[1m"
nor="\e[0m"
itl="\e[3m"
gry="\e[90m"
ec="\e[0m"

#pulls covid data via curl and creates our variables
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCurrently')
DEATH=$(echo $DATA | jq '.[0].death')
LASTUP=$(echo $DATA | jq '.[0].lastModified')
TODAY=$(date)

echo "As of  $TODAY in the United States, there have been: "
echo -e "${bol}$POSITIVE${nor} ${lr}positive${ec} COVID cases."
echo -e "${bol}$NEGATIVE${nor} ${grn}negative${ec} COVID cases."
echo -e "${bol}$HOSPITAL${nor} ${ylw}hospitalized${ec} COVID cases."
echo -e "${bol}$DEATH${nor} ${red}deaths${ec} related to COVID."
echo -e "${itl}${gry}NOTE: this data was last updated on $LASTUP${ec}"
