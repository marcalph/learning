#!/bin/bash
arg_value=${1:-default}
if [[ $arg_value == "pizza" ]]
then
  echo "with pineapple?"
else
  echo "I want pizza!"
fi