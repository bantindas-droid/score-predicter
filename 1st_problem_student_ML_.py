import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "previous_score": [30, 35, 40, 50, 55, 60, 65, 70, 80],
    "final_score": [35, 40, 45, 55, 60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["hours", "previous_score"]]
y = df["final_score"]

model = LinearRegression()
model.fit(X, y)

print("Student Exam Score Predictor Bot")
print("-------------------------------------")

while True:
    try:
        hours = float(input("Enter study hours: "))
        prev_score = float(input("Enter previous exam score: "))

        prediction = model.predict([[hours, prev_score]])
        predicted_score = prediction[0]

        print(f"\nPredicted Final Score: {predicted_score:.2f}")

        if predicted_score >= 45:
            print("Result: PASS\n")
        else:
            print("Result: FAIL\n")

    except ValueError:
        print(" Invalid input! Please enter numbers only.\n")

    choice = input("Do you want to predict again? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting the bot. Good luck!")
        break