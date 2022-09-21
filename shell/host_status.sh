#!/bin/bash
ping -c 3 $1 > /dev/null 2>&1
if [ $? -ne 0 ]
then
  echo fucking not
else
  echo maybe
fi