#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
メイン関数がある。Launch.pyから呼ばれる
"""

__author__ = 'RYOTARO Yamamoto'
__version__ = '1.0.0'
__date__ = '2023/12/07 (Created: 2023/12/07)'

import asyncio

async def unko():
	"""
	非同期でうんこをする関数
	"""
	await asyncio.sleep(5)
	print("うんこ完了")

async def hamigaki():
	"""
	非同期ではみがきをする関数
	"""
	await asyncio.sleep(3)
	print("はみがき完了")

async def morning_routine():
	"""
	モーニングルーティンを制御する関数
	"""
	print("モーニングルーティンを開始する")
	await asyncio.gather(unko(), hamigaki())
	print("モーニングルーティンを終了する")

def main():
	"""
	>>> main()
	モーニングルーティンを開始する
	はみがき完了
	うんこ完了
	モーニングルーティンを終了する
	0
	"""
	# モーニングルーティンを開始する
	asyncio.run(morning_routine())
	return 0

if __name__ == '__main__':
	import doctest
	import sys

	doctest.testmod()
	sys.exit(main())
