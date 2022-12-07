from sklearn.model_selection import KFold

# 数据总数量和要分出来的测试集的数量
# kf = KFold(15, 3)
kf = KFold(5, random_state=1, shuffle=True)
print(kf)
# for train_index, test_index in kf:
#     print(train_index, test_index)
