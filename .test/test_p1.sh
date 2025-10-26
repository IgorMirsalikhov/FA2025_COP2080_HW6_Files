#!/bin/bash

cp .test/test_p1.txt p1/
printf "p1/test_p1.txt\nby\ny\nnot\n" | python p1/p1.py

if [ -z "$(diff -uiwB .test/test_p1_after_replace.txt p1/test_p1.txt)" ]; then
    echo "Files are the same"
else
    echo "Files differ:"
    diff -uiwB .test/test_p1_after_replace.txt p1/test_p1.txt
fi