#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
メイン関数がある。Launch.pyから呼ばれる
"""

__author__ = 'RYOTARO Yamamoto'
__version__ = '1.0.0'
__date__ = '2023/12/07 (Created: 2023/12/07)'

def for_else_test1(stop_at):
	"""
	stop_atでループを終了する

	>>> for_else_test1(5)
	Don't finished...
	>>> for_else_test1(15)
	Finished!
	"""
	flag = True
	for i in range(1, 10):
		if i >= stop_at:
			flag = False
			break
	if flag:
		return "Finish!"

	return "Don't finished..."


def for_else_test2(stop_at):
	"""
	stop_atでループを終了する

	>>> for_else_test2(5)
	Don't finished...
	>>> for_else_test2(15)
	Finished!
	"""
	for i in range(1, 10):
		if i >= stop_at:
			break
	else:
		return "Finished!"

	return "Don't finished..."

def main():
	"""
	forとフラグ変数を使った場合、for-elseを使った場合をテストする。
	"""
	print("--- forとフラグを使った場合 ---")
	a_result1 = for_else_test1(5)
	a_result2 = for_else_test1(15)

	print(a_result1)
	print(a_result2)

	print()

	print("--- for-elseを使った場合 ---")
	a_result1 = for_else_test2(5)
	a_result2 = for_else_test2(15)

	print(a_result1)
	print(a_result2)

	return 0

if __name__ == '__main__':
	import doctest
	import sys

	doctest.testmod()
	sys.exit(main())
