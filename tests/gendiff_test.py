from pathlib import Path

import pytest

from gendiff.gendiff_body import generate_diff


@pytest.fixture
def expected_diff():
    expected = Path(__file__).parent / 'test_data' / 'expected_diff.txt'
    return expected


@pytest.fixture
def expected_plain():
    expected = Path(__file__).parent / 'test_data' / 'expected_diff_plain.txt'
    return expected


@pytest.fixture
def expected_json():
    expected = Path(__file__).parent / 'test_data' / 'expected_diff_json.json'
    return expected


@pytest.fixture
def testing_file_json():
    first = Path(__file__).parent / 'test_data' / 'ff1.json'
    second = Path(__file__).parent / 'test_data' / 'ff2.json'
    return first, second


@pytest.fixture
def testing_file_yaml():
    first = Path(__file__).parent / 'test_data' / 'ff1_yaml.yml'
    second = Path(__file__).parent / 'test_data' / 'ff2_yaml.yml'
    return first, second


def test_gendiff(expected_diff, testing_file_json, testing_file_yaml):
    testing_file_yml1, testing_file_yml2 = testing_file_yaml
    testing_file_json1, testing_file_json2 = testing_file_json
    assert generate_diff(
        testing_file_yml1, testing_file_yml2
        ) == expected_diff.read_text()
    assert generate_diff(
        testing_file_json1, testing_file_json2
        ) == expected_diff.read_text()


def test_gendiff_plain(expected_plain, testing_file_json, testing_file_yaml):
    testing_file_yml1, testing_file_yml2 = testing_file_yaml
    testing_file_json1, testing_file_json2 = testing_file_json
    assert generate_diff(
        testing_file_yml1, testing_file_yml2, 'plain'
        ) == expected_plain.read_text()
    assert generate_diff(
        testing_file_json1, testing_file_json2, 'plain'
        ) == expected_plain.read_text()


def test_gendiff_json(expected_json, testing_file_json, testing_file_yaml):
    testing_file_yml1, testing_file_yml2 = testing_file_yaml
    testing_file_json1, testing_file_json2 = testing_file_json

    assert generate_diff(
        testing_file_yml1, testing_file_yml2, 'json'
    ) == expected_json.read_text()
    
    assert generate_diff(
        testing_file_json1, testing_file_json2, 'json'
    ) == expected_json.read_text()