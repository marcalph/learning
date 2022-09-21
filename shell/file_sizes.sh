#!/bin/bash
for file in ls *
do
  echo $file::$(du -h $file | cut -f1)
done
