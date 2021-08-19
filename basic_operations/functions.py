"""
Some starter fucntion

"""
from basic_operations._xh import check_solution

"""
write function to count a string
"""
def count_a_string(input):

"""
write function to count a string
"""
def count_a_list(input):
    print("my input is\n", input)
    x=len(input)
    print("my answer is \n", x)
    return x


"""
write a function to reverse a list
"""
def reverse_a_list(input:list):
    print("my input is", input)
    input.reverse()
    print("my output is", input)

    return input



"""
write a fucction that multipies number
"""
def multiplies_two_numbers(a, b):
    pass


"""
write a function that create a new file called "c" in your present working directory (pwd)


"""
def create_in_pwd():
    pass


"""
write a function that create a new file called "test_file2.txt" in your present working directory (pwd)
"""


def create_in_desktop():
    pass




"""
write a function that:
    - creates a new file called "test_file3.txt" in your current directory
    - the content of the file should be each number on the input list


"""
def create_in_pwd_with_input(input_list):
    pass




"""
write a function that filters input list and returns only numbers


"""
def create_filter_int(input):
    pass



"""
write a function that filters input list and returns only string

"""
def create_filter_str(input):
    pass


"""
write a function that fetches this api https://api.discogs.com/releases/249504
it should return data as a string
"""
def api_request_function():
    pass


"""
write a function that fetches this api https://api.discogs.com/releases/249504
it should return data as a  dict (or json)
"""
def api_request_function_json():

    return

"""
write a function that fetches this api https://api.discogs.com/releases/249504
it should return all the artist names in a list
"""
def api_request_function_vids():
    pass



if __name__ == '__main__':

    check_solution()