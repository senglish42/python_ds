#!/bin/bash

(head -n 1 ../ex01/hh.csv; tail -n +2 ../ex01/hh.csv | sort -t',' -k2 -k1) > hh_sorted.csv
chmod 7777 hh_sorted.csv