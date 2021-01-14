#! /bin/bash
# Copy the latest contributors.md file content to afterword
# this will publish the contributors file online in The Turing Way book

all_contributors="./README.md" # Path to the main README file of The Turing Way
contributors_highlight="./contributors.md"
contributors_record="./book/website/afterword/contributors-record.md"

# Copy everything from the contributors highlight
echo '(contributors-record-highlights)=' > $contributors_record
cat $contributors_highlight >> $contributors_record

# Get linenumber where all contributors list starts
line_num=$(grep -n '## Contributors' $all_contributors | cut -d: -f1)
echo '\n(contributors-record-contributors)=' >> $contributors_record

tail -n +"$line_num" "$all_contributors" | while read line;
do
  echo $line >> $contributors_record
done
