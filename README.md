🧠 Nutrition Agent – Smart AI Nutrition Assistant
A next-gen nutrition assistant powered by IBM Watsonx, USDA API, and Generative AI that delivers personalized meal suggestions and explains their nutritional benefits in real time.

🚀 Features
Nutritional Data Lookup – Enter any food name and instantly retrieve accurate nutrition details from the USDA FoodData Central API.

Condition-Based Meal Planning – Get meal suggestions tailored for specific health conditions (e.g., diabetes, heart health).

AI-Powered Explanations – Understand the why behind each meal suggestion with reasoning powered by LLMs.

Interactive Testing – Test your queries and get instant responses via Watsonx Agent Studio.

🔧 Technologies Used
IBM Watsonx.ai Studio – AI model hosting & reasoning

IBM Cloud Lite – Cloud deployment environment

USDA FoodData Central API – Reliable nutritional data source

Python – Core backend logic

🛠 How It Works
User Input – Provide a food name (e.g., "banana").

Data Fetching – Retrieve detailed nutrition data from the USDA API.

AI Reasoning – Watsonx agent generates personalized meal recommendations.

Final Output – Results include caloric breakdown and contextual health advice.

📁 Project Files
README.md – Project overview & setup guide

config.py – Contains your API_KEY, PROJECT_ID, and MODEL_ID

prompt_test_examples.txt – Sample prompts for testing

screenshot/ – UI previews & example outputs

🔐 Notes
Store your API key securely — do not upload it publicly.

IBM Cloud Lite allows one Lite plan instance per service — upgrade or delete unused instances before redeploying.

📸 Sample Prompt
Suggest a diabetes-friendly breakfast using banana and oats. Explain why it's healthy.
