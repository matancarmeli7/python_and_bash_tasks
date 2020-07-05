#!/bin/bash
if [ ! -d "$2" ]
then
    echo "The Path is not exists"
    exit 1
fi

if [ $1 != 'ascending' ] && [ $1 != 'descending' ]
then
    echo "The order must be one of those values :  ascending/descending"
    exit 1
fi
order=$1
path=$2

function show_files_in_ascending(){
    test=`ls $1 | sort -nr`
    echo $test
}

function show_files_in_descending(){
    test=`ls $1 | sort -n`
    echo $test
}

if [ $order == "ascending" ]
then
    output=`show_files_in_ascending $path` 
    echo $output | xargs -n 1
else
    output=`show_files_in_descending $path`
    echo $output | xargs -n 1
fi