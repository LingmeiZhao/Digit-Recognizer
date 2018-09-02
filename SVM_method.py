import pandas as pd
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from sklearn import svm
#%matplotlib inline

labeled_images=pd.read_csv('train.csv')
images=labeled_images.iloc[0:5000,1:]
labels=labeled_images.iloc[0:5000,:1]
(train_images,test_images,train_labels,test_labels)=train_test_split(images,labels,random_state=0)

i=1
img=train_images.iloc[i].values
img=img.reshape((28,28))
plt.imshow(img,cmap='gray')
plt.title(train_labels.iloc[i,0])
plt.show()

plt.hist(train_images.iloc[i])

clf=svm.SVC()
clf.fit(train_images, train_labels.values.ravel())
clf.score(test_images,test_labels)

test_images[test_images>0]=1
train_images[train_images>0]=1

img=train_images.iloc[i].values.reshape((28,28))
plt.imshow(img,cmap='binary')
plt.title(train_labels.iloc[i])

plt.hist(train_images.iloc[i])

clf=svm.SVC()
clf.fit(train_images,train_labels.values.ravel())
clf.score(test_images,test_labels)

test_data=pd.read_csv('test.csv')
test_data[test_data>0]=1;
results=clf.predict(test_data)

results

df=pd.DataFrame(results)
df.index.name='ImageID'
df.index+=1;
df.columns=['Label']
df.to_csv('result.csv',header=True)


