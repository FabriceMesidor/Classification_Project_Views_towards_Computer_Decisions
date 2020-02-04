#  Prediction of an American adult view toward computers algorithm based on the data collected from a Pew Research Center Survey conducted in 2018


## JUSTIFICATION
Nowadays, we are observing a considerable development of machine learning and Artificial Intelligence. Computer decisions are running our life with more expectations in the future. While concerns about impact of AI are being raised, it is also worth asking: How do we perceive computer decisions? Is that perception explained by our demographic profiles and habits?

## OBJECTIVE
How social and demographic behaviors of an individual can help predict is view towards computer decisions? 

## HYPOTHESES
1. Based on an adult profiles and social media behaviors, we can determine his attitudes towards computer algorithms.
2. Social and economic profiles (income, ethnicity, education) are more likely to influence the perception towards computer decisions.

## EXPLORATORY DATA ANALYSIS
Data: survey conducted by PEW RESEARCH CENTER in May-June 2018: [Pew Research Center website](https://www.pewinternet.org/?post_type=dataset) --> (https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/W35_May18/ATP%20W35.sav).

Observations are 4,594 non-institutionalized persons age 18 and over, living in the US, including Alaska and Hawaii.
#### Target variable: 
View towards computer decisions:
1. It is possible for computer programs to make decisions without human bias (PERFECT)
2. Computer programs will always reflect the biases of the people who designed them
#### Features (33 selected from 190):

#### Data Cleaning
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

* 32% of the respondents are between 50-64 years old
* More than the average are at least college graduate
* 44% are earning US$75k or more

#### Attitudes towards computer algorithms by Demographics Categories of respondents
![by Income](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/IncomevsTarget.png)

![by Marital Status](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/MaritalvsTarget.png)

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

* No correlation between the features and target variable that would cause any issue to the modeling process.


## MODELS
#### BASELINE
DummyClassifier: 50% accuracy

#### MODELS USED
![modelsresults](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/Models%20Results.png)

* F1 score and accuracy rate were mostly used to compare the models (all tuned)

* KNN didn’t perform well with 51% AUC
* Using AUC, logistic regression, Random Forest and Adaboost gave better accuracy score.
* XGBoost retained due to better f1 score compared to Adaboost
* Best models didn’t used all the features - Possibly of reduce our features

#### PCA
The purpose of the PCA is to reduce the features in the dataset into components while preserving the maximum amount of information possible. The components can be used for modeling afterwards. Graphs below showed respectively a visual to understand PCA and the results of the model using PCA. SVM was incorporated at this stage as the components might be hardly be able to get classified (as shown in the 3D graph - a representation of the first 3 components) and SVM is good as classifying in such case.

![pca graphs](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/pca%20explaining.png)

## FINAL RESULT

![importance features](https://github.com/FabriceMesidor/Classification_Project_Views_towards_Computer_Decisions/blob/master/Support-Docs/Graphs-Pics/importance1.png)

* The logistic regression classified with an accuracy of 65% unseen data
* The SVM model was more balanced with good performance for both training (f1-score 47%) and testing data (64% accuracy) 
* Variables related to the demographics category were mostly used for the classification - "internet users" was important (trivial) to make the predictions


## FINAL CONSIDERATIONS
It was possible with ~65% accuracy to make the distinguish between attitudes of American adults towards computer decisions.
However, it would be interesting to use other variables in the database for better accuracy and other methods for tuning.






