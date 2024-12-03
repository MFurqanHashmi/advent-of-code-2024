import os
from historian_hysteria import read_two_lists_from_text_file, find_total_discrepancy_between_two_lists


TEST_INPUT_FILE_PATH = os.path.join(
        os.path.dirname(__file__), "inputs", "test_input.txt"
    )


def test_givenTestInput_whenParseFile_thenGetExpectedLists():
    left_list = [3,4,2,1,3,3]
    right_list = [4,3,5,3,9,3]

    list_of_inputs = read_two_lists_from_text_file(TEST_INPUT_FILE_PATH)
    
    assert list_of_inputs[0] == left_list
    assert list_of_inputs[1] == right_list


def test_givenTwoLists_whenCalculatingTotalDiscrepancy_thenGetExpectedValue():
    left_list = [3,4,2,1,3,3]
    right_list = [4,3,5,3,9,3]
    expected_discrepancy = 11

    total_distance_discrepancy = find_total_discrepancy_between_two_lists(left_list, right_list)

    assert total_distance_discrepancy == expected_discrepancy


