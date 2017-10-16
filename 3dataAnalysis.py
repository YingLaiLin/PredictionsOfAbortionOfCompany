#! coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
csv_suffix = '_with_result.csv'
csv_prefix = 'Data/'
train = pd.read_csv(csv_prefix + '3branch' + csv_suffix)
# print(train.describe())
fig = plt.figure()
fig.set_alpha(alpha=0.2)

#train.TARGET.value_counts().plot(kind='bar')

plt.subplot2grid((2,1),(0,0))
plt.scatter(train.B_REYEAR,train.TARGET)
plt.title(u'established year')
plt.ylabel(u'aborted')
#
plt.subplot2grid((2,1),(1,0))
plt.scatter(train.B_ENDYEAR,train.TARGET)
plt.title(u'end year')
plt.ylabel(u'aborted')
#
# plt.subplot2grid((2,2),(1,0))
# plt.scatter(train.ZCZB,train.TARGET)
# plt.title(u'money')
# plt.ylabel(u'aborted')
#
# plt.subplot2grid((2,2),(1,1))
# plt.scatter(train.ETYPE,train.TARGET)

# aborted_0 = train.IFHOME[train.TARGET==0].value_counts()
# aborted_1 = train.IFHOME[train.TARGET==1].value_counts()
# df = pd.DataFrame({'aborted':aborted_1, 'success':aborted_0})
# df.plot(kind='bar',stacked=True)
# plt.title(u'enterprise_class')
# plt.ylabel(u'aborted')

plt.show()

