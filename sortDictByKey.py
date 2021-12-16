import collections


if __name__=="__main__":
    scores = [0.34, 0.39, 0.35, 0.35, 0.42]
    names = ['731.png', '293.png', '119', '302.png', '672.png']
    assert len(scores)==len(names)
    
    score2name = {}
    for score, name in zip(scores, names):
        if score in score2name:
            score2name[score].append(name)
        else:
            score2name[score] = [name]
    score2name_ordered = collections.OrderedDict(sorted(score2name.items(), reverse=True))
    for k, v in score2name_ordered.items():
        print(k, v)