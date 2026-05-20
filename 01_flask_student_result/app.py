from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        subject1 = int(request.form["subject1"])
        subject2 = int(request.form["subject2"])
        subject3 = int(request.form["subject3"])

        total = subject1 + subject2 + subject3
        percentage = total / 3

        if subject1 >= 35 and subject2 >= 35 and subject3 >= 35:
            status = "Pass"
        else:
            status = "Fail"

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 45:
            grade = "C"
        elif percentage >= 35:
            grade = "D"
        else:
            grade = "F"

        result = {
            "name": name,
            "subject1": subject1,
            "subject2": subject2,
            "subject3": subject3,
            "total": total,
            "percentage": round(percentage, 2),
            "status": status,
            "grade": grade
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)