### intro
+ [tutorial from w3cschool](https://www.w3cschool.cn/sqlite/sqlite-python.html)
+ open a .db file and check what are really contained within it using [sqlitespy](https://github.com/suzyi/python/blob/master/sqlite3/sqlitespy.zip). Warning: this software was uploaded and stored here without permission.
### commonly-used operations
+ select
    + `cursor = connection.execute("SELECT id, info, name, selected, tag from Classify_1")`
    + `cursor = connection.execute("SELECT id from " + module_name + " WHERE selected=2")`
### read a .db file
```
import sqlite3 as sql

path_to_db = "F:/HereIsFileName.db"
connection = sql.connect(path_to_db)
img_names_train = []
# find in db
cursor = connection.execute("SELECT id from " + module_name + " WHERE selected=1")
for row in cursor:
    img_names_train.append(row[0])

img_names_test = []
cursor = connection.execute("SELECT id from " + module_name + " WHERE selected=2")
for row in cursor:
    img_names_test.append(row[0])

connection.close()
```

### insert a new line to a .db file
```
import sqlite3 as sql

# write .db file
connection = sql.connect("HereIsFileName.db")
cursor = connection.cursor()
Id =  13
Name = f"{ID}.png"
Info = {
    "img_channel" : 3,
    "img_height" : 64,
    "img_width" : 64,
    }
Selected = 0 # train:1 test:2 unlabel:0
Tag = ""
cursor.execute('INSERT INTO UnsuperSegment_1 values (?, ?, ?, ?, ?)', (Id, str(Info), Name, Selected, Tag))
connection.commit()
connection.close()
```
