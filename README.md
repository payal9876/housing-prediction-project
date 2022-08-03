# housing-prediction-project
A machine learning project to predict the prices of the houses in the california region.
This is the end to end project where i have used DOCKER to create continuous integration and continuous deployment pipeline and i have deployed it over the heroku platform 

# Objective
 We have the dataset of california housing society where the features are given below
 
 Columns:
    
	Longitude
 
	Latitude
 
	housing_median_age
 
	total_room
	
	population
	
	total_bedroom
	
	households
	
	median_income
	
	median_house_value
	
	ocean_proximity

Now, The objective is to create a machine learning model which can predict prices of the houses in the particular region


# REQUIREMENTS

  FLASK

  DOCKER

  VSCODE
  
  GIT CLI
  
  HEROKU 
  
# PROJECT -OVERVIEW

  DATA INGESTED PROCESS-
    I HAVE CREATED ARTIFACTS TO HOLD MY DATA AND THEN INGESTED DATA FROM GITHUB AND SAVED IT ONTO ARTIFACTS
    
    
  DATA VALIDATION PROCESS-
    I HAVE USED EVIDENTLY LIBRARY TO IDENTIFY ANY DATA DRIFT AND THEN SAVED REPORT ONTO ARTIFACTS
    

  DATA TRANSFORMATION PROCESS-
    I HAVE USED SIMPLE IMPUTER FOR REMOVING NULL VALUES AND ONE HOT ENCODER FOR CATEGORICAL COLUMNS
    
    
  MODEL_TRAINER_PROCESS-
    I HAVE USED REGRESSION AND RANDOM FOREST MODEL FOR TRAINING DATASET AND I HAVE SAVED IT ONTO PICKLE FILE
    
    
  MODEL_EVALUATION_PROCESS-
  
    I HAVE SAVED BEST MODEL IN THIS PROCESS. I GOT APPROXIMATELY 65% ACCURACY
    
    
 # DEPLOYMENT LINK
 
 https://housing-22.herokuapp.com/
    
   
  
      
    
    
