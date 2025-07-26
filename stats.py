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
