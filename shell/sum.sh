#!/bin/bash
if [[ ${#@} -lt 2 ]] || [[ ${#@} -gt 2 ]]
then
  echo "ERROR"
  echo "usage sum.sh <arg1> <arg2"
else
  re="^[0-9]+$"
  if ! [[ $1 =~ $re && $2 =~ $re ]]
  then
    echo "ERROR"
    echo "inputs should be numbners"
  else
    echo $(( $1 + $2))
  fi
fi