# pytorch
+ nn
  + Conv2d
  + ConvTranspose2d
  + Dropout2d
  + 
+ optim
+ 
### random distribution
+ `torch.rand(size=(1, 5))` Sampled uniformlly from the interval [0, 1).
### change data type
+ `.float()`, `.int()`, `.double()` Change the data type of a tensor `batch_data`, use `batch_data.float()`.
+ `.tolist()`. For example, `noise = torch.rand(size=(1, 5)).squeeze().tolist()`

### `torch.nn.ConvTranspose2d` vs `torch.nn.Upsample`
The parameter of `torch.nn.ConvTranspose2d` is trainable, while `torch.nn.Upsample` is a simple interpolation which is not trainable.

### `.view()` vs `.?`
`.as_contiguous`

## trouble shooting
### 1 - Expected more than 1 value per channel when training
[Solution from discuss.pytorch.org](https://discuss.pytorch.org/t/error-expected-more-than-1-value-per-channel-when-training/26274). The error is most likely thrown during training and if the current batch only contains a single sample. As you’ve explained this might happen, if the length of your Dataset is not dividable by the batch size without a remainder, which happens to be 1. You could set drop_last=True in your DataLoader and run your code again. Most likely you have a nn.BatchNorm layer somewhere in your model, which expects more then 1 value to calculate the running mean and std of the current batch. In case you want to validate your data, call model.eval() before feeding the data, as this will change the behavior of the BatchNorm layer to use the running estimates instead of calculating them for the current batch.
If you want to train your model and can’t use a bigger batch size, you could switch e.g. to InstanceNorm.
### 2 - CUDA error: device-side assert triggered
When this error message appears, just switch the device from "cuda" to "cpu", which will tells you more information. For example, it told me that "Target 13 is out of bounds" in my case.

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
## Initialization of A Neural Network
+ Improper initialization leads to a hard-to-converge model during training. In this situation, different initialization methods may work.
+ Difficult images, black-background images for example, may increase the difficulty of training.

In these cases, just print the weights and their gradients of each layer to theck,
```
print(f"iter: {iter}/{len(train_loader.dataset.imgs)/len(batch_data)}\t loss: {batch_loss.item():.5f}")
print(f"name\t data.mean()\t grad.mean()")
for name, param in model.named_parameters():
    print(f"{name}\t {param.data.mean():.6f}\t {param.grad.mean():.6f}")
```
### general initialization
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
### pretrained initialization
```
def _resnet(arch, block, layers, pretrained, progress, **kwargs):
    model = ResNet(block, layers, **kwargs)
    if pretrained:
        pretrained_state_dict = torch.load(cfg_share["path_to_pretrained_model"])
        state_dict = model.state_dict()
        for key in state_dict:
            if key in pretrained_state_dict:
                state_dict[key].copy_(pretrained_state_dict[key])
        model.load_state_dict(state_dict)
    return model
```