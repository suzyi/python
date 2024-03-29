# python
+ nowcoder OJ input-output exercise: https://ac.nowcoder.com/acm/contest/320#question, [nowcoder-oj-exercise](https://github.com/suzyi/python/blob/master/nowcoder-oj-exercise.md)
## 1 - Basics
+ **`weight={'weight_1': [1, 1.5, 5.3]}` [(notebook)](https://github.com/suzyi/python/blob/master/notebook/weight%3D%7B.ipynb)**.
+ **solve ODEs**. See [web](http://old.sebug.net/paper/books/scipydoc/scipy_intro.html#id5) or [(notebook)](https://github.com/suzyi/python/blob/master/notebook/Lorenz.ipynb) for numerical solution to Lorenz system, using python. And [web](http://bzhang.lamost.org/website/archives/lorenz_attactor) for intro to Lorenz system. See [(notebook)](https://github.com/suzyi/python/blob/master/notebook/duffing.ipynb) for duffing oscillator.
### Buid-in Containers
+ list
  + `a = []`
  + `a.append(21)` or `a += [21]`
  + `idx = length_vec.index(max(length_vec))`
  + `contours = [[[1, 1], [3, 3], [1, 3], [3, 1]], [[1, 1], [1, 2], [1, 3], [2, 3], [3, 3], [3, 2]]], contour_largest = max(contours, key=len)`. This one is quite useful when multiple objects are detected but you just need the largest one.
  + [sort a list by its axis](https://github.com/suzyi/python/blob/master/py-files/sortListByAxis.py)
+ dict - A mapping from name to value.
  + Define a series/set of funtions that are similar in form such as "f0", "f1", "f2", ... , "f20", see [notebook](https://github.com/suzyi/python/blob/master/notebook/dict.ipynb)
  + `a = {}` or `a = dict()`
  + `a['name'] = "Tom"` and `a['age'] = 10`
  + `a.keys()` gives `dict_keys(['age', 'name'])`.
  + `a.items()` gives `dict_items([('age', 10), ('name', 'Tom')])`.
  + `**kwargs` is esentially a dict.
  + [sort a dict by its key](https://github.com/suzyi/python/blob/master/py-files/sortDictByKey.py)
  + Given `x = "{'a' : 1, 'b' : True, 'c' : 'C'}"`, which is a string and can't be easily modified, then `y = eval(x)` returns you a real dict.
  + `scores = {"math": 87, "eng": 89, "phy": 88}`, then `del scores["eng"]`. Scenario: `state_dict = torch.load("resnet18-f37072fd.pth")`, `del state_dict["fc.weight"]`, `del state_dict["fc.bias"]`
+ set
  + `a = set()` or `a = {"English", "Math", "Chemistry"}`.
  + `a = a|{"English"}|{"Math"}|{English}` or `a.union{b}` returns a new set, i.e., doesn't change neither `a` or `b`.
  + The common elements of two sets. `a = {"English", "Math"}`, `b = {"English", "Chemistry"}`, `commonalities = a - (a - b)`. Or in a more powerful way, `u = set.intersection(set1, set2, set3)`.
  + All unique elements: `allUniqueElements = set.union(set1, set2, set3)`
+ string
  + `"F:\\data\\train".replace("\\","/")` gives "F:/data/train".
  + `"F:/data/train".split("/")[1]` gives "data".
+ tuple
  + Commonly used as the parameters containers, e.g. `(batch, channel, width, height)` for a batch of images.
  + `*args` is essentially a tuple.
  + `kernel_size = (1, 2, 3), kernel_size += (4, 5)` gives `kernel_size = (1, 2, 3, 4, 5)`
### build-in functions
+ `assert len(img_names)!=0, "Empty img_names does not meet requirement!"`
+ raise
  + `raise TypeError(f"List required, but {type(img_names)} found!")`
  + `raise ValueError(f"True or False required, but {img_name} found!")`
### format
+ `print(f"{3.1415:.2f}")` gives "3.14".
+ `print("Only %.2f seconds left" % (3-1.3))` gives "Only 1.70 seconds left".
+ `print("%s/images/%s.jpg" % (2007, "cat"))` gives "2007/images/cat.jpg".
### Class
A class is a collection of attributes and functions. Take the `class People` below as example, the attributes are name, age and sex and the functions are get_People_info.
```
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get_People_info(self):
        return self.name, self.age, self.sex

people_1 = People("Jorge", 18, "male")
print(people_1.name)
print(people_1.get_People_info())
```
继承自己定义的类
```
class Student(People): # 继承
    def __init__(self, name, age, sex, university):
        super(Student, self).__init__(name, age, sex)
        self.university = university

    def get_Student_info(self):
        return self.get_People_info(), self.university

student_1 = Student("Jorge", 18, "male", "Harvard")
print(student_1.name)
print(student_1.get_People_info())
print(student_1.get_Student_info())
```
or 
```
class Student(People): # 继承
    def __init__(self, name, age, sex):
        super(Student, self).__init__(name, age, sex)
        self.university = None

    def get_Student_info(self):
        return self.get_People_info(), self.university

student_1 = Student("Jorge", 18, "male")
print(student_1.name)
print(student_1.get_People_info())
print(student_1.get_Student_info())
```
继承python内置object
```
class Student(object):
```
则Student创建的对象`student_1 = Student()`会具有以下属性
+ self.__dict__.update(state) # where state is of type defaultdict.
+ self.__class__.__name__ # This is a string.

### 装饰器@
### 3 - Common Packages
+ machine learning
  + [numpy](numpy/readme.md)
+ deep learning
  + [torch](pytorch)
  + [opencv, cv2](cv2)
+ file processing
  + [txt](txt/readme.md)
  + [json](json/readme.md)
  + [database.db](sqlite3/readme.md)
  + matlab.mat
    + `import scipy.io as sio`
    + `sio.loadmat('./dataIris.mat')`
    + `sio.savemat('IrisData', {'trainingData': trainingData, 'testData': testData})`
### 4 - Advancement Programming
| Date(2019) | | notebook |
| --- | --- | --- |
| Apr 24 | parallel computing | [calculate-in-parallel.ipynb](https://github.com/suzyi/python/blob/master/notebook/calculate-in-parallel.ipynb),[train-models-in-parallel.ipynb](https://github.com/suzyi/python/blob/master/notebook/train-models-in-parallel.ipynb), [parallel-learning-notes.ipynb](https://github.com/suzyi/python/blob/master/notebook/parallel-learning-notes.ipynb) |
| Apr 24 | global variable | [global-variable.ipynb](https://github.com/suzyi/python/blob/master/notebook/global-variable.ipynb) |
