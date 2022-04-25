#!/bin/bash
case ${#@} in
    0) echo "Usage: ./<program name> <argument>";;
    1) echo "Got it: $1";;
    *) echo "hey hey... to many!";;
esac