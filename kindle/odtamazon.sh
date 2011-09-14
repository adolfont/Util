#!/bin/bash

filename="$1" 
filename=${filename%\.*}

echo "ebook-convert $filename.odt $filename.epub"
ebook-convert $filename.odt $filename.epub
echo "ebook-convert $filename.epub $filename.mobi"
ebook-convert $filename.epub $filename.mobi

mandamazon $filename.mobi
