# python
+ nowcoder OJ input-output exercise: https://ac.nowcoder.com/acm/contest/320#question, [nowcoder-oj-exercise](https://github.com/suzyi/python/blob/master/nowcoder-oj-exercise.md)
## 1 - Basics
+ **`weight={'weight_1': [1, 1.5, 5.3]}` [(notebook)](https://github.com/suzyi/python/blob/master/notebook/weight%3D%7B.ipynb)**.
+ **solve ODEs**. See [web](http://old.sebug.net/paper/books/scipydoc/scipy_intro.html#id5) or [(notebook)](https://github.com/suzyi/python/blob/master/notebook/Lorenz.ipynb) for numerical solution to Lorenz system, using python. And [web](http://bzhang.lamost.org/website/archives/lorenz_attactor) for intro to Lorenz system. See [(notebook)](https://github.com/suzyi/python/blob/master/notebook/duffing.ipynb) for duffing oscillator.
### Buid-in Containers
+ list
  + `a = []`
  + `a.append(21)` or `a += [21]`
+ dict
  + Define a series/set of funtions that are similar in form such as "f0", "f1", "f2", ... , "f20", see [notebook](https://github.com/suzyi/python/blob/master/notebook/dict.ipynb)
  + `a = {}` or `a = dict()`
+ tuple
  + Commonly used as the parameters containers, e.g. `(batch, channel, width, height)` for a batch of images.
+ set
## 3 - modules
### 3 - 1 - numpy
+ `y = lambda x: np.sin(x)`
+ `np.arange(0, 2*np.pi, .1)`
+ Define piecewise function `np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])`. [Multiple pieces](https://stackoverflow.com/questions/19578185/multiple-pieces-in-a-numpy-piecewise)
a `from matplotlib import pyplot as plt` or `import matplotlib.pyplot as plt`
+ `plt.plot(X, Y, 'r+', markersize=1)` or `plt.plot(X, Y, 'r-', linewidth=1)`
### 3 - 3 - scipy
+ `import scipy.io as sio`
+ `sio.loadmat('./dataIris.mat')`
+ `sio.savemat('IrisData', {'trainingData': trainingData, 'testData': testData})`
### 4 - Advancement Programming
| Date(2019) | | notebook |
| --- | --- | --- |
| Apr 24 | parallel computing | [calculate-in-parallel.ipynb](https://github.com/suzyi/python/blob/master/notebook/calculate-in-parallel.ipynb),[train-models-in-parallel.ipynb](https://github.com/suzyi/python/blob/master/notebook/train-models-in-parallel.ipynb), [parallel-learning-notes.ipynb](https://github.com/suzyi/python/blob/master/notebook/parallel-learning-notes.ipynb) |
| Apr 24 | global variable | [global-variable.ipynb](https://github.com/suzyi/python/blob/master/notebook/global-variable.ipynb) |
