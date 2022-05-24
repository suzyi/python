# loss
### classification loss
```
import torch
import torch.nn.functional as F

if __name__=="__main__":
    target = torch.tensor([1, 0]) # for two examples
    logits = torch.tensor([[1.1, 2.3, 3, 4, 5], [1, 2, 3, 4, 5]], dtype=torch.float)
    
    print("-----F.nll_loss-----")
    result_nll_loss = F.nll_loss(F.log_softmax(logits, dim=1), target, reduction='none')
    print(result_nll_loss)
    
    print("-----F.cross_entropy-----")
    result_cross_entropy = F.cross_entropy(logits, target, reduction="none")
    print(result_cross_entropy)
    
    print("-----F.softmax->torch.log->negtive-----")
    for i, logit in enumerate(F.softmax(logits, dim=1)):
        print(-torch.log(logit[target[i].item()]))
```
This piece of code produces
```
-----F.nll_loss-----
tensor([3.1642, 4.4519])
-----F.cross_entropy-----
tensor([3.1642, 4.4519])
-----F.softmax->torch.log->negtive-----
tensor(3.1642)
tensor(4.4519)
```