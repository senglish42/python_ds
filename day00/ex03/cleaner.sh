#!/bin/bash

cut -d "," -f1,2 ../ex02/hh_sorted.csv > .tmp1.csv;
cut -d '"' -f6 ../ex02/hh_sorted.csv |
sed -e '2,$y/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/' |\
sed '2,$s/^/#/' |
sed '/SENIOR/s/^/Senior\//' |
sed '/MIDDLE/s/^/Middle\//' |
sed '/JUNIOR/s/^/Junior\//' |
sed '/^#/c -' |
sed -r 's/(Senior\/#).+/\1/' |
sed -r 's/(Middle\/#).+/\1/' |
sed -r 's/(Junior\/#).+/\1/' |
sed 's/\/#.*//g' |
sed -r 's/(^|$)/"/g'  > .tmp2.csv ;
cut -d"," -f 4- ../ex02/hh_sorted.csv |
sed -e '2,$s/ .*",//g'> .tmp3.csv;
paste -d "," .tmp1.csv .tmp2.csv .tmp3.csv > hh_positions.csv;
rm -r .tmp1.csv .tmp2.csv .tmp3.csv