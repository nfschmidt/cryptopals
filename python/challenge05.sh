#!/bin/bash

python xor.py rexor \
	<(echo -n ICE) \
	<(echo -n \
"Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal") \
	| python hexa.py encode

