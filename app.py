from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simpan username dan password yang valid 
valid_users = {
    'user1': '123',
    'user2': '123',
    'admin': '123'
}

# Route untuk halaman login
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Periksa username dan password dalam valid_users
        if username in valid_users and valid_users[username] == password:
            return redirect(url_for('success'))
        else:
            return "Login gagal. Username atau password salah."

    return render_template('index.html')

# Route untuk halaman sukses
@app.route('/success')
def success():
    return "Login berhasil! Selamat datang."

if __name__ == '__main__':
    app.run(debug=True)
