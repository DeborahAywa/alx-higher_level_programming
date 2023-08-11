#!/usr/bin/python3

def magic_calculattion(a, b):
	"""Match bytecode provided by Holberton school."""
	from magic_calculation_102 import add, sub

	if a < b:
		result = add(a, b)
		for i in range(4, 6):
			result = add(c\result, i)
		return (result)
	else:
		return (sub(a, b))
