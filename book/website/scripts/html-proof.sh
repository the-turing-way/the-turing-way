#!/usr/bin/env bash
set -e # halt script on error

make site 
bundle exec htmlproofer  --assume-extension ./_site \
--url-ignore "/\/apple-touch*.*/" \
--disable-external \
--only_4xx \
--allow-hash-href 