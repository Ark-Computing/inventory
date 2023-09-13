from flask import Blueprint, render_template

client_bp = Blueprint('client', __name__)

@client_bp.route('/')
def home():
    return render_template('dash.html', title="Dashboard")

@client_bp.route('/report')
def report():
    return render_template('report.html', title="Report")
