# torch
helpful features
+ [loss](loss.md)
+ [transform](transform.md)
### fetch images of a certain class
```
imgs = torch.randn((5, 3, 32, 32))
labels = [2, 2, 1, 0, 1]
labels = torch.tensor(labels)
print(imgs[labels==2])
```
### Initialization of A Neural Network
Sometimes, improper initialization leads to a hard-to-converge model during training. In this situation, different initialization methods may work.
```
model = Net().to(device)
model.apply(weights_init)

def weights_init(model):
    """Initialize the weights and biases of the given network.
    inputs:
        model (torch.nn.Module): A model to be initialized.
    """
    if isinstance(model, nn.Conv2d):
#         nn.init.kaiming_normal_(model.weight.data)
#         nn.init.kaiming_uniform_(model.weight.data)
#         nn.init.xavier_normal_(model.weight.data)
#         model.weight.data.fill_(-1)
        nn.init.normal_(model.weight.data, mean=0, std=.1)
    elif isinstance(model, nn.ConvTranspose2d):
#         nn.init.kaiming_normal_(model.weight.data)
#         nn.init.kaiming_uniform_(model.weight.data)
#         nn.init.xavier_normal_(model.weight.data)
        nn.init.normal_(model.weight.data, mean=0, std=.1)
```
