#!/usr/bin/env bash
set -e # halt script on error

make site 
bundle exec htmlproofer  --assume-extension ./_site --disable-external --only_4xx