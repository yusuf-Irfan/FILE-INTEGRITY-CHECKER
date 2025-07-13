from flask import Flask, render_template, request
from integrity_checker import calculate_hash

app = Flask(__name__)

stored_hash = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global stored_hash
    result = None
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file:
            file_hash = calculate_hash(uploaded_file.stream)
            if stored_hash is None:
                stored_hash = file_hash
                result = "✅ Original hash stored. Upload the same file again to check integrity."
            else:
                if file_hash == stored_hash:
                    result = "✅ File is unchanged. Hash matches."
                else:
                    result = "⚠ File has been modified. Hash mismatch detected!"
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)