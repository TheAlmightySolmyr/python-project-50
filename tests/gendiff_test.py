import os

from gendiff.gendiff_description import generate_diff

ff1_yaml = 'test_data/ff1_yaml.yml'
ff2_yaml = 'test_data/ff2_yaml.yml'


def test_generate_diff_json():
    file1_path = os.path.join(os.path.dirname(__file__), 'test_data/ff1.json')
    file2_path = os.path.join(os.path.dirname(__file__), 'test_data/ff2.json')
    expected_diff = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    diff = generate_diff(file1_path, file2_path)
    assert diff == expected_diff


def test_generate_diff_yml():
    file1_path = os.path.join(os.path.dirname(__file__), ff1_yaml)
    file2_path = os.path.join(os.path.dirname(__file__), ff2_yaml)
    expected_diff = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    diff = generate_diff(file1_path, file2_path)
    assert diff == expected_diff