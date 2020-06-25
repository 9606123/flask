# encoding: utf-8
from flask import Flask, session, redirect, url_for, request, render_template, flash
from flask_bootstrap import Bootstrap
from .. import db
from ..models import Blogs
from . import admin


@admin.route('/', defaults={'page':1})
@admin.route('/page/<page>')
def index(page):
    if 'username' in session and session['user']['is_admin']:
        try:
            page = int(page)
            paginate = Blogs.query.paginate(page, 10)
            return render_template('adminlist.html', results = paginate.items, paginate=paginate)
        except Exception as e:
            print(e)
            flash('有错误发生')
            return render_template('adminlist.html')
    else:
        return render_template('adminlist.html')


