import sys
from stats import get_words_count, get_chars_count, get_sorted_chars_dicts, generate_report, get_sorted_dicts_list
	

def main():
    check_args()
    path = sys.argv[1]
    text = get_book_text(path)
    sorted_dict_of_chars = get_sorted_chars_dicts(get_chars_count(text))
    
    char_lines = []
    get_sorted_dicts_list(sorted_dict_of_chars, char_lines)

    joined_output = "\n".join(char_lines)
    
    generate_report(path, text, joined_output)
    

def get_book_text(path):
	with open(path) as file:
		return file.read()
     

def check_args():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)


main()