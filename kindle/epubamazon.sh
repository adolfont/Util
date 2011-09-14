#!/bin/bash

filename="$1" 
filename=${filename%\.*}

echo "ebook-convert $filename.epub $filename.mobi"
ebook-convert $filename.epub $filename.mobi

mandamazon $filename.mobi
