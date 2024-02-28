import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
with open('../models/logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)



#Was working even without this mapping code.
# Load the name_to_id_mapping.pkl file
with open('../models/name_to_id_mapping.pkl', 'rb') as file:
    name_to_id_mapping = pickle.load(file)

# Load your dataset containing player statistics
df = pd.read_csv('../data/aggregated_stats.csv')

df['Player Name'] = df['Player Name'].apply(str)


# Title
st.title("Hall of Fame Prediction")


# User input: Player's name
player_name = st.text_input("Enter a player's name")



# Add a button to explore available player names
if st.button("Explore Player Names"):
    available_players = df['Player Name'].unique()
    st.write("Available player names in the dataset:")
    st.write(available_players)

if st.button("Predict"):
    # Find player's statistics from your dataset based on the entered name
    player_stats = df[df['Player Name'] == player_name]

    if not player_stats.empty:
        # Remove non-predictive columns and use the remaining features for prediction
        X_player = player_stats.drop(['HOF', 'Player Name','PLAYER_ID','Player Name', 'GP', 'FGA',
       'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTA', 'FT_PCT', 'OREB',
       'DREB', 'REB', 'AST','BLK', 'TOV', 'PF', 'TotalSeasons' ], axis=1)

        # Make a prediction using the model
        prediction = model.predict(X_player)

        # Display the prediction
        if prediction[0] == 1:
            st.write(f"{player_name} is predicted to be in the Hall of Fame.")
        else:
            st.write(f"{player_name} is not predicted to be in the Hall of Fame.")
    else:
        st.write(f"No player found with the name {player_name}. Please check the player's name.")