#!/bin/bash

var=$(echo this | rev | cut -d "." -f1 | rev)
if [[ var -eq "py" ]]; then
	echo "yes"
else
	echo "no"
fi
