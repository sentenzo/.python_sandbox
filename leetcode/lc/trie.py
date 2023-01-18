from collections import defaultdict

_trie = lambda: defaultdict(_trie)
trie = _trie()
_TERMINATOR_ = "\0" # the sign of the word's ending 

def trie_push(word, val = None):
	cur = trie
	for c in word:
		cur = cur[c]
	cur.setdefault(_TERMINATOR_, val)
	# val - can be an index of a word in array
	#     - or the amount of such words
	
def trie_check(word):
	cur = trie
	for c in word:
		if c not in cur:
			return False
		cur = cur[c]
	return _TERMINATOR_ in cur 
	# check if the word really ends with this char
	# cause it could be smth like "abc" in trie(["abcd"])