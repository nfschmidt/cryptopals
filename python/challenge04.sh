#!/bin/bash

cat ../files/challenge04.txt | while read LINE
do
	echo -n "$LINE" \
	| python hexa.py decode \
	| python xor.py decrypt single text
done
