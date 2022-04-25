#!/bin/bash
echo -n "Please insert your input: "
while read line
do
  if [[ -z $line ]]
  then
    break
  fi
  echo -n $line | wc -c
  echo -n "Please insert your input: "
done