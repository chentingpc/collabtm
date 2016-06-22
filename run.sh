#!/bin/bash


#./bin/collabtm -dir /citeulike -nusers 5552 -ndocs 16981 -nvocab 11031 -k 50 -lda-init -fixeda
./bin/collabtm -dir citeulike/ -nusers 5552 -ndocs 16981 -nvocab 11031 -k 10 -fixeda -heldout-items-ratio 0
#./bin/collabtm -dir /citeulike -nusers 5555 -ndocs 17981 -nvocab 12031 -k 50 -fixeda


