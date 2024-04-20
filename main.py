from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

User_Email = ""
# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Dis_Project"
)

cursor = db.cursor()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

# Validate login credentials and redirect to appropriate dashboard
@app.route('/login', methods=['POST'])
def login():
    global User_Email
    email = request.form['email']
    password = request.form['password']

    # Check if user exists and credentials are correct
    query = "SELECT Position FROM Employees WHERE Email = %s AND Password = %s"
    cursor.execute(query, (email, password))
    position = cursor.fetchone()

    if position:
        User_Email = email
        # Check position of the employee and redirect to the appropriate dashboard
        if position[0] == 'Manager':
            return redirect(url_for('manager_dashboard'))
        elif position[0] == 'employee':
            return redirect(url_for('employee_dashboard'))
    
        
    else:
        # If user credentials are incorrect, render the login form again
        return render_template('login.html', message="Invalid credentials")



@app.route('/signout')
def signout():
    global User_Email
    User_Email = ""
    return redirect(url_for('login'))

# Manager dashboard route
# Manager dashboard route
@app.route('/manager/dashboard')
def manager_dashboard():
    if User_Email:
        # Fetch user data from the Employees table
        user_query = "SELECT FirstName, LastName,Position FROM Employees WHERE Email = %s"
        cursor.execute(user_query, (User_Email,))
        user_data = cursor.fetchone()
        cursor.execute("SELECT * FROM customers")
        dataCustomers = cursor.fetchall()
        cursor.execute("Select * from employees")
        dataEmployees = cursor.fetchall()
        cursor.execute("Select * from transactions")
        dataTransactions = cursor.fetchall()
        cursor.execute("Select * from products")
        dataProducts = cursor.fetchall()
        cursor.execute("Select * from suppliers")
        dataSuppliers = cursor.fetchall()
        # cursor.execute("Select * from inventory")
        # dataEmployees = cursor.fetchall()



        if user_data:
            user_name = f"{user_data[0]} {user_data[1]} "
            position = f"{user_data[2]}"
            return render_template('manager_dashboard.html', user_name=user_name,position=position,dataCustomers=dataCustomers,dataEmployees=dataEmployees,dataProducts=dataProducts,dataTransactions=dataTransactions,dataSuppliers=dataSuppliers)
    
    return render_template('login.html')


# Employee dashboard route
@app.route('/employee/dashboard')
def employee_dashboard():
    if User_Email:
        # Fetch user data from the Employees table
        user_query = "SELECT FirstName, LastName, Department FROM employees WHERE Email = %s"
        cursor.execute(user_query, (User_Email,))
        user_data = cursor.fetchone()

        if user_data:
            department = user_data[2]
            if department == 'Production':
                return redirect(url_for('production_dashboard'))
            elif department == 'Finance':
                return redirect(url_for('finance_dashboard'))
            elif department == 'Sales':
                return redirect(url_for('sales_dashboard'))
            elif department == 'HR':
                return redirect(url_for('hr_dashboard'))

    return render_template('login.html')

# Production department dashboard route
@app.route('/production/dashboard')
def production_dashboard():
    return render_template('production_dashboard.html')

# Finance department dashboard route
@app.route('/finance/dashboard')
def finance_dashboard():
    return render_template('finance_dashboard.html')

# Sales department dashboard route
@app.route('/sales/dashboard')
def sales_dashboard():
    return render_template('sales_dashboard.html')

# HR department dashboard route
@app.route('/hr/dashboard')
def hr_dashboard():
    return render_template('hr_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
