# Clear then populate the lib dir
shopt -s extglob
rm -rf lib/!(README.md)
pip install -r requirements.txt -t lib/