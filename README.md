# python
## 1 - Intro to python
python is a kernel. There are three kinds of user interfaces, inluding [spyder](https://pypi.org/project/spyder/), [jupyter](http://jupyter.org/) and [pycharm](https://www.jetbrains.com/pycharm/).
### 1 - 1 - spyder
### 1 - 2 - Jupyter
+ customize a shortcut for "restart & run all", "help -> Edit keyboards shortcuts".
+ Convert a .ipynb file to .py file in command line (terminal) `ipython nbconvert --to python YourNotebook.ipynb`
### 1 - 3 - pycharm
+ **zip [(notebook)](https://github.com/suzyi/python/blob/master/notebook/zip.ipynb)**.
## class
## `from __future__ import print_function`
The `__future__` module is used for testing future version of some changes in current python environment.
If you include this command in your program, you'd better use `print(something)` instead of `print something`, since it may return an error `invalid syntax`.
+ **`weight={'weight_1': [1, 1.5, 5.3]}` [(notebook)](https://github.com/suzyi/python/blob/master/notebook/weight%3D%7B.ipynb)**.
+ **solve ODEs**. See [web](http://old.sebug.net/paper/books/scipydoc/scipy_intro.html#id5) or [(notebook)](https://github.com/suzyi/python/blob/master/notebook/Lorenz.ipynb) for numerical solution to Lorenz system, using python. And [web](http://bzhang.lamost.org/website/archives/lorenz_attactor) for intro to Lorenz system. See [(notebook)](https://github.com/suzyi/python/blob/master/notebook/duffing.ipynb) for duffing oscillator.
## 2 - modules
### 2 - 1 - numpy
+ `y = lambda x: np.sin(x)`
+ `np.arange(0, 2*np.pi, .1)`
+ Define piecewise function `np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])`. [Multiple pieces](https://stackoverflow.com/questions/19578185/multiple-pieces-in-a-numpy-piecewise)
+ To generate random number, see [notebook](https://github.com/suzyi/python/blob/master/notebook/python/randn_rand.ipynb) for the usage of `numpy.random.rand()`, `numpy.random.randn()`.
### 2 - 2 - matplotlib
+ `from matplotlib import pyplot as plt` or `import matplotlib.pyplot as plt`
+ `plt.plot(X, Y, 'r+', markersize=1)` or `plt.plot(X, Y, 'r-', linewidth=1)`
### 2 - 3 - scipy
+ `import scipy.io as sio`
+ `sio.loadmat('./dataIris.mat')`
+ `sio.savemat('IrisData', {'trainingData': trainingData, 'testData': testData})`
