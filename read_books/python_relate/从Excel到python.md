## 《从Excel到python》
> 20190205

在Python中pandas库用于数据处理，我们从1787页的pandas官网文档中总结出最常用的36个函数，通过这些函数介绍如何通过Python完成数据生成和导入、数据清洗、预处理，以及最常见的数据分类，数据筛选，分类汇总，透视等最常见的操作

#### 第1章 生成数据表
  1. 导入数据表
  2. 创建数据表

#### 第2章 数据表检查
  1. 数据维度(行列) df.shape
  2. 数据表信息 df.info()  数据维度、列名称、数据格式和所占空间等信息
  3. 查看数据格式 df.dtypes
  4. 查看空值 df.isnull()  #检查特定列空值 df['price'].isnull()
  5. 查看唯一值 #查看city列中的唯一值 df['city'].unique()
  6. 查看数据表数值 df.values
  7. 查看列名称 df.columns
  8. 查看前10行数据 df.head(3)  #查看最后3行 df.tail(3)

#### 第3章 数据表清洗
主要内容包括对空值、重复值、大小写问题、数据格式的处理。这里不包含对数据间的逻辑验证。
  1. 处理空值(删除或填充) df.dropna(how='any') df.fillna(value=0)
  2. 清理空格 #清除city字段中的字符空格 df['city']=df['city'].map(str.strip)
  3. 大小写转换 df['city']=df['city'].str.lower()
  4. 更改数据格式 df['price'].astype('int')
  5. 更改列名称 df.rename(columns={'category': 'category-size'})
  6. 删除重复值 默认情况下df.drop_duplicates()将删除后出现的重复值(与Excel逻辑一致)。
  增加keep='last'参数后将删除最先出现的重复值，保留最后的值
  7. 数值修改及替换 df['city'].replace('sh', 'shanghai')

#### 第4章 数据预处理
对清洗完的数据进行整理以便后期的统计和分析工作。主要包括数据表的合并，排序，数值分列，数
据分组及标记等工作。
  1. 数据表合并  pd.merge(df,df1,how='inner')  left，right和outer
  2. 设置索引列  df_inner.set_index('id')
  3. 排序(按索引，按数值) #按特定列的值排序 df_inner.sort_values(by=['age'])
      #按索引列排序 df_inner.sort_index()
  4. 数据分组
  ```python
  #如果price列的值>3000，group列显示high，否则显示low
df_inner['group'] = np.where(df_inner['price'] > 3000,'high','low')
#对复合多个条件的数据进行分组标记, sign列显示为1
df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price']>= 4000), 'sign']=1
  ```

  5. 数据分列

  ```python
  #对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列
名称为category和size
pd.DataFrame((x.split('-') for x in df_inner['category']),index=d
f_inner.index,columns=['category','size'])
  ```

#### 第5章 数据提取
  1. 按标签提取(loc) df_inner.loc[3] , df_inner.loc[0:5]
  #重设索引
df_inner.reset_index() df_inner=df_inner.set_index('date')
  2. 按位置提取(iloc)  df_inner.iloc[:3,:2]  
  #使用iloc按位置单独提取数据 df_inner.iloc[[0,2,5],[4,5]]
  3. 按标签和位置提取（ix）不推荐使用  df_inner.ix[:'2013-01-03',:4]
  4. 按条件提取（区域和条件值）
  #判断city列的值是否为beijing
  df_inner['city'].isin(['beijing'])

#### 第6章 数据筛选

使用与，或，非三个条件配合大于，小于和等于对数据进行筛选，并进行计数和求和。与Excel中的筛选功能和countifs和sumifs功能相似。

**按条件筛选（与、或、非)**
```python
#使用“与”条件进行筛选
df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beiji
ng'), ['id','city','age','category','gender']]
#使用“或”条件筛选
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beiji
ng'), ['id','city','age','category','gender']].sort(['age'])
#对筛选后的数据按price字段进行求和
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beiji
ng'), ['id','city','age','category','gender','price']].sort(['age
']).price.sum()
#使用“非”条件进行筛选
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age',
'category','gender']].sort(['id'])
#对筛选后的数据按city列进行计数
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age',
'category','gender']].sort(['id']).city.count()
#使用query函数进行筛选
df_inner.query('city == ["beijing", "shanghai"]')
#对筛选后的结果按price进行求和
df_inner.query('city == ["beijing", "shanghai"]').price.sum()
```


#### 第7章 数据汇总
Excel中使用分类汇总和数据透视可以按特定维度对数据进行汇总，Python中使用的主要函
数是groupby和pivot_table
1. 分类汇总

```python
#对所有列进行计数汇总
df_inner.groupby('city').count()
#对特定的ID列进行计数汇总
df_inner.groupby('city')['id'].count()
#对两个字段进行汇总计数
df_inner.groupby(['city','size'])['id'].count()
#对city字段进行汇总并计算price的合计和均值。
df_inner.groupby('city')['price'].agg([len,np.sum, np.mean])
```
2. 数据透视

```python
#数据透视表
pd.pivot_table(df_inner,index=["city"],values=["price"],columns=[
"size"],aggfunc=[len,np.sum],fill_value=0,margins=True)
```

#### 第8章 数据统计
1. 数据采样

```python
#简单的数据采样
df_inner.sample(n=3)
#手动设置采样权重
weights = [0, 0, 0, 0, 0.5, 0.5]
df_inner.sample(n=2, weights=weights)
#采样后不放回
df_inner.sample(n=6, replace=False)
```
2. 描述统计

```python
#数据表描述性统计
df_inner.describe().round(2).T
```
3. 标准差

```python
#标准差
df_inner['price'].std()
1523.3516556155596
```
4. 协方差

```python
#两个字段间的协方差
df_inner['price'].cov(df_inner['m-point'])
17263.200000000001
#数据表中所有字段间的协方差
df_inner.cov()
```
5. 相关分析

```python
#相关性分析
df_inner['price'].corr(df_inner['m-point'])
0.77466555617085264
#数据表相关性分析
df_inner.corr()
```

#### 第9章 数据输出
1. 写入Excel、csv

```python
#输出到Excel格式
df_inner.to_Excel('Excel_to_Python.xlsx', sheet_name='bluewhale_c
c')
#输出到CSV格式
df_inner.to_csv('Excel_to_Python.csv')
```
**to_csv 参数的一些细节**
```python
dt.to_csv(‘C:/Users/think/Desktop/Result.csv‘,sep=‘?‘)#使用?分隔需要保存的数据，如果不写，默认是,

dt.to_csv(‘C:/Users/think/Desktop/Result1.csv‘,na_rep=‘NA‘) #确实值保存为NA，如果不写，默认是空

dt.to_csv(‘C:/Users/think/Desktop/Result1.csv‘,float_format=‘%.2f‘) #保留两位小数

dt.to_csv(‘C:/Users/think/Desktop/Result.csv‘,columns=[‘name‘]) #保存索引列和name列

dt.to_csv(‘C:/Users/think/Desktop/Result.csv‘,header=0) #不保存列名

dt.to_csv(‘C:/Users/think/Desktop/Result1.csv‘,index=0) #不保存行索引

```


#### 案例
**990万次骑行：纽约自行车共享系统分析**
