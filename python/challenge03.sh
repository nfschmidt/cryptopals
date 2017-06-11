#!/bin/bash

echo -n '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736' \
	| python hexa.py decode \
	| python xor.py decrypt single space

