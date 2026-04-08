from flask import Flask, render_template, request,redirect
import pickle
import os
users=[]
app = Flask(__name__)

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR,'fake_job_model.pkl'), 'rb'))
vectorizer = pickle.load(open(os.path.join(BASE_DIR'vectorizer.pkl'), 'rb'))


#signup
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "POST":

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Passwords do not match"

        users.append({
            "username": username,
            "email": email,
            "password": password
        })

        return redirect('/login')
    return render_template('signup.html')    


    
# Home / Index
@app.route('/')
def index():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        for user in users:
            if user['email'] == email and user['password'] == password:
                return redirect('/home')

        return "Invalid credentials"

    return render_template('login.html')


# Home after login
@app.route('/home')
def home():
    return render_template('homepage.html')

# Detect page (Analyze job)
@app.route('/detect')
def detect():
    return render_template('detect.html')

# Prediction (MAIN LOGIC)
@app.route('/predict', methods=['POST'])
def predict():
    job_desc = request.form['job_description'].lower()
    if job_desc == ' ':
        return render_template('detect.html',prediction="Please enter job description")
    if model is None or vectorizer is None:
        return render_template('detect.html',prediction="Model not loaded properly")    
                          

    input_data = vectorizer.transform([job_desc])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "⚠️ Fake Job Posting"
    else:
        result = "✅ Real Job Posting"

    return render_template('detect.html', prediction=result)

    



# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port,debug=False)