cd ../..
git clone https://github.com/tonyyzy/po4jupyterbook
cd book/content
python3 ../../po4jupyterbook/tools/poc.py
cd ../website
sed 's+content_folder_name: ../content+content_folder_name: ../content/locale/+g' _config.yml > _config-locale.yml
cat ../content/po/LINGUAS | while read lang;
do
    echo ${lang}
    sed "s/url: /url: ${lang}\//g" _data/toc.yml.bak > _data/toc.yml
    jupyter-book build ./ --overwrite --config _config-locale.yml
    find _build/${lang}/ -name *.md -exec sed -i s+../figures+../../figures+g {} +
    bundle exec jekyll build
    rm -r _build/${lang}
done
cp _data/toc.yml.bak _data/toc.yml