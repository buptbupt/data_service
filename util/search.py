import jieba


def get_search_list(cut_list=[], not_cut_list=[]):
    '''
    使用三元分词方法拆分cut_list
    '''
    res = cut_list
    for text in cut_list:
        lcut = jieba.lcut(text)
        for p in range(len(lcut)):
            for n in range(3):
                res.append(''.join(lcut[p:p+n+1]))
    res.extend(not_cut_list)
    return list(set(res))
