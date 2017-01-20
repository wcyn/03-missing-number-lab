def find_missing(l1, l2):
	extra = set(l1)^set(l2)
	if extra:
		return extra.pop()
	return 0
