## What is this repository for?

This repository contains calculations for the paper _A new concordance homomorphism from Khovanov homology_, namely the universal Khovanov homology and _S_-invariant (defined in the above-mentioned paper) of the _3n_-twisted positive Whitehead doubles of the _(2,2n+1)_-torus knots for 0 < n < 13.

### Detailed description of the calculations

The python-script `whitehead_torus.py` generates [PD Code](http://katlas.org/wiki/Planar_Diagrams) for twisted Whitehead doubles of torus knots. Internally, it uses [Morse Code](https://cbz20.raspberryip.com/code/khtpp/docs/Input.html) and the script `morse2pd.py` to convert Morse Code to PD Code (the latter script file was originally written for [a different project](https://github.com/LLewark/theta)). The resulting PD Codes are saved in the file `PD_Codes.txt`.

Then, using those PD codes, the program [khoca](https://github.com/LLewark/khoca) is used to calculate universal (a.k.a. equivariant) Khovanov homology of the Whitehead doubles.

Finally, the program [homca](https://github.com/diltgen/homca) is used to extract the _S_-invariant from the output of khoca. For this purpose, the output of khoca needs to be slightly reformatted. This reformatted output is contained in the file `_n_-formatted.txt` for 0 < n < 13.

The file `homca.ipynb` is a Jupyter Notebook file containing a slight modification of the homca sage code, as well as the calculations of the _S_-invariant of the Whitehead doubles.

The file `homca.html` contains a copy of the Jupyter Notebook, which can be directly viewed in the browser.
