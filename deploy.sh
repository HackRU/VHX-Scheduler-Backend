#! /bin/bash
source bin/activate
pip install -r requirements.txt
mkdir deploy/
cp -r lib/python3.6/site-packages/ deploy/

for var in "$@"
do
	cp $var deploy/
done
cp config.py deploy/
cd deploy/
zip -r dep.zip *
cd ..
cp deploy/dep.zip .
rm -rf deploy/
