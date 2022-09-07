#!/bin/bash

echo '"name","count"' > hh_uniq_positions.csv;
cut -d "," -f3 ../ex03/hh_positions.csv | tail -n +2 | sort | uniq -c | sed 's/^[[:space:]]*//g' | sed '/"-"/d' |\
sed -r 's/^(\S*)(\s*)(\S*)$/\3\2\1/g' | sed 's/ /,/' >> hh_uniq_positions.csv