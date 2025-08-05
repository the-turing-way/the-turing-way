#! /bin/bash
# Copy the latest contributors.md file content to afterword
# this will publish the contributors file online in The Turing Way book

all_contributors='../../README.md' # Path to the main README file of The Turing Way
contributor_highlights='../../contributors.md'
collaborating_projects='../../collaborating_projects.md'
contributors_record='afterword/contributors-record.md'

# Copy everything from the contributors highlight
echo '(contributors-record-highlights)=' > $contributors_record
cat $contributor_highlights >> $contributors_record

# # Get linenumber where all contributors list starts
printf '\n(contributors-record-all)=' >> $contributors_record
printf '\n# All Contributors\n' >> $contributors_record
printf '\n✨Using [all-contributors](https://allcontributors.org/) specification, _The Turing Way_ recognises all contributors, not just the ones who push code. ✨\n' >> $contributors_record
line_num=$(grep -n '## Contributors' $all_contributors | cut -d: -f1)
printf '\n(contributors-record-contributors)=\n' >> $contributors_record

tail -n +"$line_num" "$all_contributors" | while read -r line;
do
  echo "$line" >> $contributors_record
done

# Copy everything from the collaborating projects files
printf '\n(contributors-record-collaborators)=\n' >> $contributors_record
cat $collaborating_projects >> $contributors_record
