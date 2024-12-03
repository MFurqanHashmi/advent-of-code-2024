import os

def read_file(file_path: str):
  """
  Reads the content of a file.
  """
  with open(file_path, "r") as file:
    return file.read()
  
# Complexity = O(n)
def find_total_discrepancy_between_two_lists(left_list: list[int], right_list: list[int]) -> int:
    sorted_left_list = sorted(left_list)        
    sorted_right_list = sorted(right_list)

    distance_discrepancy_between_two_lists = []
    for i in range(len(sorted_left_list)):
        distance_apart = abs(sorted_left_list[i]-sorted_right_list[i])
        distance_discrepancy_between_two_lists.append(distance_apart)

    total_distance_discrepancy = 0
    for discrepancy in distance_discrepancy_between_two_lists:
        total_distance_discrepancy += discrepancy
    
    return total_distance_discrepancy

# Complexity = O(n)
def read_two_lists_from_text_file(file_path: str) -> list[list[int]]:
    file_content = read_file(file_path)
    
    left_list = []
    right_list = []
    for line in file_content.splitlines():
        nums = line.split()
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))
    
    return [left_list, right_list]




# ----

SAMPLE_INPUT_FILE_PATH = os.path.join(
        os.path.dirname(__file__), "inputs", "sample_input.txt"
    )
list_of_inputs = read_two_lists_from_text_file(SAMPLE_INPUT_FILE_PATH)
total_distance_discrepancy = find_total_discrepancy_between_two_lists(list_of_inputs[0], list_of_inputs[1])
print(f"Total Discrepancy = {total_distance_discrepancy}")