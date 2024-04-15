#!/bin/bash

# run this script locally in the '    project_management/quarterly_reports' folder

## Indicate the date and time for the last stat generation
current_time=$(date +"%Y-%m-%d %H:%M:%S.%3N")
echo "Book stats for chapters and subchapters, \
generated on: $current_time" > book-stats.md

path="../../book/website/"
# list of guides
guide_list=(reproducible-research project-design \
communication collaboration ethical-research \
community-handbook)

# Sum up chapters and subchapters
total_chapters=0
total_subchapters=0

# loop over guide list
for guide in "${guide_list[@]}";do
    echo ${guide}
    
    # count chapters in each guide
    echo "\nGuide: $guide"  >> book-stats.md
    echo "Number of chapters"
    echo "Number of chapters"  >> book-stats.md
    chapters=$(find "${path}${guide}" -maxdepth 1 -type f | cut -d/ -f2 | sort | wc -l)
    echo $chapters >> book-stats.md
    echo chapters=$((chapters + $chapters))
    total_chapters=$((total_chapters + $chapters))

    # count subchapters in each guide
    echo "Number of subchapters"
    echo "Number of subchapters"  >> book-stats.md
    subchapters=$(find "${path}${guide}" -type f | cut -d/ -f2 | sort | wc -l)
    echo $subchapters >> book-stats.md
    echo subchapters=$((subchapters + $subchapters))
    total_subchapters=$((total_subchapters + $subchapters))

done

# Sum all chapters and subchapters from all guides
echo "\nTotal number of chapters:" >>  book-stats.md
echo $total_chapters >>  book-stats.md
echo "Total number of subchapters:" >>  book-stats.md
echo $total_subchapters >>  book-stats.md
