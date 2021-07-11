# pytorch
+ nn
  + Conv2d
  + ConvTranspose2d
  + Dropout2d
  + 
+ optim
+ 

### `.float()`, `.int()`, `.double()`
To change the data type of a tensor `batch_data`, use `batch_data.float()`.

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
