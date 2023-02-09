## package import ##

import pandas as pd



train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")

train.head(6)
test.head()

train.shape
test.shape
test.info()
test.isnull()
test.isnull().sum()


# 그래프 함수 정의 #
## package import
import seaborn as sns
sns.set()

## define the chart generation function
def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    ## how many survived people in train dataframe / train[train['Survived']==1] The amount of Survived person in feature
    dead = train[train["Survived"]==0][feature].value_counts()
    ## how many people dead in train dataframe
    frame_train = pd.DataFrame([survived, dead])
    frame_train.index = ["Survived", "Dead"]
    frame_train.plot(kind = "bar", stacked = True, figsize = (10, 5))
    return frame_train      ## if do not write phase of "return frame_train", It can not define "frame_train" below.


frame_train = bar_chart('Sex') # Showing the plot according "Sex" index, and setting the value(frame_train)

tuples = survived = train[train['Survived']==1]['Sex'].value_counts()
dead_tup = train[train["Survived"]==0]['Sex'].value_counts()
print(dead_tup)
print(str(sum(dead_tup)), "+", str(sum(tuples)), "=" , str(sum(dead_tup + tuples))) ## checking the valuse(Just I wanna know)

bar_chart("Pclass")     ## Showing the plot based on the "Pclass". Pclass is a level of the ticket, one is more expensive.
bar_chart("SibSp")      ## Showing the plot based on the "SibSp". SibSp is to see the number of boarded person together.(siblings, spouse)
bar_chart("Parch")      ## Boarding together Parents or Children.
bar_chart("Embarked")   ## what section did people board.