cd ../..
git clone https://github.com/tonyyzy/po4jupyterbook
cd book/content
# Compile Markdown files from POT files
python3 ../../po4jupyterbook/tools/poc.py
cd ../website
# Copy the config file and change the location of the content to locale where 
# the translated Markdown files will be
sed 's+content_folder_name: ../content+content_folder_name: ../content/locale/+g' _config.yml > _config-locale.yml
# Make backup of the original table of content
cp _data/toc.yml _data/toc.yml.bak
cat ../content/po/LINGUAS | while read lang;
do
    echo ${lang}
    # Make language specific table of content
    sed "s/url: /url: \/${lang}\//g" ../content/po/toc.yml > _data/toc.yml
    # Use the locale config to build each language version of the book
    jupyter-book build ./ --config _config-locale.yml
    # Change the path to figures directory one level higher
    # This will use the figures from the English version
    # Should a translated figure exist, it will reside in a folder different
    # from the sed match here
    find _build/${lang}/ -name *.html -exec sed -ie "s+\.\./figures+../../figures+g" {} \;
    bundle exec jekyll build
    # Remove the translated Markdown from the _build directory otherwise jekyll 
    # will build those files again
    rm -r _build/${lang}
done
# Restore the table of content to the oiginal version
cp _data/toc.yml.bak _data/toc.yml