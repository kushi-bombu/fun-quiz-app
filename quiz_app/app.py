import streamlit as st

# Quiz questions
questions = [
    {
        "question": "Which country has more sheep than people?",
        "options": ["Australia", "India", "New Zealand", "Canada"],
        "answer": "New Zealand"
    },
    {
        "question": "Which part of the body never grows after birth?",
        "options": ["Nose", "Eyes", "Legs", "Ears"],
        "answer": "Eyes"
    },
    {
        "question": "Which fruit floats in water because it's 25% air?",
        "options": ["Banana", "Apple", "Mango", "Pear"],
        "answer": "Apple"
    },
    {
        "question": "Which is the only letter not used in any U.S. state name?",
        "options": ["Q", "Z", "X", "J"],
        "answer": "Q"
    },
    {
        "question": "What color is hippo’s sweat?",
        "options": ["Red", "White", "Blue", "Green"],
        "answer": "Red"
    },
    {
        "question": "Which animal can't jump?",
        "options": ["Elephant", "Dog", "Tiger", "Kangaroo"],
        "answer": "Elephant"
    },
    {
        "question": "What is the national animal of Scotland?",
        "options": ["Lion", "Dragon", "Unicorn", "Horse"],
        "answer": "Unicorn"
    },
    {
        "question": "Which bird can fly backward?",
        "options": ["Sparrow", "Crow", "Hummingbird", "Owl"],
        "answer": "Hummingbird"
    },
    {
        "question": "What does a group of crows called?",
        "options": ["Gang", "Herd", "Murder", "Pack"],
        "answer": "Murder"
    },
    {
        "question": "Which planet spins the fastest?",
        "options": ["Earth", "Saturn", "Jupiter", "Mars"],
        "answer": "Jupiter"
    },
    {
        "question": "Which insect has ears on its knees?",
        "options": ["Bee", "Cricket", "Ant", "Mosquito"],
        "answer": "Cricket"
    },
    {
        "question": "What is the fear of long words called?",
        "options": ["Tinyphobia", "Longworditis", "Hippopotomonstrosesquipedaliophobia", "Vocabphobia"],
        "answer": "Hippopotomonstrosesquipedaliophobia"
    },
    {
        "question": "How many noses does a slug have?",
        "options": ["1", "2", "4", "6"],
        "answer": "4"
    },
    {
        "question": "Which animal’s poop is cube-shaped?",
        "options": ["Rabbit", "Koala", "Wombat", "Camel"],
        "answer": "Wombat"
    },
    {
        "question": "Which fish can blink with both eyes separately?",
        "options": ["Tuna", "Shark", "Flounder", "Chameleon Fish"],
        "answer": "Flounder"
    },
    {
        "question": "Which fruit has its seeds on the outside?",
        "options": ["Apple", "Strawberry", "Kiwi", "Papaya"],
        "answer": "Strawberry"
    },
    {
        "question": "How many hearts does an octopus have?",
        "options": ["1", "2", "3", "4"],
        "answer": "3"
    },
    {
        "question": "Which day has the most birthdays in the world?",
        "options": ["January 1", "October 5", "December 25", "August 15"],
        "answer": "October 5"
    },
    {
        "question": "Which animal can sleep for 3 years?",
        "options": ["Bear", "Snail", "Tortoise", "Frog"],
        "answer": "Snail"
    },
    {
        "question": "What is the tiny pocket inside jeans for?",
        "options": ["Money", "Watch", "Nails", "Style"],
        "answer": "Watch"
    }
]

st.set_page_config(page_title="Fun Quiz App", layout="centered")
st.title("🎯 Fun Quiz App")
st.markdown("Test your brain with fun & surprising questions! 🧠")

score = 0

# Display quiz questions
for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}: {q['question']}")
    user_answer = st.radio("Choose your answer:", q['options'], key=f"q_{i}")
    if user_answer == q["answer"]:
        score += 1
st.markdown("---")
st.success(f"✅ You got {score} out of {len(questions)} questions correct!")

# 🎉 Optional final feedback
if score == len(questions):
    st.balloons()
    st.markdown("🎉 Perfect Score! You’re a genius!")
elif score >= 15:
    st.markdown("🔥 Great job! You really know your stuff.")
elif score >= 10:
    st.markdown("👏 Nice try! You got more than half right.")
else:
    st.markdown("😅 Keep learning — you'll get better!")


