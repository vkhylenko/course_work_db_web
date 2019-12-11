from app import app
from app import db
from flask import render_template, url_for, redirect, flash, request
from app.forms import LoginForm, RegForm
from flask_login import logout_user
from flask_login import current_user, login_user
from app.models import User, SkiResort, CategoryCountry, Countries, CurrencyType
from flask_login import login_required
from app.tables import ResultsS, ResultsE, ResultsN, ResultsO, Finder

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/index_log')
def index_log():
    return render_template('index_log.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=''
    if current_user.is_authenticated:
        return redirect(url_for('index_log'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nickname=form.nickname.data).first()
        if user is None or not user.check_password(form.password.data):
            msg = 'Failed! Incorrect nickname or password!'
            flash('Invalid username or password')
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index_log'))
        
    return render_template('login.html', title='Sign In', form=form, msg = msg)

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if current_user.is_authenticated:
        return redirect(url_for('index_log'))
    form = RegForm()
    if form.validate_on_submit():
        user = User(nickname=form.nickname.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('auth.html', title='Registration', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index', _external=True))

@app.route('/europe')
def europe():
    if len(request.args.get('id_', '')) > 0:
        id = int(request.args['id_'])
        res = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id)\
            .add_columns(Countries.country, SkiResort.name, SkiResort.altitude).filter(SkiResort.id == id).all()

        mon = SkiResort.query.join(CurrencyType, SkiResort.currency==CurrencyType.id)\
            .add_columns(SkiResort.adult, SkiResort.youth, SkiResort.child, CurrencyType.currency).filter(SkiResort.id == id).all()

        piste = SkiResort.query.add_columns(SkiResort.easy, SkiResort.intermediate, SkiResort.difficult).filter(SkiResort.id == id).all()

        lifts = SkiResort.query.add_columns(SkiResort.gondola, SkiResort.chairlift, SkiResort.platter).filter(SkiResort.id == id).all()
        
        return render_template('resort_details.html', data = res, curr = mon, piste = piste, lifts = lifts)

    eu = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id).add_columns(SkiResort.id, Countries.country).add_columns(SkiResort.name).add_columns(SkiResort.altitude).filter(CategoryCountry.category == 'Europe').all()
    table = ResultsE(eu)

    return render_template('europe.html', title='Europe',  table = table)


@app.route('/namerica')
def namerica():
    if len(request.args.get('id_', '')) > 0:
        id = int(request.args['id_'])
        res = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id)\
            .add_columns(Countries.country, SkiResort.name, SkiResort.altitude).filter(SkiResort.id == id).all()

        mon = SkiResort.query.join(CurrencyType, SkiResort.currency==CurrencyType.id)\
            .add_columns(SkiResort.adult, SkiResort.youth, SkiResort.child, CurrencyType.currency).filter(SkiResort.id == id).all()

        piste = SkiResort.query.add_columns(SkiResort.easy, SkiResort.intermediate, SkiResort.difficult).filter(SkiResort.id == id).all()

        lifts = SkiResort.query.add_columns(SkiResort.gondola, SkiResort.chairlift, SkiResort.platter).filter(SkiResort.id == id).all()
        
        return render_template('resort_details.html', data = res, curr = mon, piste = piste, lifts = lifts)
    na = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id).add_columns(SkiResort.id, Countries.country).add_columns(SkiResort.name).add_columns(SkiResort.altitude).filter(CategoryCountry.category == 'North America').all()
    sort = request.args.get('sort', '', type=str)
    table = ResultsN(na)
    return render_template('namerica.html', title='North America', table = table)

@app.route('/samerica')
def samerica():
    if len(request.args.get('id_', '')) > 0:
        id = int(request.args['id_'])
        res = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id)\
            .add_columns(Countries.country, SkiResort.name, SkiResort.altitude).filter(SkiResort.id == id).all()

        mon = SkiResort.query.join(CurrencyType, SkiResort.currency==CurrencyType.id)\
            .add_columns(SkiResort.adult, SkiResort.youth, SkiResort.child, CurrencyType.currency).filter(SkiResort.id == id).all()

        piste = SkiResort.query.add_columns(SkiResort.easy, SkiResort.intermediate, SkiResort.difficult).filter(SkiResort.id == id).all()

        lifts = SkiResort.query.add_columns(SkiResort.gondola, SkiResort.chairlift, SkiResort.platter).filter(SkiResort.id == id).all()
        
        return render_template('resort_details.html', data = res, curr = mon, piste = piste, lifts = lifts)
    sa = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id).add_columns(SkiResort.id, Countries.country).add_columns(SkiResort.name).add_columns(SkiResort.altitude).filter(CategoryCountry.category == 'South America').all()
    table = ResultsS(sa)
    return render_template('samerica.html', title='South America', table = table)

@app.route('/othworld')
def othworld():
    if len(request.args.get('id_', '')) > 0:
        id = int(request.args['id_'])
        res = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id)\
            .add_columns(Countries.country, SkiResort.name, SkiResort.altitude).filter(SkiResort.id == id).all()

        mon = SkiResort.query.join(CurrencyType, SkiResort.currency==CurrencyType.id)\
            .add_columns(SkiResort.adult, SkiResort.youth, SkiResort.child, CurrencyType.currency).filter(SkiResort.id == id).all()

        piste = SkiResort.query.add_columns(SkiResort.easy, SkiResort.intermediate, SkiResort.difficult).filter(SkiResort.id == id).all()

        lifts = SkiResort.query.add_columns(SkiResort.gondola, SkiResort.chairlift, SkiResort.platter).filter(SkiResort.id == id).all()
        
        return render_template('resort_details.html', data = res, curr = mon, piste = piste, lifts = lifts)
    ow = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id).add_columns(SkiResort.id, Countries.country).add_columns(SkiResort.name).add_columns(SkiResort.altitude).filter(CategoryCountry.category == 'Other World').all()
    table = ResultsO(ow)
    return render_template('othworld.html', title='Other World', table = table)



@app.route('/finder')
def finder():
    return render_template('finder.html', title='Resorts Finder')


@app.route('/finder/finder_res', methods=['GET', 'POST'])
def finder_res():
    if len(request.args.get('id_', '')) > 0:
        id = int(request.args['id_'])
        res = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id)\
            .add_columns(Countries.country, SkiResort.name, SkiResort.altitude).filter(SkiResort.id == id).all()

        mon = SkiResort.query.join(CurrencyType, SkiResort.currency==CurrencyType.id)\
            .add_columns(SkiResort.adult, SkiResort.youth, SkiResort.child, CurrencyType.currency).filter(SkiResort.id == id).all()

        piste = SkiResort.query.add_columns(SkiResort.easy, SkiResort.intermediate, SkiResort.difficult).filter(SkiResort.id == id).all()

        lifts = SkiResort.query.add_columns(SkiResort.gondola, SkiResort.chairlift, SkiResort.platter).filter(SkiResort.id == id).all()
        
        return render_template('resort_details.html', data = res, curr = mon, piste = piste, lifts = lifts)
    
    if request.method == 'POST':
        selectc = request.form.get('category')
        selecta = request.form.get('altitude')
        selecth = request.form.get('hardness')
        if (selecth == 'exp'):
            res = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id).add_columns(SkiResort.easy, SkiResort.intermediate, SkiResort.difficult).add_columns(SkiResort.id, Countries.country, SkiResort.name, SkiResort.altitude)\
                .filter(CategoryCountry.category == selectc).filter(SkiResort.altitude > selecta).filter(SkiResort.difficult - SkiResort.easy > 0).all()
        elif (selecth == 'beg'):
            res = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id).add_columns(SkiResort.easy, SkiResort.intermediate, SkiResort.difficult).add_columns(SkiResort.id, Countries.country, SkiResort.name, SkiResort.altitude)\
                .filter(CategoryCountry.category == selectc).filter(SkiResort.altitude > selecta).filter(SkiResort.difficult - SkiResort.easy < 0).all()
        else:
            res = SkiResort.query.join(Countries, SkiResort.country_category==Countries.id).join(CategoryCountry, Countries.category_id==CategoryCountry.id).add_columns(SkiResort.id, Countries.country, SkiResort.name, SkiResort.altitude)\
                .filter(CategoryCountry.category == selectc).filter(SkiResort.altitude > selecta).all()
        table = Finder(res)
        return render_template('finder.html', title='For You!', table = table )



