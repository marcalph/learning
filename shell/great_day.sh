#!/bin/bash
if [[ -z $1 ]]
then
  res="a great day"
else
  res="$1"
fi
echo "Today is ${res}"