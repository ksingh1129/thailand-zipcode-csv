import re
import json


def transform_sub_district(value):
    return re.sub('ต\.|แขวง', '', value).strip()


def transform_district(value):
    return re.sub('อ\.', '', value).strip()


def transform_province(value):
    return re.sub('จ\.', '', value).strip()


def transform_camel_case(value):
    return ''.join(a.capitalize() for a in re.split('([^a-zA-Z0-9])', value) if a.isalnum())
