#!/bin/sh

curl -k -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text=data%scientist&search_field=name&page=0&per_page=20' | jq '.' > hh.json
