#! /bin/bash
# Copy the latest contributors.md file content to afterword
# this will publish the contributors file online in The Turing Way book
all_contributors='README.md' # Path to the main README file of The Turing Way
contributor_highlights='contributors.md'
contributor_records='book/website/afterword/contributor-records.md'
latin_list=

# Copy everything from the contributors highlight
echo '(aw-contributor-records-highlights)=' > $contributor_records
cat $contributor_highlights >> $contributor_records

# # Get linenumber where all contributors list starts
line_num=$(grep -n '## Contributors' $all_contributors | cut -d: -f1)
#echo $line_num
#echo '\n## Contributors\n' >> $contributor_records
echo '\n(aw-contributor-records-contributors)=' >> $contributor_records

tail -n +"$line_num" "$all_contributors" | while read line;
do
  echo $line >> $contributor_records
done

sed -i '' 's/etc/.../g' $contributor_records
sed -i '' 's/i.e./like/g' $contributor_records
sed -i '' 's/ie/like/g' $contributor_records
sed -i '' 's/e.g./such as/g' $contributor_records
