#!/bin/bash
# 1. Install System Dependencies (Required for libsass, lxml, and psycopg)
# dnf automatically handles x86 vs Graviton (aarch64)
dnf install -y \
    gcc \
    gcc-c++ \
    python3-devel \
    postgresql15-devel \
    libxml2-devel \
    libxslt-devel \
    libjpeg-turbo-devel \
    libpng-devel \
    zlib-devel

# 2. Activate the Virtual Environment
VENV=$(find /var/app/venv/ -maxdepth 1 -type d | tail -n 1)
source "$VENV/bin/activate"

# 3. Upgrade Pip/Setuptools to handle Python 3.12/3.13 changes
pip install --upgrade pip setuptools wheel

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