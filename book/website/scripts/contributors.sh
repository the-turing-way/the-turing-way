#! /bin/bash
# Copy the latest contributors.md file content to afterword
# this will publish the contributors file online in The Turing Way book
all_contributors='../../README.md' # Path to the main README file of The Turing Way
contributor_highlights='../../contributors.md'
contributor_record='afterword/contributors-record.md'

# Copy everything from the contributors highlight
echo '(aw-contributors-record-highlights)=' > $contributor_record
cat $contributor_highlights >> $contributor_record

# # Get linenumber where all contributors list starts
line_num=$(grep -n '## Contributors' $all_contributors | cut -d: -f1)
echo '\n(aw-contributors-record-contributors)=' >> $contributor_record

tail -n +"$line_num" "$all_contributors" | while read line;
do
  echo $line >> $contributor_record
done
