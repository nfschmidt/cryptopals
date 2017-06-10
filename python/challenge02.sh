#!/bin/bash

python xor.py fixor \
	<(python hexa.py decode <<< 1c0111001f010100061a024b53535009181c) \
	<(python hexa.py decode <<< 686974207468652062756c6c277320657965) \
	| python hexa.py encode

