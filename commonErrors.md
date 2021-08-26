# Common Errors
### OSError: [Errno 24] Too many open files
File "F:\software\miniconda3\lib\site-packages\PIL\Image.py", OSError: [Errno 24] Too many open files

```
# source code
for idx in data_indexs:
    path_to_image = os.path.join(project_path, module_name, "source", f"{idx}.png")
    self.imageNames.append(f"{idx}.png")
    self.images.append(Image.open(path_to_image))      

# solution
for idx in data_indexs:
    path_to_image = os.path.join(project_path, module_name, "source", f"{idx}.png")
    self.imageNames.append(f"{idx}.png")
    with Image.open(path_to_image) as img:
        self.images.append(img.copy())
```
