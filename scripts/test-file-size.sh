#! /bin/bash
# add any files you want the test to ignore between the two ENDOFLIST placeholders. 
# one file per line
read -r -d '' IGNORE_LIST <<'ENDOFLIST'
./conferences/presentations/MRCBSU_20190320/Whitaker_MRCBSU_TheTuringWay_March2019.pdf
ENDOFLIST

echo "Performing file size checks..."
echo
echo "Ignoring known large files:"
echo "$IGNORE_LIST"
echo
FIND_IGNORES=$(printf "! -path %s " ${IGNORE_LIST})
BIG_FILES=$(find .  -size +5M  -type f ${FIND_IGNORES} ! -path "./.git/*" -print)
if [ ! -z "$BIG_FILES" ]; then
    echo "Error, unexpected large (data?) files found:" 1>&2
    echo "$BIG_FILES" 1>&2
    exit -1
else
    echo "No large files found."
fi
