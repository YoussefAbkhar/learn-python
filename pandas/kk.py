import pandas as pd
import matplotlib.pyplot as plt
#matplotlib inline

fl = pd.read_excel('../selenium/example.xlsx')

print(fl)

# print(fl.head())


# print(fl.shape)

# fl.info()
# print(fl.describe())
# fl.drop(['age','home.dest'],axis=1,inplace=True)
# fl.info()
# fl['age'] = fl['age'].fillna(0)
# fl.info()


# fl.hist(bins=80,figsize=(30,20))
# fl = [100,200,150,500]
# s = pd.DataFrame(fl)
# s.plt()
