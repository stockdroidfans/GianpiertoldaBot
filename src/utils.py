# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
	# [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)

	© 2021 [Stockdroid Fans](https://github.com/stockdroidfans)
	Licensed under the MIT [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)

	---

	General–purpose utilities

	```python
	from gianpiertolda import utils
	```
'''

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

# Imports
''' System '''
import sys, os, time, logging, traceback

''' Libraries '''
import utils, json, html, random, hashlib, rich
from rich import print
from rich.logging import RichHandler

''' Platforms '''
import pyrogram
import discord

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

class CacheFullError(Exception): pass

class Cache:
	'''
		Creates a new cache object. Caches are used to temporarily store data in
		lists with specific properties and will be reset once memory is cleared
		or the program terminates.

		To get the list object, use the `.get()` method.

		---

		```python
			from gianpiertolda import utils

			my_cache = utils.Cache(
				threshold = 256, accepts = [str]
			)
			my_cache.store('hello world')

			my_cache.get() # ['hello world']
		```

		---

		| Property | Type | Default | Description |
		| -------- | ---- | ------- | ----------- |
		| `threshold` | `int` | `512` | Defines a maximum amount of objects that can be stored in this cache. Attempting to store any object after this limit is reached will raise an `CacheFullError` |
		| `accepts` | `list` | `[]` | A list of types that this cache will accept |
	'''
	def __init__(self,
		threshold: int = 512, accepts: list = [],
	*args, **kwargs):
		self.threshold = threshold
		# If the list is empty (len(accepts) == false), then any value can be accepted
		self.accepts = accepts if len(accepts) else True
		
		self.array: list

	def get(self,
	*args, **kwargs):
		return self.array
	
	def store(self,
		object,
	*args, **kwargs):
		# Checks if the amount of objects already in cache exceed the given threshold
		if len(self.array) <= self.threshold:
			# Checks if cache can accept this object, or if self.accepts is True
			if type(object) in self.accepts or self.accepts:
				self.array.append(object) # append the object
			else: raise TypeError(f'cache does not accept {type(object)} (cache only accepts {", ".join(self.accepts[0:-2]) + " and " + self.accepts[:-1]})')
		else: raise CacheFullError(f'cache is full (hit the threshold of {self.threshold})')

class Log: pass # under construction

def true(
	object, fallback = None,
*args, **kwargs):
	'''
		Returns the object if it's true, else returns a fallback value.
		If an array is given, removes the objects in an array which are
		false.

		---

		```python
			from gianpiertolda import utils
			from utils import true

			my_number = 2
			something = False
			my_list = [0, '', 1, True, 255]
			my_dict = {'i': True, 'a': False, 'b': 'hello'}

			true(2) # 2
			true('', fallback = 727) # 727
			true(0) # None
			true([0, '', 1, True, 255]) # [1, True, 255]
		```

		---

		| Argument | Type | Default | Description |
		| -------- | ---- | ------- | ----------- |
		| `object` | Any | | Object to evaluate |
		| `fallback` | Any | `None` | Return value if `object` is false |
	'''
	if object: return object
	if type(object) in (list, tuple, set, dict):
		for i, x in enumerate(object):
			if not x: object.remove(x)
		return object
	return fallback

def find(
	array: list or tuple,
	key: any, value: any,
	*args, **kwargs
):
	'''
		Returns the index of the dict that has '`key`' equal to '`value`'
		in a list or tuple.

		---

		```python
			from gianpiertolda import utils

			foo = [
				{'id': 104, 'content': 'hello world'},
				{'id': 255, 'content': 'hello galaxy'}
			]

			bar = utils.find(foo, 'id', 104) # 0
			baz = foo[bar] # {'id': 104, 'content': 'hello world'}
		```

		---

		| Argument | Type | Description |
		| -------- | ---- | ----------- |
		| `array` | `list` or `tuple` | Input array |
		| `key` | `any` | Key to check the value of |
		| `value` | `any` | Value that `key` needs to match |
	'''
	for e, dictionary in enumerate(array):
		if dictionary[key] == value:
			return e

def gather(
	key: dict, catches: dict,
	*args, **kwargs
):
	'''
		Checks if a dictionary contains all the keys in '`catches`'. If not,
		appends it to the dictionary with the corresponding value.

		---

		```python
			from gianpiertolda import utils

			dict_1 = {'a': 'b', 'wait': 'but'}
			dict_2 = {'a': 'b', 'why': '??'}

			utils.gather(dict1, dict2) # {'a': 'b', 'wait': 'but', 'why': '??'}
		```

		---

		| Argument | Type | Description |
		| -------- | ---- | ----------- |
		| `key` | `dict` | Input dictionary |
		| `catches` | `dict` | Fallback dictionary to catch values from if `key` does not contain them |
	'''
	for catch in catches:
		key[catch] = key.get(catch, catches[catch])
	return key

def validate(
	string: str,
	pattern: str = r'^(?=.{8,20})[a-zA-Z0-9_]', fix: bool = False,
	*args, **kwargs
):
	'''
		Validates a string based on a regex pattern (defaults to alphanumeric
		validation, AKA username validation). Returns the original string if
		it matches the pattern.

		---

		```python
			from gianpiertolda import utils

			utils.validate('StuckDuck') # 'StuckDuck'
			utils.validate('a comically large string of text') # False
			utils.validate('My_text', pattern = r'[a-z0-9]') # False
		```

		---

		| Argument | Type | Description |
		| -------- | ---- | ----------- |
		| `string` | `str` | String to validate |
		| `pattern` | `str` | Regex pattern `string` has to match |
		| `fix` | `bool` | Whether or not calling the function with an unmatching string should return the string, modified to match the pattern |
	'''
	import re
	if re.fullmatch(pattern, string):
		return string
	else:
		if fix: return re.sub(
			'^' + pattern,
			pattern,
			string
		)
		else: return False