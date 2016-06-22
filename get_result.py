import sys
import pandas as pd
import numpy as np
from metrics_ranking import eval_multiple, eval_multiple_original, eval_apk

result_filename = sys.argv[1]
if len(sys.argv) == 3:
    topk = int(sys.argv[2])
else:
    topk = -1

result = pd.read_csv(result_filename, sep='\t', header=None, names=['uid', 'iid', 'truth', 'pred'])
result = pd.DataFrame(result, columns=['uid', 'truth', 'pred']).groupby('uid')
map_k, recall_k, precision_k = [], [], []
for each in result:
    true_scores, pred_scores = each[1]['truth'], each[1]['pred']
    ap, recall, precision = eval_multiple_original(true_scores, pred_scores, topk) \
        if topk == -1 else eval_multiple(true_scores, pred_scores, topk)
    map_k.append(ap)
    recall_k.append(recall)
    precision_k.append(precision)
print {'map@%d' % topk: np.mean(map_k),
        'recall@%d' % topk: np.mean(recall_k),
        'precision@%d' % topk: np.mean(precision_k)}
