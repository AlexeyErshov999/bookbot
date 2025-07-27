from stats import get_words_count, get_chars_count, get_sorted_chars_dicts


def get_book_text(path):
	with open(path) as file:
		return file.read()
	

def main(path):
    text = get_book_text(path)
    sorted_dict_of_chars = get_sorted_chars_dicts(get_chars_count(text))
    
    char_lines = []
    for item in sorted_dict_of_chars:
        char = item["char"]
        if not char.isalpha():
            continue
        char_lines.append(f"{char}: {item['num']}")

    joined_output = "\n".join(char_lines)
    
    print(f'''
	============ BOOKBOT ============
	Analyzing book found at books/frankenstein.txt...
	----------- Word Count ----------
	Found {get_words_count(text)} total words
	--------- Character Count -------
    {joined_output}
	============= END ===============
    ''')


main("./books/frankenstein.txt")