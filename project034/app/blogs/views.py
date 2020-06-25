# encoding: utf-8
from flask import Flask, session, redirect, url_for, request, render_template, flash
from flask_bootstrap import Bootstrap
from .. import db
from ..models import User,Blogs
import math
from . import blogs


@blogs.route('/', defaults={'page':1})
@blogs.route('/page/<int:page>')
def index(page):
    try:
        paginate = None
        if 'username' in session:
            records = Blogs.query.filter_by(author=session['username'])
        else:
            records = Blogs.query
        if request.args.get('category') and records:
            category=request.args.get('category')
            print(category)
            records = records.filter_by(category=category)
        paginate = records.paginate(page, 5)
        return render_template('index.html', results = paginate.items, paginate=paginate)
    except Exception as e:
        print(e)
        flash('有错误发生')
        return render_template('index.html', results = [])

@blogs.route('/blogs/detail/<id>')
def detail(id):
    try:
        blog = Blogs.query.get_or_404(id)
        db.session.commit()
        return render_template('blogdetail.html', result = blog)
    except Exception as e:
        print(e)
        flash('有错误发生')
        return render_template('index.html', results = [])

#增删改查
@blogs.route('/blogs/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        try: 
            subject = request.form['subject']
            content = request.form['content']
            category = request.form['category']
        
            blog = Blogs.query.filter_by(subject=subject).first()
            if blog:
                flash('已有同名博客 {} 已经存在！'.format(subject),'danger')
                return redirect(url_for('blogs.index'))
            else:
                blog = Blogs(subject=subject,
                            content=content,
                            category=category,
                            author=session['username'])
                db.session.add(blog)
                db.session.commit()
                flash('博客创建成功!','success')
                return redirect(url_for('blogs.index'))
        except Exception as e:
            print('exception - {}'.format(str(e)))
            flash('有异常发生，请稍后再试!','danger')
            return redirect(url_for('blogs.index'))
    else:
        return render_template('blogs.html', url="/blogs/add", result=[])

@blogs.route('/blogs/delete/<id>', methods=['GET','POST'])
def delete(id):
    try:
        blog = Blogs.query.get_or_404(id)
        db.session.delete(blog)
        db.session.commit()
        flash('删除成功!','success')
        return redirect(url_for('blogs.index'))
    except Exception as e:
        print('exception - {}'.format(str(e)))
        flash('有异常发生，请稍后再试!','danger')
        return redirect(url_for('blogs.index'))
    

@blogs.route('/blogs/edit/<id>', methods=['GET','POST'])
def edit(id):
    blog = Blogs.query.get_or_404(id)
    if request.method == 'POST':
        try: 
            subject = request.form['subject']
            content = request.form['content']
            category = request.form['category']

            blog.subject = subject
            blog.category = category
            blog.content = content
            db.session.commit()

            flash('博客更改成功!','success')
            return redirect(url_for('blogs.index'))
        except Exception as e:
            print('exception - {}'.format(str(e)))
            flash('有异常发生，请稍后再试!','danger')
            return redirect(url_for('blogs.index'))
    else:
        return render_template('blogsedit.html', result=blog)

@blogs.route('/about')
def about():
    return render_template('about.html')