# This script explains how to make 
# functional decoration very simply.

# ------------------------
# ~ yanwar live on @Gurka
# Kamis, 3 08 2017
# ------------------------

# How to use ?
# -----------------------------
# >>> import icantry_01
# >>> icantry_01.my_sentence()
# 'Ya.. you **** man!'


def bad_word_filtering(func):
	the_bad_words = [
		'fuck', 
		'babi', 
		'anjing',
		'bastard']
	replacer = "*"

	def wrapper():
		data = func().split(" ")

		for i, word in enumerate(data[:]):
			if word in the_bad_words:
				data[i] = replacer * len(word)

		return " ".join(data)

	wrapper.__name__ = func.__name__
	return wrapper


@bad_word_filtering
def my_sentence():
	return "Ya.. you fuck man!"

