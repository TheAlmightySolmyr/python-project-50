import os

from gendiff.gendiff_description import generate_diff


def test_generate_diff():
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