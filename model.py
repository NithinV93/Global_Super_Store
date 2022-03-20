import pandas as pd
import pickle
import numpy as np

import warnings
warnings.filterwarnings('ignore')



from sklearn.model_selection import train_test_split
df= pd.read_excel('Global_Superstore.xls')
df_clean = df[['Profit','Sales','Discount','Shipping Cost','Quantity','Segment','Category']]
final_dataset = pd.get_dummies(df_clean)
X=final_dataset.iloc[:,1:]
y=final_dataset.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.20)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=20, min_samples_leaf=10, min_samples_split=5,
                      n_estimators=100, random_state=42)
#Fitting the model
m=rf.fit(x_train, y_train)

#Saving the model to disk
pickle.dump(rf,open('model.pkl','wb') )