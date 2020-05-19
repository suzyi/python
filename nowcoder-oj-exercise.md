读取所有的行数`sys.stdin`
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
