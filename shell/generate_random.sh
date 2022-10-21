#!/bin/bash

set -o errexit #-e
set -o xtrace #-x
function generate_random_image {
    mx=320;my=256;head -c "$((3*mx*my))" /dev/urandom | convert -depth 8 -size "${mx}x${my}" RGB:- random.png
}

function generate_random_file {
    head -c 1048576 </dev/urandom > random.file
}


generate_random_image
generate_random_file
