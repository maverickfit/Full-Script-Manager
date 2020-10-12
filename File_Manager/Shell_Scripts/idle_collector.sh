#!/bin/bash
# Script that runs adb top on tablet and returns the avg % idle

I_FILE_NAME="Results/idle.txt" #Set File Name
RESULTS_FILE="Results/idle_results.txt" 

let SECONDS_IN_MINUTE=55 #set to 55 to account for 4.5s drift per minute
let DELAY=1 #Variable to set the delay between top log pulls in seconds
let LINES=5 #Variable to set the number of top displays (lower equals less impact)
let TIME_TOTAL=$SECONDS_IN_MINUTE*$1

adb shell top -d $DELAY -m $LINES -n $TIME_TOTAL | grep Idle | tr -s " " "\n" | grep -A1 Idle | tr -d '%Idle-' | grep -v -e '^$' >> $I_FILE_NAME #Collect Idle Data from 'top'

let I_NUM_LINES=$(wc -l $I_FILE_NAME | awk '{print $1}') #Get number of lines in output

let I_counter=1 #Used to iterate to number of collection data points
let I_SUM=0 #Used to hold the sum of all collected data points
until [ $I_counter -gt $I_NUM_LINES ] #Add all data points
do
    let I_VAL=$(cat $I_FILE_NAME | head -n$I_counter | tail -n1)
    let I_SUM+=$I_VAL
    ((I_counter++))
done

I_FINAL_VAL=$(echo "scale=2; $I_SUM / $I_NUM_LINES" | bc -l)

echo $I_SUM >> $RESULTS_FILE
echo $I_NUM_LINES >> $RESULTS_FILE
echo $I_FINAL_VAL >> $RESULTS_FILE
