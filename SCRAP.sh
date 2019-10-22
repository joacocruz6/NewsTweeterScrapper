#!/bin/bash
cd src/webscrapper/ && python3 webscraper.py https://twitter.com/latercera latercera_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/elmostrador elmostrador_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/Emol mercurio_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/T13 trece_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/La_Segunda la_segunda_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/CHVNoticias chv_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/meganoticiascl mega_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/24HorasTVN tvn_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/lacuarta la_cuarta_data.json
cd ../webscrapper/ && python3 webscraper.py https://twitter.com/lun lun_data.json

cd ../bdUploader/ && python3 uploader.py latercera_data.json
cd ../bdUploader/ && python3 uploader.py elmostrador_data.json
cd ../bdUploader/ && python3 uploader.py mercurio_data.json
cd ../bdUploader/ && python3 uploader.py trece_data.json
cd ../bdUploader/ && python3 uploader.py la_segunda_data.json
cd ../bdUploader/ && python3 uploader.py chv_data.json
cd ../bdUploader/ && python3 uploader.py mega_data.json
cd ../bdUploader/ && python3 uploader.py tvn_data.json
cd ../bdUploader/ && python3 uploader.py la_cuarta_data.json
cd ../bdUploader/ && python3 uploader.py lun_data.json
python3 exporter.py
