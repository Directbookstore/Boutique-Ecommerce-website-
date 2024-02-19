from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

# Define the User model and the structure of the user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



# Wrap relevant parts of your code in the application context
with app.app_context():
    # Create the tables in the database
    db.create_all()
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/cart.html')
    def cart():
        return render_template('cart.html')

    @app.route('/sign-up.html')
    def sign_up():
        return render_template('sign-up.html')

    @app.route('/login.html')
    def login():
        return render_template('login.html')

    @app.route('/login', methods=['POST'])
    def login_post():
        username = request.form.get('username')
        password = request.form.get('password')
        # Perform authentication logic here
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # If authentication succeeds, redirect to dashboard
            return redirect(url_for('dashboard'))
        else:
            # If authentication fails, show login page with error
            return render_template('login.html', error='Invalid username or password')

    @app.route('/dashboard')
    def dashboard():
        # Render dashboard template
        return render_template('dashboard.html')

    @app.route('/signup', methods=['POST'])
    def signup():
        username = request.form.get('username')
        password = request.form.get('password')
        # Create a new user
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return 'User created successfully!'

if __name__ == '__main__':
    app.run(debug=True)


