

#  Prediction of an American adult view toward computers algorithm based on the data collected from a Pew Research Center Survey conducted in 2018


## JUSTIFICATION
Nowadays, we are observing a considerable development of machine learning and Artificial Intelligence. Computer decisions are running our life: the recommendation of a simple book to read or finding our next travel destinations are the results of algorithms based on our past behaviors. Analysts expect that people will become even more dependent on networked artificial intelligence (AI) in complex digital systems. Hence, different sectors raise the concern about impact of AI on production and free will of human being. Before getting to these concerns, a couple of questions are worth asking: How do we perceive computer decisions? Is that perception explained by our demographic profiles and habits? Hence, the purpose of this research where I will try to answer the previous questions on machine learning with .. machine learning based on some classification models.

## OBJECTIVES
This work is purely an academic research - an individual project on classification for the Data Science bootcamp at Flatiron School. It was a good opportunity for me to use this project to work on a subject that we talked about on a daily basis to build my Data Science portfolio.
Otherwise, I want to find out:
How social and demographic behaviors of an individual can help predict is view towards computer decisions? 

## HYPOTHESES
2 main hypotheses will guide my work:

1. Based on an adult profiles and social media behaviors, we can determine his attitudes towards computer algorithms.

2. Social and economic profiles (income, ethnicity, education) are more likely to influence the perception towards computer decisions.


## METHODOLOGY
I used Python to undergo my analysis and models in my research. For managing my data and plotting graphs, I used Pandas, Matplotlib and Seaborn. Scikit-learn was really useful for fitting, predicting and evaluating models. Other librairies used: Numpy... 

I downloaded database with all the answers of a survey conducted by PEW RESEARCH CENTER in May-June 2018. The SPSS file from the [Pew Research Center website](https://www.pewinternet.org/?post_type=dataset) can be found [here](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/W35_May18/ATP%20W35.sav).

Observations are 4,594 non-institutionalized persons age 18 and over, living in the US, including Alaska and Hawaii.


## EXPLORATORY DATA ANALYSIS
#### Target variable: 
View towards computer decisions:
1. It is possible for computer programs to make decisions without human bias (PERFECT)
2. Computer programs will always reflect the biases of the people who designed them
#### Features (33 selected from 190):
The endogenous  variables used are:
1. Demographics (Income - Age - Marital Status - Religion)
2. Specific questions from the survey re social media use and opinions related to major technology companies


Before working with the data, some data cleaning and transformation were necessary:
1. Remove observations with missing data (answers coded 99 or NAN)
2. Rename columns name
3. Convert the answers for 'Refused’ to a neutral modality
4. Scale the data for better performance of models and like for like comparison
5. Create dummies
 
#### Profiles of the respondents
![Distribution target](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/Distribution_target.png)
* Majority of the adults interviewed think that computer algorithms are biased by designers errors

![age](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/Age.png)

![Income](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/Income2.png)

![Education](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/Edcation.png)

* 32% of the respondents are between 50-64 years old
* More than the average are at least college graduate
* 44% are earning US$75k or more
* These profiles shows how the respondents are aware of the question asked

#### Attitudes towards computer algorithms by Demographics Categories of respondents
![by Income](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/IncomevsTarget.png)

![by Marital Status](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/MaritalvsTarget.png)

![by Religion](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/ReligionvsTarget.png)

* The attitudes towards computer decisions are not uniform and vary based on the profiles

#### Views based on Social Media Behavior
![Media Influence Policy](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/MediainfluencevsTarget.png)

![Media Create Movement](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/MediacontentvsTarget.png)

![Trust](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/TrustTechvsTarget.png)

* The less important an adult consider social media influence, the most likely he will think computer decisions are biased
* Similarly for creation of movement by social media
* We can assume some difference of views based on interactions of respondents with social media or major tech companies

#### Independence of Features and Target
![Correlation Heatmap](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/Correlation-Heatmap.png)

![Correlation vs. target](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/Correlation-coef.png)

* No correlation between the features and target variable that would cause any issue to the modeling process.


## MODELS
#### BASELINE
In order to evaluate the different results that I will get, I started by establishig a baseline model. I picked the DummyClassifier which is a classifier that makes predictions using simple rules. The Strategy: “uniform” was selected to generate predictions uniformly at random.

![baseline](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/DummyResults.png)

#### MODELS USED
![modelsresults](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/Models%20Results.png)

* I used different methods to tune the hyperparameters of the models
* F1 score and accuracy rate were mostly used to compare the models

* KNN didn’t perform well with 51% AUC
* Using AUC, logistic regression, Random Forest and Adaboost gave better accuracy score.
* XGBoost retained due to better f1 score compared to Adaboost
* Best models didn’t used all the features - Possibly of reduce our features

#### PCA
The purpose of the PCA is to reduce the features in the dataset into components while preserving the maximum amount of information possible. The components can be used for modeling afterwards. Graphs below showed respectively a visual to understand PCA and the results of the model using PCA. SVM was incorporated at this stage as the components might be hardly be able to get classified (as shown in the 3D graph - a representation of the first 3 components) and SVM is good as classifying in such case.

![pca graphs](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/pca%20explaining.png)

![result models pca](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/pca%20models.png)

## FINAL RESULT
Once I have the models built, I apply them on the testing data to evaluate them.

![testing](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/testing%20final.png)

![importance features](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/importance1.png)

* The logistic regression classified with an accuracy of 65% unseen data
* The SVM model was more balanced with good performance for both training (f1-score 47%) and testing data (64% accuracy) 
* Variables related to the demographics category were mostly used for the classification - "internet users" was important (trivial) to make the predictions


## FINAL CONSIDERATIONS
After fitting and evaluating different classification models, I kept 2 that did better than tossing a coin.
It was possible with ~65% accuracy to make the distinguish between attitudes of American adults towards computer decisions.
However, it would be interesting to use other variables in the database for better accuracy. Aslo, other methods can help tune the models in a more effective way.
Instead using a random train, test, split, an extension of this reseach would be to experiment cross validation for training and testing the models






