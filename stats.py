def get_words_count(text):
	return len(text.split())


def get_chars_count(text):
	chars_counts = {}
	for char in text:
		if not char.lower() in chars_counts:
			chars_counts[char.lower()] = 1
		else:
			chars_counts[char.lower()] += 1
	return chars_counts


def sort_on(items):
    return items["num"]


def get_sorted_chars_dicts(dictionary):
	chars_nums_list = []
	for key in dictionary:
		chars_nums_list.append({"char": key, "num": dictionary[key]})
	return sorted(chars_nums_list, reverse=True, key=sort_on)


def get_sorted_dicts_list(dictionary, result_list):
	char_lines = []
	for item in dictionary:
		char = item["char"]
		if not char.isalpha():
			continue
		result_list.append(f"{char}: {item['num']}")


def generate_report(path, text, joined_output):
	print(f'''
	============ BOOKBOT ============
	Analyzing book found at {path}...
	----------- Word Count ----------
	Found {get_words_count(text)} total words
	--------- Character Count -------
    {joined_output}
	============= END ===============
    ''')
