# !/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import os
import time
import sys
import argparse

sys.path.append(os.path.abspath('../../xyz/'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '__list_of_files', action='append', help='Name of the audio file to be processed', nargs='+', required=True)
    print("Iteration running in loop:")
    args = parser.parse_args()
    total_time = time.time()

    def check_directory(file_name):
        directory = os.path.dirname(file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)


    def save(file_name, words, emotions):
        check_directory(file_name)
        csv_file = open(file_name,'a')
        csvWriter = csv.writer(csv_file)
        csvWriter.writerows(zip(words, emotions))


    if

