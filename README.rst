spongemock
##########
Me: Mock some text like spongebob would.

You: mOCk SoMe TexT lIKe SpONGebOb wOuLd.

.. image:: http://pixel.nymag.com/imgs/daily/vulture/2017/05/16/16-spongebob-explainer.w710.h473.2x.jpg
   :scale: 25 %
   :alt: spongemock

How To Use
==========
spongemock [-h] [-c] [-b BIAS] [-s SEED | -S STRSEED] text [text ...]

positional arguments
--------------------
`text` - the text to mock. ThE tExT tO mOCk.

optional arguments
------------------
``-h``, ``--help`` - show this help message and exit

``-c``, ``--copy`` - Mocked text will be copied to the clipboard.
 
``-b BIAS``, ``--bias BIAS`` - This bias is used to succesively increase the chance of swapping from the previously-mocked case. A value of ``0`` will ensure the chance is always 50/50, and a value of ``1`` will ensure that after the first random choice the capitalization perfectly oscilates. Default is ``0.5``.

``-s SEED``, ``--seed SEED`` - Seed for random number generator. Can be any number or string (numbers are parsed).

``-S STRSEED``, ``--strseed STRSEED`` - Seed for random number generator. Does not attempt to parse the string to a number.