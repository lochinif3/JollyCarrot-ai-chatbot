# JollyCarrot Chatbot
A Discord based, simple AI chatbot that you can directly use for any domain from rabbits to recipes without reinventing the wheel.

### Prerequisites
  - Install Jupyter Notebook.  
  - Create a Discord server and bot via the Discord Developer Portal.

### Train the Models
  - Open and run buildNLP.ipynb to generate:
      - chatbot_model.keras
      - words.pkl
      - classes.pkl
  - Open and run Algorithms_Evaluation.ipynb to generate:
      - decision_tree_model.pkl
      - scaler.pkl

### Configure Tokens
  - In your bot code, set:
      - TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
      - api_key = 'YOUR_API_KEY'

### Run the Bot
  - Launch the bot script (JollyCarrot.ipynb) and invite it to your Discord server.




