#!/bin/bash

# 1. Base Build Tools (Essential for compiling libsass, lxml, and psycopg)
yum -y install gcc gcc-c++ python3-devel

# 2. Database & XML Headers (Required for psycopg2 and lxml)
yum -y install postgresql-devel libpq-devel libxml2-devel libxslt-devel

# 3. Image & SASS Headers (Required for Pillow and libsass)
yum -y install libjpeg-turbo-devel libpng-devel libmemcached-devel

# 4. Architecture-specific tweaks
if lscpu | grep -q "aarch64"; then
  echo "Graviton detected"
  yum -y install zlib-devel
else
  echo "x86 detected"
  yum -y install zlib-devel.x86_64
fi

# For an Ubuntu Development machine, you need:
#
#    # Update package lists
#    sudo apt-get update
#
#    # 1. Base Build Tools (Essential for compiling libsass, lxml, etc.)
#    sudo apt-get install -y build-essential python3-dev gcc g++
#
#    # 2. Database & XML Headers (Required for psycopg and lxml)
#    sudo apt-get install -y libpq-dev libxml2-dev libxslt-dev
#
#    # 3. Image & SASS Headers (Required for Pillow and libsass)
#    sudo apt-get install -y libjpeg-dev libpng-dev libfreetype6-dev libwebp-dev zlib1g-dev
#
#    # 4. Memcached headers
#    sudo apt-get install -y libmemcached-dev