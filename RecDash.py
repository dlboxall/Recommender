#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.set_page_config(page_title="Course Recommender", layout="wide")

# --- Hero Section ---
hero_col1, hero_col2, hero_col3 = st.columns([3, 2, 2])

with hero_col1:
    st.markdown("### Why take courses online through Coursera?")
    st.markdown("Coursera offers flexible, affordable access to top-rated university and industry content—anytime, anywhere.")

with hero_col2:
    st.markdown("#### If you're new to Coursera")
    st.button("Start Here!", key="new_user")

with hero_col3:
    st.markdown("#### If you're a returning Coursera student")
    st.button("Start Here!", key="returning_user")

st.markdown("---")

# --- Interactive Section: Cold Start / Word Cloud ---
middle_col1, middle_col2 = st.columns(2)

with middle_col1:
    st.markdown("#### Explore Your Interests")
    interests = st.multiselect(
        "Select topics you’re interested in:",
        ["Data Science", "Python", "AI", "Web Development", "Business", "Design", "Cloud", "Cybersecurity"]
    )

with middle_col2:
    st.markdown("#### Input Past Course Experience")
    taken_courses = st.text_input("Enter previously taken courses (comma-separated):")
    favorites = st.text_input("Top 3 favorite courses:")

st.markdown("---")

# --- Recommended Courses Section ---
st.markdown("## Recommended Courses")

filter_col1, filter_col2 = st.columns([3, 2])

with filter_col1:
    selected_genres = st.multiselect("Filter by genre:", ["Data Science", "Python", "Business", "AI", "Cloud", "Design"])

with filter_col2:
    exclude_terms = st.text_input("Exclude courses containing:")

# Placeholder for recommendations (replace with dynamic logic later)
st.write("Showing personalized recommendations based on your inputs...")
st.success("✔️ Placeholder: Recommended Course 1")
st.success("✔️ Placeholder: Recommended Course 2")
st.success("✔️ Placeholder: Recommended Course 3")

