# 🧠 Nutrition Agent - Smartest AI Nutrition Assistant

This project uses **IBM Watsonx**, **USDA API**, and **generative AI** to create a smart, interactive nutrition agent that provides personalized meal suggestions.

## 🚀 Features
- Accepts food name input and retrieves nutritional data via the USDA API.
- Suggests healthy meals for specific health conditions (like diabetes).
- Explains nutritional benefits using LLM-powered reasoning.
- Interactive prompt testing through Watsonx Agent Studio.

## 🔧 Technologies Used
- IBM Watsonx.ai Studio
- IBM Cloud Lite (deployment)
- USDA FoodData Central API
- Python

## 🛠 How It Works
1. User provides food input (e.g., "banana").
2. Agent fetches nutritional data using the USDA API.
3. Watsonx agent generates tailored meal recommendations.
4. Results include caloric breakdown and contextual advice for health conditions.

## 📁 Files
- `README.md` – project overview
- `config.py` – contains your `API_KEY`, `PROJECT_ID`, and `MODEL_ID`
- `prompt_test_examples.txt` – sample prompts used during testing
- `screenshot/` – includes interface previews or agent responses

## 🔐 Notes
- Ensure you securely store your API Key (do not upload it publicly).
- IBM allows only one Lite plan instance per service. Upgrade or delete unused ones to redeploy.

## 📸 Sample Prompt
> Suggest a diabetes-friendly breakfast using banana and oats. Explain why it's healthy.

---

