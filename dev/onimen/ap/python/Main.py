#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
メイン関数がある。Launch.pyから呼ばれる
"""

__author__ = 'RYOTARO Yamamoto'
__version__ = '1.0.0'
__date__ = '2023/12/07 (Created: 2023/12/07)'

def main():
	"""
	>>> main()
	Hi there?
	0
	"""

	print("Hi there?")
	return 0

if __name__ == '__main__':
	import doctest
	import sys

	doctest.testmod()
	sys.exit(main())
