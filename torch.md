### .float(), .int()
To change the data type of a tensor `batch_data`, use `batch_data.float()`.

### torch.nn.ConvTranspose2d vs torch.nn.Upsample
The parameter of `torch.nn.ConvTranspose2d` is trainable, while `torch.nn.Upsample` is a simple interpolation which is not trainable.
