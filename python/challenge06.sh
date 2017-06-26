#!/bin/bash

cat ../files/challenge06.txt \
	| tr -d '\n' \
	| python b64.py decode \
	| python vigenere.py
