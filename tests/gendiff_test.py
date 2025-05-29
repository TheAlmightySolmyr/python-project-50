from pathlib import Path

from gendiff.gendiff_description import generate_diff


def test_gendiff():
    test_data_dir = Path(__file__).parent / 'test_data'
    ff1_yaml = test_data_dir / 'ff1_yaml.yml'
    ff2_yaml = test_data_dir / 'ff2_yaml.yml'
    ff1_json = test_data_dir / 'ff1.json'
    ff2_json = test_data_dir / 'ff2.json'
    expected_diff = (test_data_dir / 'expected_diff.txt').read_text()
    assert generate_diff(ff1_yaml, ff2_yaml) == expected_diff
    assert generate_diff(ff1_json, ff2_json) == expected_diff


def test_gendiff_plain():
    test_data_dir = Path(__file__).parent / 'test_data'
    ff1_yaml = test_data_dir / 'ff1_yaml.yml'
    ff2_yaml = test_data_dir / 'ff2_yaml.yml'
    ff1_json = test_data_dir / 'ff1.json'
    ff2_json = test_data_dir / 'ff2.json'
    expected_diff = (test_data_dir / 'expected_diff_plain.txt').read_text()
    assert generate_diff(ff1_yaml, ff2_yaml, 'plain') == expected_diff
    assert generate_diff(ff1_json, ff2_json, 'plain') == expected_diff