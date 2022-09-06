#!/bin/bash

(head -n 1 ../ex01/hh.csv; tail -n +2 ../ex01/hh.csv | sort -t',' -k2,2 -k1,1) > hh_sorted.csv