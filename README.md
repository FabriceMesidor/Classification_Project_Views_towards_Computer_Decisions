

#  Prediction of an American adult view toward computers algorithm based on the data collected from a Pew Research Center Survey conducted in 2018


## SUMMARY 
Predict an American view towards computer decisions


## JUSTIFICATION
Nowadays, we are observing an considerable development of machine learning and Artificial Intelligence. Computer decisions are running our life: the recommendation of a simple book to read or finding our next travel destinations are the results of algorithms based on our past behaviors. Analysts expect that people will become even more dependent on networked artificial intelligence (AI) in complex digital systems. Hence, different sectors raise the concern about impact of AI on production and free will of human being. Before getting to these concerns, a couple of questions are worth asking: How do we perceive computer decisions? Is that perception explained by our demographic profiles and habits? Hence, the purpose of this research which will be try to answer the previous questions on machine learning with .. machine learning based on some classification models.

## OBJECTIVES
This work is purely an academic research - an individual project on classification for the Data Science bootcamp at Flatiron School. It was a good opportunity for me to use this project to work on a subject that we talked about on a daily basis to build my Data Science portfolio.
Otherwise, I want to find out:
How social and demographic behavior of an individual can help predict is view towards computer decisions? 

## HYPOTHESES
2 main hypotheses will guide my work:

1. Based on an adult profiles and social media behaviors, we can determine his attitudes towards computer algorithms

2. Social and economic profiles (income, ethnicity, education) are more likely to influence the perception towards computer decisions.


## METHODOLOGY
I used Python to undergo my analysis and models in my research. For managing my data and plotting graphs, I used Pandas and Matplotlib. ScikitLearn was really useful for fitting, predicting and evaluating models. Other librairies used: Numpy... 

I downloaded the survey data conducted by PEW RESEARCH CENTER in May-June 2018. The SPSS file from the [Pew Research Center website](https://www.pewinternet.org/?post_type=dataset) can be found [here](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/W35_May18/ATP%20W35.sav).

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
In order to evaluate the different results that I will get, I started by establishig a baseline model. I picked the DummyClassifier which is a classifier that makes predictions using simple rules. The Strategy: “uniform” was selected to generate predictions uniformly at random

#### MODELS USED



* I used different methods to tune the hyperparameters of the models
* F1 score and accuracy rate were used to comprare the models

#### EVALUATION:
* KNN didn’t perform well with 51% AUC
* Using AUC, logistic regression, Random Forest and Adaboost gave better accuracy score.
* XGBoost retained due to better f1 score compared to Adaboost
* Best models didn’t used all the features - Possibly of reduce our features


PCA to reduce the features
Models results after PCA

## FINAL MODEL


## CONSIDERATIONS





