#!/bin/bash
# verifica se um arquivo é do tipo epub. 
# se for, converte para mobi antes de enviar para a Amazon

filename="$1" 
extension="${filename##*.}"

if test "$extension" == "epub" 
then 
  epubamazon.sh "$1"
else
  mandamazon "$1"
fi



