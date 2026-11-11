
# Recipe Recommendation System

A personalised recipe recommendation application that suggests Indian recipes based on available ingredients, dietary preferences and cooking time.

## Project Overview

The system helps users discover recipes using ingredients they already have. Users can select ingredients, specify dietary preferences and set a maximum cooking time to receive ranked recipe recommendations.

## Features

- Ingredient-based recipe matching.
- Vegetarian, vegan and non-vegetarian filters.
- Adjustable maximum cooking time.
- Interactive ingredient selection.
- Displays matched and missing ingredients.
- Ranks and displays up to 10 matching recipes.
- CSV-based recipe dataset.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive user interface |
| Pandas | Dataset processing |
| CSV | Recipe data storage |
| C++ | Original DSA project implementation (source to be added) |

## Recommendation Logic

1. Collect user-selected ingredients.
2. Filter recipes by dietary preference.
3. Remove recipes exceeding the selected cooking time.
4. Calculate matching and missing ingredients.
5. Rank recipes by:
   - Highest number of matching ingredients.
   - Fewest missing ingredients.
   - Shortest cooking time.
6. Display the top matching results.

## Project Structure

```text
recipe-recommender/
├── README.md
├── recipe_app.py
├── recipes_dataset_india.csv
└── requirements.txt
```

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/JayP-1/recipe-recommender.git
cd recipe-recommender
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run recipe_app.py
```

Open the local Streamlit URL displayed in your terminal.

## Future Improvements

- Improve ingredient matching with fuzzy search.
- Introduce ingredient synonyms.
- Add user profiles and saved preferences.
- Develop a REST API for integration with other interfaces.
- Expand the recipe dataset.

## Project Information

**Domain:** Data Structures, Python Development and Recommendation Systems.

Developed as an academic software engineering project at Manipal Institute of Technology.
