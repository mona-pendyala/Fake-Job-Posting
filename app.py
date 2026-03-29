from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
#model = pickle.load(open('fake_job_model.pkl', 'rb'))
#vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Home / Index
@app.route('/')
def index():
    return render_template('index.html')

# Login page
@app.route('/login')
def login():
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

    # Rule-based check
    if "fee" in job_desc or "whatsapp" in job_desc or "earn money" in job_desc:
        result = "⚠ Fake Job Posting"
    
        
    else:
         result = "✅ Real Job Posting"

    return render_template('detect.html', prediction=result)

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port,debug=False)