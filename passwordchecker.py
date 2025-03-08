import streamlit as st
import re

# Streamlit Page Title
st.title("🔐 Password Strength Meter")

# Function to Check Password Strength
def check_password(password):
    score = 0
    feedback = []  # Store feedback messages

    # At least 8 characters
    if len(password) < 8:
        feedback.append("❌ Password should be at least 8 characters long.")
    else:
        score += 1

    # Contains both uppercase and lowercase letters
    if not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        feedback.append("❌ Include both uppercase and lowercase letters.")
    else:
        score += 1

    # Contains at least one digit
    if not re.search(r"\d", password):
        feedback.append("❌ Add at least one number (0-9).")
    else:
        score += 1

    # Contains at least one special character
    if not re.search(r"[!@#$%^&*]", password):
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    else:
        score += 1

    # Strength Evaluation
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")

    # Display Feedback
    if feedback:
        st.write("### Suggestions:")
        for msg in feedback:
            st.write(msg)

# Take Input from User in Browser
password = st.text_input("Enter your password:", type="password")

# Check password **ONLY** when user enters something
if password:
    check_password(password)
