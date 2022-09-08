#!/bin/sh

#узнаю количество вакансий на каждый день, записываю их в одну линию
line=$(cut -d "," -f2 ../ex03/hh_positions.csv  | tail -n +2 | sed 's/^.\(..........\).*/\1/' | uniq -c |\
sed 's/^[[:space:]]*//g' | sed '/"-"/d' | cut -d " " -f1 | sed ':a;N;$!ba;s/\n/,/g')
#парсинг линии с количеством вакансий на каждый день
str=$(echo $line | tr "," "\n")
#прохожусь по дням в цикле, чтобы узнать какие файлы нам нужно конкатенировать, записываю названия файлов в одну линию
last=2;
all_csv="";
for num in $str
do
    name=$(cut -d "," -f2 ../ex03/hh_positions.csv  | tail -n +$last | head -n $num | sed 's/^.\(..........\).*/\1/')
    name=$(echo $name | cut -d " " -f1)
    last=$((last + num))
    all_csv="$all_csv $name"
done
#создаю .csv файл, куда буду передовать данные из разделённых файлов
cat ../ex03/hh_positions.csv | head -n 1 > concatenated.csv
#парсинг линии с именами созданных файлов формата .csv
conc=$(echo $all_csv | tr " " "\n")
#прохожу в цикле по созданным файлам, передаю данные из файлов в общий .csv файл
for split in $conc
do
  if [ -f $split.csv ]
    then cat $split.csv | tail -n +2 >> concatenated.csv
  fi
done