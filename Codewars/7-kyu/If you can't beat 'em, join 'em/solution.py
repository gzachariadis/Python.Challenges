from itertools import chain

def cant_beat_so_join(lsts):
	return list(chain.from_iterable(sorted(lsts, key = sum, reverse = True)))
