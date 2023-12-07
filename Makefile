PYTHON	= python
PYCS	= $(shell find . -name "*.pyc")
PYCACHE = $(shell find . -name "__pycache__")
PYDOC	= pydoc
TARGET	= Launch.py
WORKDIR	= ./
PACKAGE	= dev.onimen.ap.python
PYLINT	= pylint
LINTRC 	= pylintrc.txt
LINTRES	= pylintresult.txt

# PACKAGEを出力し、パイプでsedに渡し、'.'をすべて'/'に置き換える
PKGPATH	= $(shell echo $(PACKAGE) | sed -e 's/\./\//g')

# PACKAGEを出力し、パイプでcutに私、'.'で分割したときの1番目の値
PKG_ROOT = $(shell echo $(PACKAGE) | cut -d '.' -f1)

all:
	@:	# @はエコーを抑制する。「: 」は常に終了コード0を返すコマンド

clean:
	# *.pycファイルをすべて消し去る
	@for each in $(PYCS) ; do rm -rf $${each} ; done

	# __pycache__ディレクトリをすべて消し去る	
	@for each in $(PYCACHE) ; do rm -rf $${each} ; done

	# pylintの結果ファイルが存在したら削除する
	@if [ -e $(LINTRES) ] ; then rm -f $(LINTRES); fi

	# 現在のディレクトリ以下の".DS_Store"をすべて消し去る
	@find . -name '.DS_Store' -exec rm {} ";"

	# 現在のディレクトリ以下のファイル/ディレクトリの拡張属性をクリアする
	@xattr -cr ./

unittest:
	@find $(PKG_ROOT) -name '*.py' -exec $(PYTHON) {} -v ";"

test: all
	$(PYTHON) $(TARGET)

doc:
	$(PYDOC) ./$(TARGET) ./$()

pylint:
	@if [ -z `pip list --format=freeze | grep pylint` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install pylint); \
	fi

pip:
	@if [ -z `which pip`]; \
	then \
		(cd $(WORKDIR); curl -O https://bootstrap.pypa.io/get-pip.py); \
		(cd $(WORKDIR); sudo -H python get-pip.py); \
		(cd $(WORKDIR); rm get-pip.py); \
	else
		(cd $(WORKDIR); sudo -H pip install -U pip); \
	fi

lint: pylint clean
	@if [ ! -e $(LINTRC) ] ; then $(PYLINT) --generate-rcfile > $(LINTRC) ; fi
	$(PYLINT) --rcfile=$(LINTRC) --reports=n `find . -name "*.py"` > $(LINTRES) ; less $(LINTRES)

prepare: pip pylint

