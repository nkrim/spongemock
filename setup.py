import setuptools
from distutils.core import setup
from os import path

# Helper functions
# ----------------
def readFile(file):
	with open(file) as f:
		return f.read()

# Arguments
# ------------
CLASSIFIERS = []

# Dynamic info
# ------------
VERSION 			= '0.2.1'
CLASSIFIERS 		+= [
						'Development Status :: 3 - Alpha',
					]

# Package/Dependency info
# ---------------
PACKAGES			= [	'spongemock'	]
PACKAGE_DIR 		= {	'spongemock': 'src'	}
DATA_FILES			= [ ('', ['README.rst','LICENSE']), ]
INSTALL_REQUIRES 	= [	'pyperclip>=1.5.27' ]

# Static info
# -----------
NAME 				= 'spongemock'
DESCRIPTION 		= 'Mock some text like spongebob would. mOCk SoMe TexT lIKe SpONGebOb wOuLd.'
LONG_DESCRIPTION 	= readFile(path.join(path.dirname(path.abspath(__file__)), 'README.rst'))
AUTHOR 				= 'Noah Krim'
AUTHOR_EMAIL 		= 'nkrim62@gmail.com'
LICENSE 			= 'MIT License'
URL 				= 'https://github.com/nkrim/spongemock'
KEYWORDS 			= 'spongemock spongebob squarepants meme mock text random'
ENTRY_POINTS		= { 'console_scripts': [ 'spongemock = spongemock.__main__:main' ] }
CLASSIFIERS 		+= [
						'Environment :: Console',
						'Intended Audience :: End Users/Desktop',
						'License :: OSI Approved :: MIT License',
						'Natural Language :: English',
						'Operating System :: OS Independent',
						'Programming Language :: Python',
						'Programming Language :: Python :: 2',
						'Programming Language :: Python :: 3',
						'Topic :: Text Processing',
						'Topic :: Text Processing :: Filters',
						'Topic :: Text Processing :: General',
						'Topic :: Utilities',
					]
ZIP_SAFE			= True

# Setup call
# ----------
setup(
	name=NAME,
	version=VERSION,
	description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	author=AUTHOR,
	author_email=AUTHOR_EMAIL,
	license=LICENSE,
	url=URL,
	keywords=KEYWORDS,
	entry_points=ENTRY_POINTS,
	packages=PACKAGES,
	package_dir=PACKAGE_DIR,
	data_files=DATA_FILES,
	install_requires=INSTALL_REQUIRES,
	classifiers=CLASSIFIERS,
	zip_safe=ZIP_SAFE )