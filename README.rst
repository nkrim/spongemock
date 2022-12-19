spongemock
##########
.. line-block::
	Me: Mock some text like spongebob would.
	You: mOCk SoMe TexT lIKe SpONGebOb wOuLd.

.. image:: http://pixel.nymag.com/imgs/daily/vulture/2017/05/16/16-spongebob-explainer.w710.h473.2x.jpg
	:alt: spongemock


How to Install
==============
``pip install spongemock``

or (for python3 specifically)

``pip3 install spongemock``


How To Use
==========
``spongemock [-h] [-c] [-b BIAS] [-s SEED | -S STRSEED] text [text ...]``

positional arguments
--------------------
``text`` - the text to mock. ThE tExT tO mOCk.

optional arguments
------------------
``-h``, ``--help`` - show this help message and exit

``-c``, ``--copy`` - copy the mocked text to the clipboard.
 
``-b BIAS``, ``--bias BIAS`` - this bias is used to successively increase the chance of swapping from the previously-mocked case. A value of ``0`` will ensure the chance is always 50/50, and a value of ``1`` will ensure that after the first random choice the capitalization perfectly oscilates. Default is ``0.5``.

``-s SEED``, ``--seed SEED`` - seed for random number generator. Can be any number or string (numbers are parsed).

``-S STRSEED``, ``--strseed STRSEED`` - seed for random number generator. Does not attempt to parse the string to a number.


Use as a Library
----------------
``from spongemock import spongemock``

for use as ``spongemock.mock()``, or

``from spongemock.spongemock import mock``

Pass the ``text``, and optional ``diversity_bias`` or ``random_seed`` keyword arguments, to the ``mock()`` function.


Contributors
------------
A big thanks to `dgw <https://github.com/dgw>`_ for their contributions.
