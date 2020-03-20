import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import metrics

ri = Ridge(normalize=True)
el = ElasticNet(max_iter=2000, random_state=0)
x = pd.read_csv('train.csv')
newdata = pd.read_csv('test.csv')
'''
unidict = {}
for l in range(len(uni)):
    unidict[uni[l]] = l
for l in range(len(x)):
    x.loc[l,"Neighborhood"] = unidict[x.loc[l,"Neighborhood"]]
print(x["Neighborhood"])
# xt = lt.groupby('Neighborhood')
# arr = pd.DataFrame({"Mean":np.array(xt.mean()).reshape(-1),"Count":np.array(xt.count()).reshape(-1)},index=range(len(xt.mean())))
# print(arr)
#print(arr)
# key = xt.groups.keys()
#plt.bar(key,arr,width=.3)
#plt.show()

lt = x.loc[:,('SalePrice','MSZoning')]
xt = lt.groupby('MSZoning')
arr = np.array(xt.mean())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr)
#plt.show()

for k in range(len(x)):
    if(x.loc[k,"MSZoning"] == 'A'):
        x.loc[k, "MSZoning"] = 0
    elif(x.loc[k,"MSZoning"] == 'C (all)'):
        x.loc[k, "MSZoning"] = 1
    elif(x.loc[k,"MSZoning"]=='RP'):
        x.loc[k, "MSZoning"] = 2
    elif x.loc[k,"MSZoning"]=='RH' or x.loc[k,"MSZoning"] == 'RM':
        x.loc[k, "MSZoning"] = 3
    elif(x.loc[k,"MSZoning"]=='I'):
        x.loc[k, "MSZoning"] = 4
    elif(x.loc[k,"MSZoning"]=='RL'):
        x.loc[k, "MSZoning"] = 5
    elif(x.loc[k,"MSZoning"] == 'FV'):
        x.loc[k, "MSZoning"] = 6

#print(x["MSZoning"])
lt = x.loc[:,('SalePrice','SaleCondition')]
xt = lt.groupby('SaleCondition')
arr = np.array(xt.mean())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr,width=.5)
#plt.show()

for l in range(len(x)):
    if x.loc[l,"SaleCondition"] == 'AdjLand':
        x.loc[l,"SaleCondition"] = 0
    elif x.loc[l,"SaleCondition"] == 'Abnorml' or x.loc[l,"SaleCondition"] == 'Family':
        x.loc[l,"SaleCondition"] = 1
    elif x.loc[l,"SaleCondition"] == 'Alloca':
        x.loc[l,"SaleCondition"] = 2
    elif  x.loc[l,"SaleCondition"] == 'Normal':
        x.loc[l,"SaleCondition"] = 3
    else:
         x.loc[l,"SaleCondition"] = 4

lt = x.loc[:,('SalePrice','Street')]
xt = lt.groupby('Street')
arr = np.array(xt.mean())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr,width=.3)
#plt.show()

for l in range(len(x)):
    if x.loc[l,"Street"] == 'Grvl':
        x.loc[l,"Street"] = 0
    elif x.loc[l,"Street"] == 'Pave':
        x.loc[l,"Street"] = 1

lt = x.loc[:,('SalePrice','LotShape')]
xt = lt.groupby('LotShape')
arr = np.array(xt.median())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr,width=.3)
#plt.show()

for l in range(len(x)):
    if x.loc[l,"LotShape"] == 'Reg':
        x.loc[l,"LotShape"] = 1
    elif x.loc[l,"LotShape"] == 'IR1' or x.loc[l,"LotShape"] == 'IR3':
        x.loc[l,"LotShape"] = 2
    elif x.loc[l,"LotShape"] == 'IR2':
        x.loc[l,"LotShape"] = 3
#print(x["LotShape"])
lt = x.loc[:,('SalePrice','Utilities')]
xt = lt.groupby('Utilities')
arr = np.array(xt.median())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr,width=.3)
#plt.show()

for l in range(len(x)):
    if x.loc[l,"Utilities"] == 'NoSewr':
        x.loc[l,"Utilities"] = 0
    elif x.loc[l,"Utilities"] == 'NoSeWa':
        x.loc[l,"Utilities"] = 1
    elif x.loc[l,"Utilities"] == 'AllPub':
        x.loc[l,"Utilities"] = 2

lt = x.loc[:,('SalePrice','HouseStyle')]
xt = lt.groupby('HouseStyle')
arr = np.array(xt.median())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr,width=.3)
#plt.show()

for l in range(len(x)):
    if x.loc[l,"HouseStyle"] == '1.5Unf':
        x.loc[l,"HouseStyle"] = 0
    elif x.loc[l,"HouseStyle"] == '1.5Fin' or x.loc[l,"HouseStyle"] == '2.5Unf' or x.loc[l,"HouseStyle"] == 'SFoyer':
        x.loc[l,"HouseStyle"] = 1
    elif x.loc[l,"HouseStyle"] == '1Story' or x.loc[l,"HouseStyle"] == 'SLvl':
        x.loc[l,"HouseStyle"] = 2
    else:
        x.loc[l,"HouseStyle"] = 3

lt = x.loc[:,('SalePrice','OverallQual')]
xt = lt.groupby('OverallQual')
arr = np.array(xt.median())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr)
#plt.show()

lt = x.loc[:,('SalePrice','OverallCond')]
xt = lt.groupby('OverallCond')
arr = np.array(xt.mean())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr)
#plt.show()

#print(x.loc[:,("SalePrice","YearBuilt","YearRemodAdd")])

#plt.scatter(x["YearRemodAdd"],x["SalePrice"])
#plt.show()
# 
for l in range(len(x)):
    if 1950 <= x.loc[l,"YearRemodAdd"] < 1960:
        x.loc[l,"YearRemodAdd"] = 0
    elif 1960 <= x.loc[l,"YearRemodAdd"] < 1970:
        x.loc[l,"YearRemodAdd"] = 1
    elif 1970 <= x.loc[l, "YearRemodAdd"] <= 1980:
        x.loc[l,"YearRemodAdd"] = 1
    elif 1980 <= x.loc[l,"YearRemodAdd"] < 1990:
        x.loc[l,"YearRemodAdd"] = 2
    elif 1990 <= x.loc[l, "YearRemodAdd"] < 2000:
        x.loc[l,"YearRemodAdd"] = 3
    else:
        x.loc[l,"YearRemodAdd"] = 3

for l in range(len(x)):
    if 1950 <= x.loc[l,"YearRemodAdd"] < 1970:
        x.loc[l,"YearRemodAdd"] = 0
    elif 1970 <= x.loc[l,"YearRemodAdd"] < 1990:
        x.loc[l,"YearRemodAdd"] = 1
    else:
        x.loc[l,"YearRemodAdd"] = 2


for l in range(len(x)):
    if 1950 <= x.loc[l,"YearRemodAdd"] < 1980:
        x.loc[l,"YearRemodAdd"] = 0
    elif 1980 <= x.loc[l,"YearRemodAdd"] < 2000:
        x.loc[l,"YearRemodAdd"] = 1
    elif 2000 <= x.loc[l, "YearRemodAdd"] < 2005:
        x.loc[l, "YearRemodAdd"] = 2
    elif 2005 <= x.loc[l, "YearRemodAdd"] <= 2010:
        x.loc[l,"YearRemodAdd"] = 3
    else:
        x.loc[l,"YearRemodAdd"] = 4

lt = x.loc[:,('SalePrice','YearRemodAdd')]
xt = lt.groupby('YearRemodAdd')
arr = np.array(xt.median())
arr = arr.reshape(-1)
# print(arr)
key = xt.groups.keys()
# plt.bar(key,arr,width=.3)
# plt.show()

lt = x.loc[:,('SalePrice','ExterQual')]
xt = lt.groupby('ExterQual')
arr = np.array(xt.median())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
# plt.bar(key,arr,width=.3)
# plt.show()
for l in range(len(x)):
    if x.loc[l,"ExterQual"] == 'Po':
        x.loc[l,"ExterQual"] = 0
    elif x.loc[l,"ExterQual"] < "Fa":
        x.loc[l,"ExterQual"] = 1
    elif x.loc[l, "ExterQual"] < "TA":
        x.loc[l, "ExterQual"] = 2
    elif x.loc[l, "ExterQual"] <= "Gd":
        x.loc[l,"ExterQual"] = 3
    else:
        x.loc[l,"ExterQual"] = 4
lt = x.loc[:,('SalePrice','FireplaceQu')]
xt = lt.groupby('FireplaceQu')
arr = np.array(xt.mean())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr,width=.3)
#plt.show()
lt = x.loc[:,('SalePrice','PoolQC')]
xt = lt.groupby('PoolQC')
arr = np.array(xt.mean())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
#plt.bar(key,arr,width=.3)
#plt.show()

for l in range(len(x)):
    if x.loc[l,"MiscFeature"] == "TenC":
        x.loc[l,"MiscFeature"] = 3
    elif x.loc[l,"MiscFeature"] == "Gar2" or x.loc[l,"MiscFeature"] == "Shed":
        x.loc[l, "MiscFeature"] = 2
    elif x.loc[l,"MiscFeature"] == "Othr":
        x.loc[l, "MiscFeature"] = 1
    else:
        x.loc[l, "MiscFeature"] = 0
lt = x.loc[:,('SalePrice','Foundation')]
xt = lt.groupby('Foundation')
arr = np.array(xt.mean())
arr = arr.reshape(-1)
#print(arr)
key = xt.groups.keys()
# plt.bar(key,arr,width=.3)
# plt.show()

for l in range(len(x)):
    if x.loc[l,"PoolQC"] == "Ex":
        x.loc[l,"PoolQC"] = 2
    elif x.loc[l,"PoolQC"] == "Fa" or x.loc[l,"PoolQC"] == "Gd":
        x.loc[l,"PoolQC"] = 1
    else:
        x.loc[l,"PoolQC"] = 0

#print(min(x["YearRemodAdd"]))
#print(max(x["YearRemodAdd"]))
for l in range(len(x)):
    if x.loc[l,"FireplaceQu"] == "Ex":
        x.loc[l,"FireplaceQu"] = 3
    elif x.loc[l,"FireplaceQu"] == "TA" or x.loc[l,"FireplaceQu"] == "Gd":
        x.loc[l,"FireplaceQu"] = 2
    elif x.loc[l,"FireplaceQu"] == "Fa":
        x.loc[l, "FireplaceQu"] = 1
    else:
        x.loc[l,"FireplaceQu"] = 0

for l in range(len(x)):
    if x.loc[l,"OverallCond"] == 1:
        x.loc[l,"OverallCond"] = 0
    elif x.loc[l,"OverallCond"] == 3:
        x.loc[l,"OverallCond"] = 1
    elif x.loc[l,"OverallCond"] == 4:
        x.loc[l,"OverallCond"] = 2
    elif x.loc[l,"OverallCond"] == 2 or x.loc[l,"OverallCond"] == 6 or x.loc[l,"OverallCond"] == 7 or x.loc[l,"OverallCond"] == 8:
        x.loc[l,"OverallCond"] = 3
    else:
        x.loc[l,"OverallCond"] = 4

for l in range(len(x)):
    if x.loc[l,"Foundation"] == "Slab":
        x.loc[l,"Foundation"] = 0
    elif x.loc[l,"Foundation"] == "BrkTil":
        x.loc[l, "Foundation"] = 1
    elif x.loc[l,"Foundation"] == "CBlock" or x.loc[l,"Foundation"] == "Stone":
        x.loc[l, "Foundation"] = 2
    elif x.loc[l,"Foundation"] == "Wood":
        x.loc[l, "Foundation"] = 3
    else:
        x.loc[l, "Foundation"] = 4
for l in range(len(q)):
    if q.loc[l, "CentralAir"] == 'N': q.loc[l,"CentralAir"] = 0
    else: q.loc[l, "CentralAir"] = 1
'''


wholesum = pd.concat((x,newdata)).reset_index(drop=True)
miss = (wholesum.isnull().sum()/len(wholesum))*100
miss = miss.drop(miss[miss==0].index).sort_values(ascending = False)
print(miss)
'''
for column_name in ('PoolQC','MiscFeature','Alley','Fence','FireplaceQu','GarageType', 'GarageFinish', 'GarageQual', 'GarageCond','BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2','MasVnrType','MSSubClass'):
  x[column_name].fillna('None',inplace=True)
  newdata[column_name].fillna(' ',inplace=True)
for column_name in ('GarageYrBlt', 'GarageArea','Electrical','KitchenQual', 'GarageCars','BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF','TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath','MasVnrArea'):
  newdata[column_name].fillna(0,inplace=True)
  x[column_name].fillna(0,inplace=True)
for column_name in ('MSZoning','SaleType','Exterior1st','Exterior2nd'):
  x[column_name].fillna(x[column_name].mode()[0],inplace=True)
  newdata[column_name].fillna(newdata[column_name].mode()[0],inplace=True)
'''
for column_name in x.columns:
    if x[column_name].dtype == object:
        x[column_name].fillna(0, inplace=True)
    else:
        x[column_name].fillna(x[column_name].mean(), inplace=True)
for column_name in newdata.columns:
    if newdata[column_name].dtype == object:
        newdata[column_name].fillna(0, inplace=True)
    else:
        newdata[column_name].fillna(x[column_name].mean(), inplace=True)
# x["Utilities"] = x["Utilities"].dropna(inplace=True)
x["Functional"] = x["Functional"].fillna('Typical')
newdata["Functional"] = newdata["Functional"].fillna('Typical')
x["LotFrontage"].fillna(x["LotFrontage"].mean(), inplace=True)
newdata["LotFrontage"].fillna(newdata["LotFrontage"].mean(), inplace=True)
wholesum = pd.concat((x, newdata)).reset_index(drop=True)
miss = (wholesum.isnull().sum() / len(wholesum)) * 100
miss = miss.drop(miss[miss == 0].index).sort_values(ascending=False)
print(miss)

for l in range(len(x)):
    if x.loc[l, "KitchenQual"] == "Ex":
        x.loc[l, "KitchenQual"] = 4
    elif x.loc[l, "KitchenQual"] == "Gd":
        x.loc[l, "KitchenQual"] = 3
    elif x.loc[l, "KitchenQual"] == "TA":
        x.loc[l, "KitchenQual"] = 2
    elif x.loc[l, "KitchenQual"] == "Fa":
        x.loc[l, "KitchenQual"] = 1
    else:
        x.loc[l, "KitchenQual"] = 0
# print(newdata)
print(x.columns)


# print(x)
def band_create(dataset, column_name):
    uni = []
    groups = dataset.groupby(column_name)
    for unique_column in groups.groups:
        uni.append(unique_column)
    unidict = {}
    for l in range(len(uni)):
        unidict[uni[l]] = l
    for l in range(len(dataset)):
        dataset.loc[l, column_name] = unidict[dataset.loc[l, column_name]]


# x = x.drop(x[(x['GrLivArea']>4000) & (x['SalePrice']<300000)].index)

def replace(q):
    band_create(q, "PoolQC")
    band_create(q, "Fence")
    band_create(q, "Alley")
    band_create(q, "Electrical")
    band_create(q, "Heating")
    band_create(q, "HeatingQC")
    band_create(q, "GarageType")
    band_create(q, "BsmtExposure")
    band_create(q, "BsmtQual")
    band_create(q, "RoofStyle")
    band_create(q, "BsmtFinType1")
    band_create(q, "BsmtFinType2")
    band_create(q, "Functional")
    band_create(q, "FireplaceQu")
    band_create(q, "RoofMatl")
    band_create(q, "GarageCond")
    band_create(q, "MiscFeature")
    band_create(q, "GarageQual")
    band_create(q, "GarageType")
    band_create(q, "MasVnrType")
    band_create(q, "ExterCond")
    band_create(q, "CentralAir")
    band_create(q, "PavedDrive")
    band_create(q, "BsmtFinType1")
    band_create(q, "BsmtCond")
    band_create(q, "BsmtQual")
    band_create(q, "RoofStyle")
    band_create(q, "SaleType")
    band_create(q, "LotConfig")
    band_create(q, "Exterior1st")
    band_create(q, "Exterior2nd")
    band_create(q, "Condition2")
    band_create(q, "HouseStyle")
    band_create(q, "MSZoning")
    band_create(q, "SaleType")
    band_create(q, "MSSubClass")
    band_create(q, "SaleCondition")
    band_create(q, "LotConfig")
    band_create(q, "Condition1")
    band_create(q, "BldgType")
    band_create(q, "RoofStyle")
    band_create(q, "LandContour")
    band_create(q, "ExterQual")
    uni = np.unique(q["Neighborhood"])
    unidict = {}
    for l in range(len(uni)):
        unidict[uni[l]] = l
    for l in range(len(q)):
        q.loc[l, "Neighborhood"] = unidict[q.loc[l, "Neighborhood"]]
    for l in range(len(q)):
        if q.loc[l, "LandSlope"] == 'Gtl':
            q.loc[l, "LandSlope"] = 0
        elif q.loc[l, "LandSlope"] == 'Mod':
            q.loc[l, "LandSlope"] = 1
        else:
            q.loc[l, "LandSlope"] = 2
    for l in range(len(q)):
        if q.loc[l, "Condition2"] == 'Artery' or q.loc[l, "Condition2"] == 'RRNn':
            q.loc[l, "Condition2"] = 0
        elif q.loc[l, "Condition2"] == 'Feedr':
            q.loc[l, "Condition2"] = 1
        elif q.loc[l, "Condition2"] == 'RRAn':
            q.loc[l, "Condition2"] = 2
        elif q.loc[l, "Condition2"] == 'Norm':
            q.loc[l, "Condition2"] = 3
        elif q.loc[l, "Condition2"] == 'RRAe':
            q.loc[l, "Condition2"] = 4
        elif q.loc[l, "Condition2"] == 'PosN':
            q.loc[l, "Condition2"] = 5
        else:
            q.loc[l, "Condition2"] = 6
    for l in range(len(q)):
        if q.loc[l, "CentralAir"] == 'N':
            q.loc[l, "CentralAir"] = 0
        else:
            q.loc[l, "CentralAir"] = 1
    q["YearBuilt"] = (q["YearBuilt"] + q["YearRemodAdd"]) / 2
    for l in range(len(q)):
        if 1950 <= q.loc[l, "YearRemodAdd"] < 1980:
            q.loc[l, "YearRemodAdd"] = 0
        elif 1980 <= x.loc[l, "YearRemodAdd"] < 2000:
            q.loc[l, "YearRemodAdd"] = 1
        elif 2000 <= q.loc[l, "YearRemodAdd"] < 2005:
            q.loc[l, "YearRemodAdd"] = 2
        elif 2005 <= q.loc[l, "YearRemodAdd"] <= 2010:
            q.loc[l, "YearRemodAdd"] = 3
        else:
            q.loc[l, "YearRemodAdd"] = 4
    q["YrSold"] = q["YrSold"] + (q["MoSold"] / 12)
    for l in range(len(q)):
        if q.loc[l, "Foundation"] == "Slab":
            q.loc[l, "Foundation"] = 0
        elif q.loc[l, "Foundation"] == "BrkTil":
            q.loc[l, "Foundation"] = 1
        elif q.loc[l, "Foundation"] == "CBlock" or x.loc[l, "Foundation"] == "Stone":
            q.loc[l, "Foundation"] = 2
        elif q.loc[l, "Foundation"] == "Wood":
            q.loc[l, "Foundation"] = 3
        else:
            q.loc[l, "Foundation"] = 4
    for l in range(len(q)):
        if q.loc[l, "KitchenQual"] == "Ex":
            q.loc[l, "KitchenQual"] = 4
        elif q.loc[l, "KitchenQual"] == "Gd":
            q.loc[l, "KitchenQual"] = 3
        elif q.loc[l, "KitchenQual"] == "TA":
            q.loc[l, "KitchenQual"] = 2
        elif q.loc[l, "KitchenQual"] == "Fa":
            q.loc[l, "KitchenQual"] = 1
        else:
            q.loc[l, "KitchenQual"] = 0
    for k in range(len(q)):
        if (q.loc[k, "MSZoning"] == 'A'):
            q.loc[k, "MSZoning"] = 0
        elif (q.loc[k, "MSZoning"] == 'C (all)'):
            q.loc[k, "MSZoning"] = 1
        elif (q.loc[k, "MSZoning"] == 'RP'):
            q.loc[k, "MSZoning"] = 2
        elif q.loc[k, "MSZoning"] == 'RH' or q.loc[k, "MSZoning"] == 'RM':
            q.loc[k, "MSZoning"] = 3
        elif (q.loc[k, "MSZoning"] == 'I'):
            q.loc[k, "MSZoning"] = 4
        elif (q.loc[k, "MSZoning"] == 'RL'):
            q.loc[k, "MSZoning"] = 5
        elif (q.loc[k, "MSZoning"] == 'FV'):
            q.loc[k, "MSZoning"] = 6
    for l in range(len(q)):
        if q.loc[l, "SaleCondition"] == 'AdjLand':
            q.loc[l, "SaleCondition"] = 0
        elif q.loc[l, "SaleCondition"] == 'Abnorml' or q.loc[l, "SaleCondition"] == 'Family':
            q.loc[l, "SaleCondition"] = 1
        elif q.loc[l, "SaleCondition"] == 'Alloca':
            q.loc[l, "SaleCondition"] = 2
        elif q.loc[l, "SaleCondition"] == 'Normal':
            q.loc[l, "SaleCondition"] = 3
        else:
            q.loc[l, "SaleCondition"] = 4
    for l in range(len(q)):
        if q.loc[l, "Street"] == 'Grvl':
            q.loc[l, "Street"] = 0
        elif q.loc[l, "Street"] == 'Pave':
            q.loc[l, "Street"] = 1
    for l in range(len(q)):
        if q.loc[l, "LotShape"] == 'Reg':
            q.loc[l, "LotShape"] = 1
        elif q.loc[l, "LotShape"] == 'IR1' or q.loc[l, "LotShape"] == 'IR3':
            q.loc[l, "LotShape"] = 2
        elif q.loc[l, "LotShape"] == 'IR2':
            q.loc[l, "LotShape"] = 3
    q = q.drop(["Utilities"], axis=1)
    # for l in range(len(q)):
    #   if q.loc[l, "Utilities"] == 'NoSewr':
    #      q.loc[l, "Utilities"] = 0
    # elif q.loc[l, "Utilities"] == 'NoSeWa':
    #    q.loc[l, "Utilities"] = 1
    # elif q.loc[l, "Utilities"] == 'AllPub':
    #   q.loc[l, "Utilities"] = 2
    for l in range(len(q)):
        if q.loc[l, "HouseStyle"] == '1.5Unf':
            q.loc[l, "HouseStyle"] = 0
        elif q.loc[l, "HouseStyle"] == '1.5Fin' or q.loc[l, "HouseStyle"] == '2.5Unf' or q.loc[
            l, "HouseStyle"] == 'SFoyer':
            q.loc[l, "HouseStyle"] = 1
        elif q.loc[l, "HouseStyle"] == '1Story' or q.loc[l, "HouseStyle"] == 'SLvl':
            q.loc[l, "HouseStyle"] = 2
        else:
            q.loc[l, "HouseStyle"] = 3

    for l in range(len(q)):
        if q.loc[l, "PoolQC"] == "Ex":
            q.loc[l, "PoolQC"] = 2
        elif q.loc[l, "PoolQC"] == "Fa" or q.loc[l, "PoolQC"] == "Gd":
            q.loc[l, "PoolQC"] = 1
        else:
            q.loc[l, "PoolQC"] = 0

    for l in range(len(q)):
        if q.loc[l, "FireplaceQu"] == "Ex":
            q.loc[l, "FireplaceQu"] = 3
        elif q.loc[l, "FireplaceQu"] == "TA" or q.loc[l, "FireplaceQu"] == "Gd":
            q.loc[l, "FireplaceQu"] = 2
        elif q.loc[l, "FireplaceQu"] == "Fa":
            q.loc[l, "FireplaceQu"] = 1
        else:
            q.loc[l, "FireplaceQu"] = 0

    for l in range(len(q)):
        if q.loc[l, "OverallCond"] == 1:
            q.loc[l, "OverallCond"] = 0
        elif q.loc[l, "OverallCond"] == 3:
            q.loc[l, "OverallCond"] = 1
        elif q.loc[l, "OverallCond"] == 4:
            q.loc[l, "OverallCond"] = 2
        elif q.loc[l, "OverallCond"] == 2 or q.loc[l, "OverallCond"] == 6 or q.loc[l, "OverallCond"] == 7 or q.loc[
            l, "OverallCond"] == 8:
            q.loc[l, "OverallCond"] = 3
        else:
            q.loc[l, "OverallCond"] = 4
    for l in range(len(q)):
        if q.loc[l, "ExterQual"] == 'Po':
            q.loc[l, "ExterQual"] = 0
        elif q.loc[l, "ExterQual"] == "Fa":
            q.loc[l, "ExterQual"] = 1
        elif q.loc[l, "ExterQual"] == "TA":
            q.loc[l, "ExterQual"] = 2
        elif q.loc[l, "ExterQual"] == "Gd":
            q.loc[l, "ExterQual"] = 3
        else:
            q.loc[l, "ExterQual"] = 4
    for l in range(len(q)):
        if 1950 <= q.loc[l, "YearRemodAdd"] < 1970:
            q.loc[l, "YearRemodAdd"] = 0
        elif 1970 <= q.loc[l, "YearRemodAdd"] < 1990:
            q.loc[l, "YearRemodAdd"] = 1
        else:
            q.loc[l, "YearRemodAdd"] = 2


replace(x)
replace(newdata)
pl = np.array(x["SalePrice"])
pl = np.reshape(pl,(-1,1))
dt = x.loc[:,('MSSubClass','MSZoning','LotFrontage','LotArea','Street','Alley',
                    'LotShape','LandContour','LotConfig','LandSlope','Neighborhood',
       'LotConfig','LandSlope','Condition1','Condition2','BldgType','HouseStyle', 'OverallQual', 'OverallCond',
                    'YearBuilt', 'YearRemodAdd','RoofStyle','RoofMatl','Exterior1st',
                    'Exterior2nd','YearBuilt','MasVnrType','ExterQual','ExterCond','Foundation',
                    'BsmtQual','BsmtCond','BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF','Heating','HeatingQC',
       'Electrical', '1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
       'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr',
       'TotRmsAbvGrd', 'Functional'
       ,'GarageType','GarageQual','GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea',
       'Fence','MiscFeature','MiscVal',
       'SaleType','SaleCondition','YrSold')]#dt= x.loc[:,('GarageType','BsmtQual','BsmtFinType1','BsmtUnfSF','BsmtFinSF2','BsmtFinSF1','Condition1','Condition2','RoofMatl','Exterior1st','Exterior2nd','YrSold','ExterCond','CentralAir','MiscVal','WoodDeckSF','PavedDrive','TotalBsmtSF','BsmtFinType1','BsmtQual','BsmtCond','MasVnrArea','RoofStyle','LotConfig','LotFrontage','Exterior1st','MSZoning','SaleType','Fireplaces','LotArea','SaleCondition','Condition1','BldgType','RoofStyle','Neighborhood','YearBuilt','KitchenQual','FullBath','HalfBath','BsmtFullBath','BsmtHalfBath','GrLivArea','1stFlrSF','2ndFlrSF','MSZoning','HouseStyle','Utilities','LotShape','Street','SaleCondition','OverallCond','OverallQual','ExterQual','PoolQC','FireplaceQu','Foundation','GarageCars','GarageArea','LandContour','YearRemodAdd','TotRmsAbvGrd')]#,'GarageCars','GarageArea',,'ExterCond')]
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
   # print(dt)
sv = SVR(kernel='rbf',max_iter = 300)#,gamma=0.000000000001,max_iter = 500)
ri.fit(dt,x["SalePrice"])
dd = newdata.loc[:,('MSSubClass','MSZoning','LotFrontage','LotArea','Street','Alley',
                    'LotShape','LandContour','LotConfig','LandSlope','Neighborhood',
       'LotConfig','LandSlope','Condition1','Condition2','BldgType','HouseStyle', 'OverallQual', 'OverallCond',
                    'YearBuilt', 'YearRemodAdd','RoofStyle','RoofMatl','Exterior1st',
                    'Exterior2nd','YearBuilt','MasVnrType','ExterQual','ExterCond','Foundation',
                    'BsmtQual','BsmtCond','BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF','Heating','HeatingQC',
       'Electrical', '1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
       'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr',
       'TotRmsAbvGrd', 'Functional'
       ,'GarageType','GarageQual','GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea',
       'Fence','MiscFeature','MiscVal',
       'SaleType','SaleCondition','YrSold')]
#dd = newdata.loc[:,('GarageType','BsmtQual','BsmtFinType1','BsmtUnfSF','BsmtFinSF2','BsmtFinSF1','Condition1','Condition2','RoofMatl','Exterior1st','Exterior2nd','YrSold','ExterCond','CentralAir','MiscVal','WoodDeckSF','PavedDrive','TotalBsmtSF','BsmtFinType1','BsmtQual','BsmtCond','MasVnrArea','RoofStyle','LotConfig','LotFrontage','Exterior1st','MSZoning','SaleType','Fireplaces','LotArea','SaleCondition','Condition1','BldgType','RoofStyle','Neighborhood','YearBuilt','KitchenQual','FullBath','HalfBath','BsmtFullBath','BsmtHalfBath','GrLivArea','1stFlrSF','2ndFlrSF','MSZoning','HouseStyle','Utilities','LotShape','Street','SaleCondition','OverallCond','OverallQual','ExterQual','PoolQC','FireplaceQu','Foundation','GarageCars','GarageArea','LandContour','YearRemodAdd','TotRmsAbvGrd')]#,'YearRemodAdd','GarageCars','GarageArea',,'ExterCond')]
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#   print(dt)
dnew = ri.predict(dd)
newframe = pd.DataFrame({"Id":newdata["Id"],"SalePrice":dnew})
print(newframe)
newframe.to_csv('Submine2.csv',index=None)