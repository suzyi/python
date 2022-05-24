# transform
Using the code below, a gray-scaled image is transformed to a colorful image, which then can be feeded to a pretrained resnet18. This works for MNIST dataset.
```
import torchvision.transforms as transforms

transform = transforms.Compose([transforms.Resize(size=(cfg_share['img_height'], cfg_share['img_width'])),
                                transforms.ToTensor(),
                                transforms.Lambda(lambda x: x.repeat(3, 1, 1) ),
                               ])
```