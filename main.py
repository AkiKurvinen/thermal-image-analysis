# Predict hand position (open/closed)
# by using 4 thermal images from camera wristband

import matplotlib.pyplot as plt

# Import pixel data from camera files
from readfile import get_all_data
X, y = get_all_data()
y= y.values.ravel()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

# Test if data contains the phenomenon
# by using simple Logistic Regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='lbfgs', max_iter=1000)
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)
y_test_pred = logreg.predict(X_test)


from sklearn.metrics import confusion_matrix
import seaborn as sns

ax = plt.subplot()
lr_cm = confusion_matrix(y_test, y_test_pred)
sns.heatmap(lr_cm, annot=True, fmt='g', ax=ax)
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for LogisticRegression'); 

ax.xaxis.set_ticklabels(['open', 'closed']);
ax.yaxis.set_ticklabels(['open', 'closed']);
plt.show()

# Use cross-validation for accuracy score
from sklearn.linear_model import LogisticRegressionCV
clf = LogisticRegressionCV(cv=5, random_state=0, max_iter=1000).fit(X, y)
clf.predict(X)
clf.predict_proba(X).shape
print('accuracy:',clf.score(X, y))
fold_scores = clf.scores_[1]
fold_scores = fold_scores[:,0]
print(fold_scores.mean())

# accuracy: 0.95
# fold scores mean: 0.875

def show_image(row, cam):
    st_pix = cam * 768
    end_px = st_pix + 768
    img = X.iloc[row, st_pix:end_px]
    img = img.values.reshape(24,32)
    sns.heatmap(img)
    plt.show()
    
# Show 4 images of same situation
show_image(0, 0)
show_image(0, 1)
show_image(0, 2)
show_image(0, 3)
