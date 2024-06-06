#!/bin/bash
# run this script locally in the 'quarterly report' folder
# Indicate the date and time for last stat generation

current_time=$(date +"%Y-%m-%d %H:%M:%S.%3N")
echo "#Book stats for chapters and subchapters, \
generated on: $current_time" > book-stats.md

# add table header
echo "guide name; number of chapters; number of subchapters"  >> book-stats.md
echo "guide name; number of chapters; number of subchapters"

path="../../book/website/"
# Sum up chapters and subchapters
total_chapters=0
total_subchapters=0

# list of guides
guide_list=(reproducible-research project-design \
communication collaboration ethical-research \
community-handbook)

# loop over guide list
for guide in "${guide_list[@]}";do
    # count chapters in each guide
    chapters=$(find "${path}${guide}" -maxdepth 1 -type f | cut -d/ -f2 | sort | wc -l | awk '{print $1 - 1}')
    # count subchapters in each guide
    subchapters=$(find "${path}${guide}" -type f | cut -d/ -f2 | sort | wc -l| awk '{print $1 - 1}')
    
    echo "${guide}; $chapters; $subchapters"
    echo "${guide}; $chapters; $subchapters" >> book-stats.csv

    total_chapters=$((total_chapters + $chapters))
    total_subchapters=$((total_subchapters + $subchapters))
done

# Sum all chapters and subchapters from all guides
echo "\nall guides; $total_chapters; $total_subchapters"
echo "all guides; $total_chapters; $total_subchapters" >>  book-stats.csv
