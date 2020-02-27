#!/bin/sh

n=`wc -l ../hightemp.txt | awk '{print $1}'`
split -l $((n/3)) ../hightemp.txt split.txt
