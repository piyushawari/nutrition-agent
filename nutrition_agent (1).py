import requests
import json
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParams

# --- STEP 1: Set your USDA API key ---
USDA_API_KEY = "qxvCuG7RjqWs6yBwIQbYmtIkBveiUbTnyssKjKYA"
SEARCH_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"
DETAIL_URL = "https://api.nal.usda.gov/fdc/v1/food/"

# --- STEP 2: Get nutrient data for a food item ---
def get_nutrition(food_item):
    params = {
        "query": food_item,
        "pageSize": 1,
        "api_key": USDA_API_KEY
    }
    response = requests.get(SEARCH_URL, params=params)
    result = response.json()

    if not result.get("foods"):
        return None

    food = result["foods"][0]
    fdc_id = food["fdcId"]

    # Fetch full nutrient data
    response = requests.get(f"{DETAIL_URL}{fdc_id}?api_key={USDA_API_KEY}")
    food_data = response.json()

    nutrients = {"calories": None, "protein": None, "carbs": None, "fat": None}

    for nutrient in food_data.get("foodNutrients", []):
        name = nutrient.get("nutrientName", "").lower()
        value = nutrient.get("value", 0)
        unit = nutrient.get("unitName", "")

        if "energy" in name and nutrients["calories"] is None:
            nutrients["calories"] = round(value / 4.184, 2) if unit == "kJ" else value
        elif "protein" in name and nutrients["protein"] is None:
            nutrients["protein"] = value
        elif "carbohydrate" in name and nutrients["carbs"] is None:
            nutrients["carbs"] = value
        elif "fat" in name and nutrients["fat"] is None:
            nutrients["fat"] = value

    return {
        "description": food.get("description", ""),
        "nutrients": nutrients
    }

# --- STEP 3: Generate prompt for AI model ---
def build_prompt(food_info):
    nutrients = food_info["nutrients"]
    return f"""
Suggest a healthy breakfast that includes {food_info['description']} 
(calories: {nutrients['calories']} kcal, 
protein: {nutrients['protein']} g, 
carbs: {nutrients['carbs']} g, 
fat: {nutrients['fat']} g) 
for a diabetic patient. Explain why it's a good choice.
"""

# --- STEP 4: Set up Watsonx credentials ---
wml_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "a2Td0nbWWX2dN7to1-j76ZxY940lTfunM8engyYyoiZD"
}

project_id = "bea3339e-2025-4d66-888a-1c8b2a8c746e
"
model_id = "360282fb-4fb1-431e-a355-c71fac425b17"  # or any other model you've deployed

# --- STEP 5: Run the model ---
def get_ai_response(prompt):
    gen_params = {
        GenTextParams.DECODING_METHOD: "greedy",
        GenTextParams.MAX_NEW_TOKENS: 300,
        GenTextParams.TEMPERATURE: 0.7
    }

    model = Model(model_id=model_id, credentials=wml_credentials, project_id=project_id)
    response = model.generate(prompt=prompt, params=gen_params)
    return response["results"][0]["generated_text"]

# --- STEP 6: Try it ---
if __name__ == "__main__":
    food_item = input("Enter a food item: ")
    food_info = get_nutrition(food_item)

    if not food_info:
        print("Food not found.")
    else:
        prompt = build_prompt(food_info)
        print("\n🧠 AI Prompt:\n", prompt)
        response = get_ai_response(prompt)
        print("\n🤖 Nutrition Agent Says:\n", response)
