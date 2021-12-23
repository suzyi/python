### read from a json file
```
import json

if __name__=="__main__":
    with open("task.json", 'r', encoding='UTF-8') as file:
        content = json.load(file)
        print(content)
```
where 
+ `encoding='UTF-8'` enables opening a file with utf-8.
+ By default, it opens a file with GBK.

### modify an existing json file
```
import json

if __name__=="__main__":
    with open("task.json", 'r+', encoding='UTF-8') as file:
        content = json.load(file)
        content["blur_idxs"]["annotate"] = "1~6"
        file.seek(0)        # <--- should reset file position to the beginning.
        json.dump(content, file, indent=4, ensure_ascii=False)
        file.truncate()     # remove remaining part
```
