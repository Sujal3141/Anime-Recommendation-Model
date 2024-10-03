# Anime-Recommendation-Model

## Project Overview

○ This project aims to build a Recommendation model that can suggest anime which are similar based on their story ,characters,director etc. 

○ The dataset contains various features such as :
	
Anime_id - Id for an Anime is unique so this will act kind of a primary key but this does not play any role in training of the     Recommendation system.

Title - This is the title of the anime . Sometimes anime with similar title may be related to each other, so this may play in role in training.

Other columns which may be usefull in training the model: 

[Genre ,Synopsis,Type,Producer,Studio,Rating	,ScoredBy	Popularity	,Members,Source	,Aired.]






## Objectives

○ Dropping the unnecessary columns (['Anime_id','Title','Genre','Synopsis'] are playing a major role in deciding the anime in comparision to other so dropping columns except these .)

○ Checking for null values . As their are very few null values in comparision to the dataset ,the most optimal way is to drop the rows with null values.

○ Concatnating all columns to a single column "tag".  

○ Applying stemming for recognising the word with same meaning as same.

○ Applying text vectorization to convert text into vectors and selecting maximum 5000 features . 

○ Using cosine similarity to get similar vectors and the anime corresponding to that will be similar.





## Technologies Used

○ Python: The core programming language for implementing the data processing .

○ Pandas : For data manipulation and analysis.

○ TextVectorization: For training the model.

○ Cosine Similarity - For finding similar vectors .

