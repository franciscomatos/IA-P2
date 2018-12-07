#!/bin/bash
trap "exit" INT
for number in {1..1000}
do
    echo 'TESTE '$number >> testsResults.txt
    python3 mainRL.py >> testsResults.txt
done
