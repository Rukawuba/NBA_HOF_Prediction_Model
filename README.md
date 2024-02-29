

# Hall of Fame Prediction Model

## Overview
This repository contains code for a predictive model built using Logistic Regression to determine whether a player will be inducted into the Hall of Fame. The model utilizes statistical data from both past and present players to make predictions.

## Dataset
The dataset used for training and testing the model consists of various features from player career statistics. Each record in the dataset represents a player, with a binary label indicating whether the player has been inducted into the Hall of Fame or not. The data has been taken from the NBA API from various tables and then combined to analyze each player's career and determine whether they have a career that would leave them in the Hall of Fame. 

## Model
The predictive model is built using Logistic Regression, a popular algorithm for binary classification tasks. Logistic Regression calculates the probability that a given input belongs to a certain class (in this case, whether a player will make the Hall of Fame or not) using players who are already currently in the Hall of Fame as a baseline metric.

## Usage
To use the model:

Clone this repository to your local machine.
Install the required dependencies listed in requirements.txt.
Run the provided scripts to train the model, evaluate its performance, and make predictions on new data.
Customize the model by tweaking hyperparameters or adding/removing features as needed.
Results
The model's performance metrics such as accuracy, precision, recall, and F1-score are documented in the provided notebooks and/or scripts. These metrics can help assess the model's effectiveness in predicting Hall of Fame inductions.

## Contributions
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Acknowledgments
Special thanks to the creators of the NBA API dataset that was used in this project.
Inspiration for this project came from the desire to explore predictive modeling in sports analytics.
