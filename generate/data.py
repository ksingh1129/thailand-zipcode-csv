import json
import csv

from generate.utilities import transform_sub_district, transform_district, transform_province, transform_camel_case

csvFilePath = "data/tambons.csv"
dbJsonUrl = "data/raw_database.json"


def get_zip_code(code):
    with open(dbJsonUrl, 'r', encoding='UTF8') as dbJsonFile:
        data = json.loads(dbJsonFile.read())
        for i in data:
            if i['district_code'] == code:
                return i['zipcode']
                break


def create_thailand_zip_code_csv_file():
    with open(csvFilePath, encoding='UTF8') as csvFile:
        read_csv = csv.reader(csvFile, delimiter=',')
        next(read_csv)
        sub_district_list = list(read_csv)
        with open('./dist/thailand_zip_codes.csv', 'w', newline='', encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow(
                ["SubDistrictId", "SubDistrictNameTH", "SubDistrictNameEN", "SubDistrictCamelCase", "ZipCode",
                 "DistrictId", "DistrictNameTH", "DistrictNameEN", "DistrictNameCamelCase", "ProvinceId",
                 "ProvinceNameTH", "ProvinceNameEN", "ProvinceCamelCase"])
            for row in sub_district_list:
                writer.writerow(
                    [
                        row[1], transform_sub_district(row[2]), row[3], transform_camel_case(row[3]), get_zip_code(int(row[1])),
                        row[4], transform_district(row[5]), row[6], transform_camel_case(row[6]), row[7],
                        transform_province(row[8]), row[9], transform_camel_case(row[9])
                    ])
