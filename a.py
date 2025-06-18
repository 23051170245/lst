import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split 
import pickle

#设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width' ,True)
#读取数据集，并将字符编码指定为gbk,防止中文报错
penguin_df=pd.read_csv('penguins-chinese.csv',encoding='gbk')
#删除缺失值所在的行 

penguin_df.dropna (inplace=True) 

#将企鹅的种类定义为目标输出变量 

output = penguin_df['企鹅的种类'] 

#将去除年份列不作为特征列 

#使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列 

features = penguin_df[['企鹅栖息的岛屿','喙的长度','喙的深度','翅膀的长度','身体质量','性别']] 

#对特征列进行独热编码 

features = pd.get_dummies (features)

#将目标输出变量转换为离散数值 

output_codes,output_uniques = pd.factorize(output) 

x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

rfc = RandomForestClassifier()

#使用训练集数据x_train和y_train来拟合（训练）模型 

rfc.fit(x_train, y_train) 

#用训练好的模型rfc对测试集数据x_test进行预测，将预测结果存储在y_pred中 


y_pred = rfc.predict (x_test) 

#计算测试集上模型的预测准确率 

#方法是使用accuracy_score 方法，比对真实标签y_test和预测标签y_pred 

#返回预测正确的样本占全部样本的比例,即准确率 

score = accuracy_score (y_test, y_pred) 
with open('rfc_model.pkl','wb') as f:
    pickle.dump(rfc,f)
with open('output_uniques.pkl','wb') as f:
    pickle.dump(output_uniques,f)
print('保存成功')
