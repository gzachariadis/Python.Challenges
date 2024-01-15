def get_middle(s):
	index, odd = divmod(len(s), 2)
	return s[index] if odd else s[index - 1 : index + 1]
