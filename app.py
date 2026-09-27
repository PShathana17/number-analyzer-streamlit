import streamlit as st
import random

# ==============================
#       NUMBER ANALYZER
# ==============================

def print_num(n):
    st.write("--- Numbers ---")

    for i in range(1, n + 1):
        st.write(i)


def print_even(n):
    st.write("--- Even Numbers ---")

    for i in range(2, n + 1):
        if i % 2 == 0:
            st.write(i)


def print_odd(n):
    st.write("--- Odd Numbers ---")

    for i in range(1, n + 1):
        if i % 2 == 1:
            st.write(i)


def find_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    st.write("--- Sum ---")
    st.write("Total =", total)


def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


def check_prime(n):
    is_prime = True

    if n < 2:
        is_prime = False

    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

    if is_prime:
        return "Prime"
    else:
        return "Not Prime"


def multiplication_table(n):
    st.write("--- Multiplication Table ---")

    for i in range(1, 11):
        st.write(n, "x", i, "=", n * i)


def star_pattern(n):
    st.write("--- Star Pattern ---")

    for i in range(1, n + 1):
        stars = ""

        for j in range(i):
            stars += "* "

        st.text(stars)


# ==============================
#       NUMBER GAME
# ==============================

def number_game():

    st.subheader("🎮 Number Challenge")

    # ------------------------------
    # GAME VARIABLES
    # ------------------------------

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "lives" not in st.session_state:
        st.session_state.lives = 3

    if "game_round" not in st.session_state:
        st.session_state.game_round = 1

    if "game_stage" not in st.session_state:
        st.session_state.game_stage = "even"

    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 50)

    # ------------------------------
    # GAME OVER
    # ------------------------------

    if st.session_state.lives == 0:

        st.error("💀 GAME OVER")

        st.write("🏆 Final Score:", st.session_state.score)

        if st.session_state.score >= 40:
            st.success("🌟 Excellent! Number Master!")

        elif st.session_state.score >= 20:
            st.info("👏 Good Job!")

        else:
            st.warning("💪 Keep Practicing!")

        if st.button("🔄 Restart Game"):

            st.session_state.score = 0
            st.session_state.lives = 3
            st.session_state.game_round = 1
            st.session_state.game_stage = "even"
            st.session_state.number = random.randint(1, 50)

            st.rerun()

        return

    # ------------------------------
    # SCORE & LIVES
    # ------------------------------

    st.write("🏆 Score:", st.session_state.score)
    st.write("❤️ Lives:", st.session_state.lives)

    # ==================================================
    # ROUND 1 - EVEN / ODD
    # ==================================================

    if st.session_state.game_stage == "even":

        st.write("## 🎯 Even / Odd Challenge")

        st.write(
            "Question:",
            st.session_state.game_round,
            "/ 3"
        )

        number = st.session_state.number

        st.write("### Number:", number)

        answer = st.selectbox(
            "Is it even or odd?",
            ["Choose", "Even", "Odd"],
            key=f"even_answer_{st.session_state.game_round}"
        )

        if st.button("Submit Answer"):

            if answer == "Choose":

                st.warning("Please choose an answer.")

            else:

                if number % 2 == 0:
                    correct_answer = "Even"
                else:
                    correct_answer = "Odd"

                if answer == correct_answer:

                    st.success("✅ Correct!")

                    st.session_state.score += 10

                else:

                    st.error("❌ Wrong!")

                    st.write(
                        "Correct answer:",
                        correct_answer
                    )

                    st.session_state.lives -= 1

                # Next question
                if st.session_state.game_round < 3:

                    st.session_state.game_round += 1
                    st.session_state.number = random.randint(1, 50)

                else:

                    # Move to prime challenge
                    st.session_state.game_stage = "prime"
                    st.session_state.game_round = 1
                    st.session_state.number = random.randint(2, 50)

                st.rerun()

    # ==================================================
    # ROUND 2 - PRIME
    # ==================================================

    elif st.session_state.game_stage == "prime":

        st.write("## 🧠 Prime Challenge")

        st.write(
            "Question:",
            st.session_state.game_round,
            "/ 2"
        )

        number = st.session_state.number

        st.write("### Number:", number)

        answer = st.selectbox(
            "Is it prime or not prime?",
            ["Choose", "Prime", "Not Prime"],
            key=f"prime_answer_{st.session_state.game_round}"
        )

        if st.button("Submit Prime Answer"):

            if answer == "Choose":

                st.warning("Please choose an answer.")

            else:

                correct_answer = check_prime(number)

                if answer == correct_answer:

                    st.success("✅ Correct!")

                    st.session_state.score += 10

                else:

                    st.error("❌ Wrong!")

                    st.write(
                        "Correct answer:",
                        correct_answer
                    )

                    st.session_state.lives -= 1

                # Next question
                if st.session_state.game_round < 2:

                    st.session_state.game_round += 1
                    st.session_state.number = random.randint(2, 50)

                else:

                    # Game completed
                    st.session_state.game_stage = "finished"

                st.rerun()

    # ==================================================
    # GAME FINISHED
    # ==================================================

    elif st.session_state.game_stage == "finished":

        st.success("🏆 GAME COMPLETED!")

        st.write(
            "Final Score:",
            st.session_state.score
        )

        st.write(
            "Lives Remaining:",
            st.session_state.lives
        )

        if st.session_state.score >= 40:

            st.success(
                "🌟 Excellent! Number Master!"
            )

        elif st.session_state.score >= 20:

            st.info(
                "👏 Good Job!"
            )

        else:

            st.warning(
                "💪 Keep Practicing!"
            )

        if st.button("🔄 Play Again"):

            st.session_state.score = 0
            st.session_state.lives = 3
            st.session_state.game_round = 1
            st.session_state.game_stage = "even"
            st.session_state.number = random.randint(1, 50)

            st.rerun()

# ==============================
#       STREAMLIT APP
# ==============================

st.title("🔢 Number Analyzer")

st.write("Analyze numbers or play the Number Challenge 🎮")


choice = st.selectbox(
    "Choose an operation",
    [
        "Numbers",
        "Even",
        "Odd",
        "Sum",
        "Factorial",
        "Prime",
        "Table",
        "Pattern",
        "🎮 Game"
    ]
)


# ==============================
#       ANALYZER
# ==============================

if choice != "🎮 Game":

    n = st.number_input(
        "Enter N",
        min_value=1,
        step=1
    )

    if st.button("Run"):

        if choice == "Numbers":
            print_num(n)

        elif choice == "Even":
            print_even(n)

        elif choice == "Odd":
            print_odd(n)

        elif choice == "Sum":
            find_sum(n)

        elif choice == "Factorial":
            st.write("Factorial =", factorial(n))

        elif choice == "Prime":
            st.write("Result:", check_prime(n))

        elif choice == "Table":
            multiplication_table(n)

        elif choice == "Pattern":
            star_pattern(n)


# ==============================
#       GAME
# ==============================

else:

    number_game()