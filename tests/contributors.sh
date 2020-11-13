#! /bin/bash
# Copy the latest contributors.md file content to afterword
# this will publish the contributors file online in The Turing Way book
<<<<<<< HEAD

all_contributors="./README.md" # Path to the main README file of The Turing Way
contributors_highlight="./contributors.md"
contributors_record="./book/website/afterword/contributors-record.md"
=======
all_contributors='./README.md' # Path to the main README file of The Turing Way
contributors_highlight='./contributors.md'
contributors_record='./book/website/afterword/contributors-record.md'
>>>>>>> f1fa2fa88f705760313b340bf804cd5d77c719d1

# Copy everything from the contributors highlight
echo '(aw-contributors-record-highlights)=' > $contributors_record
cat $contributors_highlight >> $contributors_record

# # Get linenumber where all contributors list starts
line_num=$(grep -n '## Contributors' $all_contributors | cut -d: -f1)
echo '\n(aw-contributors-record-contributors)=' >> $contributors_record

tail -n +"$line_num" "$all_contributors" | while read line;
do
  echo $line >> $contributors_record
done
