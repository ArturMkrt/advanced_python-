def get_chars_set_with_count(s):
	a = {}
	for c in s:
		if c in a:
			a[c] +=1
		else:
			a[c]= 1
	return a

def dup_without_same_symbol_count(strs):
	start = set(strs[0])
	i = 1
	while i<len(strs) and len(start):
		start = start.intersection(set(strs[i]))
		i += 1
	return len(start)


def dup_with_same_symbol_count(strs):
	start = get_chars_set_with_count(strs[0])
	i = 1
	while i<len(strs) and len(start):
		a = get_chars_set_with_count(strs[i])
		for c in list(start.keys()):
			if c in a:
				start[c] = min(a[c], start[c])
			else:
				del start[c]
		i += 1
	return sum(start.values())


def get_dup_count(strs,same_symbol = False):
	if same_symbol:
		return dup_with_same_symbol_count(strs)
	else:
		return dup_without_same_symbol_count(strs)


print(get_dup_count(['abc','abd','abe'],False))
#////////////////////////////////////////////////////////////////////
def get_dup_count(strs,same_symbol = False):
  lists = [list(s) for s in strs[1:]]
  if same_symbol:
    chars = list(strs[0])
  else:
    chars = list(set(strs[0]))
  for i in range(len(lists)):
    j = 0
    while j < len(chars):
      if chars[j] in lists[i]:
        if same_symbol:
          lists[i].remove(chars[j])
        j += 1
      else:
        del chars[j]
  return len(chars)