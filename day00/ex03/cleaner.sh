#!/bin/bash

cut -d"," -f1,2 ../ex02/hh_sorted.csv > hh.csv;
cut -d"," -f3 < ../ex02/hh_sorted.csv |
sed -e '2,$y/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/' |\
sed '2,$s/^/#/' |
sed '/SENIOR/s/^/Senior\//' |
sed '/MIDDLE/s/^/Middle\//' |
sed '/JUNIOR/s/^/Junior\//' |
sed '/^#/c "-"' |
sed -r 's/(Senior\/#).+/\1/' |
sed -r 's/(Middle\/#).+/\1/' |
sed -r 's/(Junior\/#).+/\1/' |
sed 's/\/#.*//g' |
awk -F"," '{$3; print}' input.csv > output.csv