#!/bin/bash

yum -y install libmemcached-devel

lscpu | grep Architecture | grep x86

if [ $? -eq 0 ]; then
  echo "Has x86 processor"
  yum -y install zlib-devel.x86_64
else
  echo "Has Graviton processor"
  yum -y install zlib-devel
  yum -y install gcc-c++
fi
