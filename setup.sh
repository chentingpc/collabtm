#!/bin/bash

home=$(pwd)
./configure make --prefix=$home
make install
