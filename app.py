from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy Data Testing ke liye
customers = [
    {
        "id": 1,
        "name": "Ali Raza",
        "phone": "03001234567",
        "ip": "192.168.1.10",
        "package": "10 Mbps - Fiber",
        "fee": 2000,
        "status": "Active",
        "expiry": "2026-10-31"
    }
]

@app.route('/')
def dashboard():
    total_users = len(customers)
    active_users = sum(1 for c in customers if c['status'] == 'Active')
    expired_users = sum(1 for c in customers if c['status'] == 'Expired')
    total_revenue = sum(c['fee'] for c in customers if c['status'] == 'Active')

    return render_template('index.html', 
                           customers=customers, 
                           total=total_users, 
                           active=active_users, 
                           expired=expired_users, 
                           revenue=total_revenue)

@app.route('/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        new_customer = {
            "id": len(customers) + 1,
            "name": request.form['name'],
            "phone": request.form['phone'],
            "ip": request.form['ip'],
            "package": request.form['package'],
            "fee": int(request.form['fee']),
            "status": "Active",
            "expiry": request.form['expiry']
        }
        customers.append(new_customer)
        return redirect(url_for('dashboard'))
    return render_template('add_customer.html')

if __name__ == '__main__':
    app.run(debug=True)