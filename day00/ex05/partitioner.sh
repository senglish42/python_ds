#!/bin/sh

#узнаю количество вакансий на каждый день, записываю их в одну линию
line=$(cut -d "," -f2 ../ex03/hh_positions.csv  | tail -n +2 | sed 's/^.\(..........\).*/\1/' | uniq -c |\
sed 's/^[[:space:]]*//g' | sed '/"-"/d' | cut -d " " -f1 | sed ':a;N;$!ba;s/\n/,/g')
#парсинг линии
str=$(echo $line | tr "," "\n")
#прохожусь по дням в цикле, закидываю строки в созданные на каждый день файлы
last=2;
for num in $str
do
    name=$(cut -d "," -f2 ../ex03/hh_positions.csv  | tail -n +$last | head -n $num | sed 's/^.\(..........\).*/\1/')
    name=$(echo $name | cut -d " " -f1)
    cat ../ex03/hh_positions.csv | head -n 1 > $name.csv
    cat ../ex03/hh_positions.csv | tail -n +$last | head -n $num >> $name.csv
    last=$((last + num))
done