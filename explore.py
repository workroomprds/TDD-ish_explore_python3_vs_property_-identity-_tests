#!/usr/bin/env python3

import math
from random import *

def raise_two_to_the_power_of(subject):
	"""returns power of 2"""
	return pow(2,subject)

def take_logarithm_of_2(subject):
	"""returns log of 2 - inverse of power of 2"""
	return math.log2(subject)

def convert_to_string(subject):
	"""returns a string"""
	return str(subject)
	
def convert_to_int(subject):
	"""returns an int - possible inverse of str"""
	return int(subject)

def convert_to_float(subject):
	"""returns a float - possible inverse of str"""
	return float(subject)

class divideMultiplyThing:
	"""To return functions alreeady set up to divide / multiply / whatever by a particaulr number, entered in init"""
	def __init__(self, n):
		self.partcular_number = n
	def divideBy(self, subject):
		return(subject / self.partcular_number)
	def multiplyBy(self, subject):
		return(subject * self.partcular_number)

def make_power(thing):
	return(pow(10,thing))

def test_transformers():
	"""Testing that the transformers transform at least one thing in a reasonable way"""
	assert (raise_two_to_the_power_of(3) == 8)
	assert (take_logarithm_of_2(8) == 3)
	assert (convert_to_string(10) == "10")
	assert (convert_to_int("0100") == 100)
	d = divideMultiplyThing(5)
	assert (d.divideBy(10) == 2)
	assert (d.multiplyBy(10) == 50)
	
test_transformers()

#----

def get_int_range_around_0(size, steps=0)->list:
	"""Returns a list of ints from - to + size, in specified no. of gaps (so returns one more entry)"""
	if (steps == 0): #also default
		steps = size
	return list(range(-size,size+1,int(2*size/steps)))

def get_int_range_from_0(size, steps=0)->list:
	"""Returns a list of ints from 0 to + size, in specified no. of gaps (so returns one more entry)"""
	if (steps == 0): #also default
		steps = size
	return list(range(0,size+1,int(size/steps)))

def get_a_bunch_of_random_ints(howmany, offset=0, mult=100)->list:
	"""Returns a list of random ints"""
	output = map(int, get_a_bunch_of_random_floats(howmany, offset, mult)) 
	return list(output)

def get_a_bunch_of_random_floats(howmany, offset=0, mult=100)->list:
	"""Returns a list of randon floats"""
	output = []
	for item in range(howmany):
		output.append(offset+mult*random())
	return output

def test_generators():
	assert (get_int_range_around_0(10, 4) == [-10, -5, 0, 5, 10]) ## Approval test
	assert (get_int_range_from_0(10, 2) == [0,5,10]) ## Approval test
	# no tests yet for get_a_bunch_of_random_ints
	# no tests yet for get_a_bunch_of_random_floats

test_generators()
	
#---
	
def make_test(do_something, reverse_something):
	"""Returns a function which, given a value, checks that two functions work together to rethrn the value to its starting state"""
	def test_identity(original):
		transformed = do_something(original)
		reverted_to_original = reverse_something(transformed)
		message = " : ".join([str(original), str(transformed), str(reverted_to_original), str(original == reverted_to_original)])
		assert original == reverted_to_original , message
		return message

	return test_identity

def test_checker():
	def add_one(x):
		return x+1
	def take_one(x):
		return x-1
	
	this_test = make_test(add_one, take_one)
	
	assert this_test(1) ==  '1 : 2 : 1 : True' #Approval test
	
	#commented out because it's going to fail, and I've not written a try/catch that is worthwhile
	#that_test = make_test(add_one, add_one)
	#try:
	#	assert that_test(5) !=  '5 : 6 : 5 : True' #Approval test
	#finally:
	#	pass

test_checker()


#---

def look_for_oddness_in_powers_of_two():
	"""Runs a bunch of tests looking at powers of two in order to look at very large numbers"""
	testIdentity = make_test(raise_two_to_the_power_of, take_logarithm_of_2)
	test_points = get_int_range_around_0(1000, 20)
	for item in test_points:
		print(testIdentity(item))

def look_for_oddness_in_conversions():
	"""Runs a bunch of tests to look at converting to / from ints, floats and strings"""
	testIdentity = make_test(convert_to_string, convert_to_int)
	test_points = get_int_range_around_0(9999999999999999999999, 20)
	#Next thing here, to get moving
	#edges = 1E20
	#test_points = get_a_bunch_of_random_ints(100, -edges, 2*edges )
	
	for item in test_points:
		print(testIdentity(item))
		
def look_for_oddness_in_precision():
	"""Runs a bunch of tests looking at divide and multiply (in that order) - note double-depth"""
	big_test_points = get_int_range_from_0(1000)
	for item in big_test_points:
		print(item)
		if (item == 0):
			item = 1
		d = divideMultiplyThing(item)
		testIdentity = make_test( d.divideBy, d.multiplyBy)
		
		test_points = get_int_range_around_0(1000)
		for item in test_points:
			testIdentity(item)
			#print(testIdentity(item))

look_for_oddness_in_precision()
	
	