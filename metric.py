#coding:utf-8
import collections

#gt[index] = id_gt
#pred[index] = id_pred


def b_cube_precision(gt,pred,ignore=-1):
	group = collections.defaultdict(list)
	for index,id_pred in enumerate(pred):
		group[id_pred].append(gt[index])
	edge_true,edge_all = 0,0
	for id_pred in group:
		num = len(group[id_pred])
		edge_all += num*(num-1)
		counter = collections.Counter()
		counter.update(group[id_pred])
		for id_gt,count in counter.most_common(2):
			if id_gt == ignore:
				continue
			else:
				edge_true += count*(count-1)
				break
	res = edge_true / edge_all
	return res

def b_cube_recall(gt,pred):
	group = collections.defaultdict(list)
	for index,id_gt in enumerate(gt):
		group[id_gt].append(pred[index])
	edge_exist,edge_all = 0,0
	for id_gt in group:
		num = len(group[id_gt])
		edge_all += num * (num-1)
		counter = collections.Counter()
		counter.update(group[id_gt])
		for id_pred in counter:
			count = counter[id_pred]
			edge_exist += count*(count-1)
	res = edge_exist / edge_all
	return res

if __name__ == '__main__':
	gt = [1]*10
	pred = [1]*6 + [2]*4
	print('precision: ',b_cube_precision(gt,pred))
	print('recall: ',b_cube_recall(gt,pred))

		

