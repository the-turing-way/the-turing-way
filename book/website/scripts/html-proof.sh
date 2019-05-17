#!/usr/bin/env bash
set -e # halt script on error

make site 
bundle exec htmlproofer --allow-hash-href \
--assume-extension ./_site \
--url-ignore "/\/apple-touch*.*/,/\/images/logo/favicon.ico/,/#*/" \
--disable-external \
--only_4xx 

