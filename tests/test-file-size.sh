#! /bin/bash
# Add file paths to any files test should ignore between the two ENDOFLIST placeholders.
# Specify file paths relative to the root of the repository, one file path per line.
# To test locally, ensure script is run from the root repository.
read -r -d '' IGNORE_LIST <<'ENDOFLIST'
./conferences/presentations/MRCBSU_20190320/Whitaker_MRCBSU_TheTuringWay_March2019.pdf
ENDOFLIST

echo "Performing file size checks..."
echo
echo "Ignoring known large files:"
echo "$IGNORE_LIST"
echo
FIND_IGNORES=$(printf "! -path %s " "${IGNORE_LIST}")
BIG_FILES=$(find .  -size +5M  -name "${FIND_IGNORES}" ! -path "./.git/*" -print)
if [ -n "$BIG_FILES" ]; then
    echo "Error, unexpected large (data?) files found:" 1>&2
    echo "$BIG_FILES" 1>&2
    exit 1
else
    echo "No large files found."
fi
