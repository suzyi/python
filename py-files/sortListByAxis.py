if __name__=="__main__":
    scores = [0.34, 0.39, 0.35, 0.35, 0.42]
    names = ['731.png', '293.png', '119', '302.png', '672.png']
    assert len(scores)==len(names)
    
    score2name = []
    for name, score in zip(names, scores):
        score2name.append([name, score])
    print(score2name)
    score2name_ordered = sorted(score2name, key=lambda x: x[1], reverse=True)
    # in-place usage: score2name.sort(key=lambda x: x[1], reverse=True)
    print(score2name_ordered)
