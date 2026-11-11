import streamlit as st
import pandas as pd

st.set_page_config(page_title="Recipe Recommender", layout="wide")

@st.cache_data
def load_data(path="recipes_dataset_india.csv"):
    df = pd.read_csv(path)
    df['ingredients_list'] = df['ingredients'].apply(lambda x: [i.strip().lower() for i in str(x).split("|") if i.strip()])
    return df

df = load_data("recipes_dataset_india.csv")



st.title("🍽️ Recipe Recommender — UI Extension")
st.markdown("Future-work frontend for the DSA C++ mini-project. Uses same CSV dataset and matching logic.")

with st.sidebar:
    st.header("Input Controls")
    st.subheader("Choose dietary preference")
    diet = st.radio("Diet", options=["veg", "vegan", "non-veg"], index=0)
    st.subheader("Max cooking time (minutes)")
    max_time = st.slider("Max time", min_value=5, max_value=120, value=45, step=5)
    st.subheader("Quick pick ingredient groups (expandable)")
    with st.expander("Vegetables"):
        v_potato = st.checkbox("potato", help="potato")
        v_onion = st.checkbox("onion")
        v_tomato = st.checkbox("tomato")
        v_peas = st.checkbox("peas")
        v_carrot = st.checkbox("carrot")
    with st.expander("Grains & Pulses"):
        g_rice = st.checkbox("rice")
        g_wheat = st.checkbox("wheat flour")
        g_poha = st.checkbox("poha")
        g_dal = st.checkbox("moong dal")
    with st.expander("Dairy & Protein"):
        d_paneer = st.checkbox("paneer")
        d_milk = st.checkbox("milk")
        d_egg = st.checkbox("egg")
        d_chicken = st.checkbox("chicken")
    with st.expander("Spices & Staples"):
        s_salt = st.checkbox("salt", value=True)
        s_cumin = st.checkbox("cumin")
        s_turmeric = st.checkbox("turmeric")
        s_garlic = st.checkbox("garlic")

    st.subheader("Extra ingredients (comma-separated)")
    extras = st.text_input("Extras (type other ingredients)")



    st.markdown("---")
    run = st.button("🔎 Recommend Recipes")

user_ings = set()
choices = {
    "potato": v_potato, "onion": v_onion, "tomato": v_tomato, "peas": v_peas, "carrot": v_carrot,
    "rice": g_rice, "wheat flour": g_wheat, "poha": g_poha, "moong dal": g_dal,
    "paneer": d_paneer, "milk": d_milk, "egg": d_egg, "chicken": d_chicken,
    "salt": s_salt, "cumin": s_cumin, "turmeric": s_turmeric, "garlic": s_garlic
}
for k,v in choices.items():
    if v: user_ings.add(k)



if extras:
    for it in extras.split(","):
        it = it.strip().lower()
        if it: user_ings.add(it)

if run:
    st.info(f"Searching for recipes — Diet: **{diet}**, Max time: **{max_time} min**, Ingredients: **{', '.join(sorted(user_ings))}**")
    candidates = []
    for idx, row in df.iterrows():
        if row['diet_type'].lower() != diet:
            continue
        if int(row['cook_time_minutes']) > max_time:
            continue
        ings = row['ingredients_list']
        matches = sum(1 for ing in ings if ing in user_ings)
        missing = len(ings) - matches




        if matches > 0:
            candidates.append((matches, -missing, int(row['cook_time_minutes']), idx))

    if not candidates:
        st.warning("No matching recipes found. Try expanding ingredients or increasing max time.")
    else:
        candidates.sort(reverse=True)
        topk = min(10, len(candidates))
        for rank in range(topk):
            matches, neg_missing, cooktime, idx = candidates[rank]
            missing = -neg_missing
            row = df.loc[idx]
            st.markdown("---")
            cols = st.columns([1,3])
            if row['diet_type'].lower() == 'veg':
                emoji = "🥗"
            elif row['diet_type'].lower() == 'vegan':
                emoji = "🌱"
            else:
                emoji = "🍗"
            cols[0].markdown(f"### {emoji}")
            title = f"**{row['name']}** — {row['diet_type']} • {row['cook_time_minutes']} min"
            cols[1].markdown(title)
            matched_list = [ing for ing in row['ingredients_list'] if ing in user_ings]
            missing_list = [ing for ing in row['ingredients_list'] if ing not in user_ings]
            cols[1].markdown(f"**Matches ({matches}):** " + ", ".join(matched_list))
            cols[1].markdown(f"**Missing ({missing}):** " + ", ".join(missing_list))
            cols[1].markdown(f"[Instructions]({row['instructions_link']})")
        st.success("Done!")
else:
    st.info("Select ingredients and press 'Recommend Recipes' to begin.")