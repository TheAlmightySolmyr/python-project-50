import os

from gendiff.gendiff_description import generate_diff

ff1_yaml = 'test_data/ff1_yaml.yml'
ff2_yaml = 'test_data/ff2_yaml.yml'

ff1_json = 'test_data/ff1.json'
ff2_json = 'test_data/ff2.json'


def test_generate_diff_json():
    file1_path = os.path.join(os.path.dirname(__file__), ff1_json)
    file2_path = os.path.join(os.path.dirname(__file__), ff2_json)
    expected_diff = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            key: value
            doge: {
              - wow:
              + wow: so much
            }
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

    diff = generate_diff(file1_path, file2_path)

    assert diff == expected_diff


def test_generate_diff_yaml():
    file1_path = os.path.join(os.path.dirname(__file__), ff1_yaml)
    file2_path = os.path.join(os.path.dirname(__file__), ff2_yaml)

    expected_diff = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            key: value
            doge: {
              - wow:
              + wow: so much
            }
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

    diff = generate_diff(file1_path, file2_path)

    assert diff == expected_diff