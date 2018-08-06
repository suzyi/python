# python
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
### 2 - 2 - matplotlib
+ `from matplotlib import pyplot as plt` or `import matplotlib.pyplot as plt`
+ `plt.plot(X, Y, 'r+', markersize=1)` or `plt.plot(X, Y, 'r-', linewidth=1)`
### 2 - 3 - scipy
+ `import scipy.io as sio`
+ `sio.loadmat('./dataIris.mat')`
+ `sio.savemat('IrisData', {'trainingData': trainingData, 'testData': testData})`
