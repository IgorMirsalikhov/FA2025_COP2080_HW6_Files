#!/bin/bash

printf "p2/dir_a\np2/dir_b\n" | python p2/p2.py

if [ -z "$(diff -uiwB .test/diff_report.txt diff_report.txt)" ]; then
    echo "Files are the same"
else
    echo "Files differ:"
    diff -uiwB .test/diff_report.txt diff_report.txt
fi