#!/bin/bash
(( $1 % 2 )) || res="one factor"
(( $1 % 3 )) || res+="...actually two!"

echo ${res:-$1}