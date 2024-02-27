#!/usr/bin/env bash

count=0
filetypes=('python', 'c', 'ruby', 'bash')
while (( count < 1 )); do
	if [[ 'python' = @('python'|'c'|'ruby'|'bash') ]]; then
		printf "Yes, 'python' is recognized\n"
	fi
	count+=1
done
