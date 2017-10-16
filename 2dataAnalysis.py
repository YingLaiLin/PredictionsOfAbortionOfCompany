#! coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt

csv_suffix = '_with_result.csv'
csv_prefix = 'Data/'
train = pd.read_csv(csv_prefix + '2alter' + csv_suffix)
# print(train.describe())
fig = plt.figure()
fig.set_alpha(alpha=0.2)

# train.TARGET.value_counts().plot(kind='bar')

# plt.subplot2grid((2,2),(0,0))
# plt.scatter(train.RGYEAR,train.TARGET)
# plt.title(u'established year')
# plt.ylabel(u'aborted')
#
# plt.subplot2grid((2,2),(0,1))
# plt.scatter(train.HY,train.TARGET)
# plt.title(u'class')
# plt.ylabel(u'aborted')
#
# plt.subplot2grid((2,2),(1,0))
# plt.scatter(train.ZCZB,train.TARGET)
# plt.title(u'money')
# plt.ylabel(u'aborted')
#
# plt.subplot2grid((2,2),(1,1))
# plt.scatter(train.ETYPE,train.TARGET)
# 数据清洗
# df = train[(train.ALTERNO=="05") | (train.ALTERNO=='27')]
# df.to_csv(csv_prefix + '2alter' + csv_suffix,index=False)
plt.subplot2grid((2, 3), (0, 0), colspan=2)
aborted_0 = train.ALTDATE[train.TARGET == 0].value_counts()
aborted_1 = train.ALTDATE[train.TARGET == 1].value_counts()
df = pd.DataFrame({'aborted': aborted_1, 'success': aborted_0})
df.plot(kind='bar', stacked=True)
plt.title(u'enterprise_class')
plt.ylabel(u'aborted')

plt.subplot2grid((2, 3), (1, 0))
aborted_0 = train.ALTERNO[train.TARGET == 0].value_counts()
aborted_1 = train.ALTERNO[train.TARGET == 1].value_counts()
df = pd.DataFrame({'aborted': aborted_1, 'success': aborted_0})
df.plot(kind='bar', stacked=True)
plt.title(u'Alter no')
plt.ylabel(u'aborted')
plt.show()
