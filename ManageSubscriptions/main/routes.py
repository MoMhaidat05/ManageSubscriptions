from flask import Blueprint
from flask import render_template,url_for,flash,redirect,request,abort
from ManageSubscriptions import db,limiter
from flask_login import current_user

main_bp = Blueprint('main', __name__)

@main_bp.route("/",methods=['GET'])
@main_bp.route("/home",methods=['GET'])
def index():
    return render_template('home.html',title='Subly - Manage subscriptions easily')

@main_bp.route('/pricing', methods=["GET","POST"])
@limiter.limit("5 per 10 minutes", methods=["POST"])
def pricing():
    return render_template('pricing.html', title='Subly - Pricing')

@main_bp.route('/about', methods=["GET"])
def about():
    return render_template('about.html', title='Subly - About')

@main_bp.route('/static/error_logs/', defaults={'path': ''})
@main_bp.route('/static/error_logs/<path:path>')
def block_error_logs(path):
    return abort(403)
