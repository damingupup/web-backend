from flask import Flask, redirect, url_for, render_template, request, session
from flask import Blueprint, abort
import json
import forms
import helpers

merchant_show = Blueprint('merchant_show', __name__,
                        template_folder='templates')

@register_user.route('/merchants', methods=['GET', 'POST'])
def merchants():
    if session.get('logged_in'):
    	print("show merchants")
    return redirect(url_for('auth.login'))

@bp.route('/merchants/<int:id>/registration-info', methods=('GET', 'POST'))
def get_registration(id):
    """Update a post if the current user is the author."""
    if request.method == 'GET':
    	print("show merchants")
    return redirect(url_for('auth.login'))
