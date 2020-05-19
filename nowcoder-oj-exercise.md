+ `sys.stdin`读取所有的内容，并转化为字符串。
+ `line = sys.stdin.readline().strip().split()`读取一行数据，`.split()`表示用默认空格分开，`.split(',')`表示逗号分开。
### 读取所有的行数`sys.stdin`
```
import sys
for line in sys.stdin:
    temp = line.split()
    print(int(temp[0])+int(temp[1]))
```
例如：
```
输入：
1 5
10 20
输出：
6
30
```
### 逐行读取
```
import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    line = sys.stdin.readline().strip().split()
    print(int(line[0])+int(line[1]))
```
