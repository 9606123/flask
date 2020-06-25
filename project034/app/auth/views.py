# encoding: utf-8
from flask import Flask, session, redirect, url_for, request, render_template, flash
from flask_bootstrap import Bootstrap
from .. import db
from ..models import User
from . import account

# 用户登录
@account.route('/login', methods=['POST'])
def login():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']

      try:
         user = User.query.filter_by(username = username).first()
         if user is not None and user.verify_password(password):
            session['user'] = user.to_json()
            session['username'] = username
            flash('你好 {}, 欢迎来到xx系统!'.format(username),'success')
            return redirect(url_for('blogs.index'))
         else:
            flash('用户名和密码不匹配，请检查后重试!', 'danger')
            return redirect(url_for('blogs.index'))
      except Exception as e:
         print('exception - {}'.format(str(e)))
         flash('登录异常，请稍后再试!','danger')
         return redirect(url_for('blogs.index'))
   else:
      return redirect(url_for('blogs.index'))
      
# 用户注册
@account.route('/register', methods=['POST'])
def register():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      password2 = request.form['password2']
      first_name = request.form['first_name']
      last_name = request.form['last_name']

      if password != password2:
         flash('两次输入的密码不匹配，请检查后重试!','danger')
         return redirect(url_for('blogs.index'))

      try: 
         user = User.query.filter_by(username = username).first()
         if user:
            flash('用户名 {} 已经存在，请更换用户名！'.format(username),'danger')
            return redirect(url_for('blogs.index'))
         else:
            user = User(username=username,
                           password=password,
                           first_name=first_name,
                           last_name=last_name)
            db.session.add(user)
            db.session.commit()
            session['user'] = user.to_json()
            session['username'] = username
            flash('账户创建成功，欢迎 {}!'.format(username),'success')
            return redirect(url_for('blogs.index'))
      except Exception as e:
         print('exception - {}'.format(str(e)))
         flash('有异常发生，请稍后再试!','danger')
         return redirect(url_for('blogs.index'))

#用户登出，在session中清除用户名
@account.route('/logout')
def logout():
   session.pop('user', None)
   session.pop('username', None)
   return redirect(url_for('blogs.index'))
