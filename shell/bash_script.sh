#!/bin/bash

set -o errexit #-e
set -o xtrace #-x
set -o nounset
# function hello {
#     echo "Hello World!"

# }

# a=(1 2 3 4)
# echo ${a[2]}
# function myfunc {
#     echo $1
#     echo $2
# }
# myfunc "Hello World"
# myfunc Hello World


# type myfunc



# no > output.txt 2>&1
# no 2>&1 > output.txt
A=1
[ $A = 1 ]
echo $?
[ $A == 1 ]
echo $?
[ $A = 2 ]
echo $?

[ 10 -lt 2 ]      # The -lt operator works in single brackets
echo $?
[ '10' -lt '2' ]
echo $?           # Still treats arguments as integers when quoted
[ 1 -lt 2 ]
echo $?
[ 10 -gt 1 ]
echo $?
[ 1 -eq-e 1 ]
echo $?
[ 1 -ne 1 ]
echo $?