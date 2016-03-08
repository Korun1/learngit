#!/bin/bash

pushd `dirname $0` > /dev/null
CUR_DIR=`pwd`
popd > /dev/null
date_now=`date +%Y-%m-%d`
echo ${date_now}
date=`date +%Y-%m-%d -d "-1 day"`
echo ${date}

a=`date -d"$date" +%w`
echo $a
if [ $a -eq 0  ];then
    echo "yes"
fi
