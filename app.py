from flask import Flask, url_for, render_template, redirect, request, flash
from forms import ContactForm
from calculator import CalcRib, CalcSpouse, CalcWidow, DualAB, CalcDwb
import jinja2

env = jinja2.Environment()
env.globals.update(zip=zip)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'trialcomp'


@app.route('/')
def my_home():
    form = ContactForm()
    return render_template('index.html', form=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    bics = request.args.get('type_comp')
    prot_ques = request.args.get('prot_date')
    prot_month = request.args.get('prot_month')
    month_selected = int(request.args.get('month'))
    day_selected = int(request.args.get('day'))
    year_selected = int(request.args.get('year'))

    if bics == "a":
        title = 'Retirement MBA'
        rib_pia = request.args.get('rib_pia')
        rib_benefits = CalcRib(rib_pia, month_selected, day_selected, year_selected, prot_month, prot_ques)
        calc_selected = rib_benefits.calc_benefits()
        num_of_rf = int(rib_benefits.calc_rf())
        month_and_year = rib_benefits.month_year()
        max_drcs, current_drcs = rib_benefits.calc_drcs()
        month_year_drcs, message = rib_benefits.drc_months()
        drcs_mba_calculated = rib_benefits.calc_mba_drcs()
        return render_template('results.html', calc_selected=calc_selected, month_and_year=month_and_year, bics=bics,
                               title=title, num_of_rf=num_of_rf, month_selected=month_selected,
                               year_selected=year_selected, zip=zip, max_drcs=max_drcs, drcs_mba_calculated=drcs_mba_calculated, month_year_drcs=month_year_drcs, message=message)

    elif bics == "b":
        title = 'Spouse MBA'
        spo_pia = request.args.get('spouse_nh_pia')
        spouse_benefits = CalcSpouse(spo_pia, month_selected, day_selected, year_selected, prot_month, prot_ques)
        calc_selected = spouse_benefits.calc_benefits_b()
        num_of_rf = spouse_benefits.calc_rf()
        month_and_year = spouse_benefits.month_year()
        return render_template('results.html', calc_selected=calc_selected, month_and_year=month_and_year, bics=bics,
                               title=title, num_of_rf=num_of_rf, month_selected=month_selected,
                               year_selected=year_selected, zip=zip)
    elif bics == "d":
        title = 'Widows MBA'
        widow_pia = request.args.get('deceased_nh_pia')
        dnh_rib = request.args.get('reduced_nh_mba')
        riblim = request.args.get('rib_lim')
        gp_ques = request.args.get('gp_ques')
        gp_amt = request.args.get('gp_amt')
        widows_benefits = CalcWidow(widow_pia, month_selected, day_selected, year_selected, gp_amt, riblim, dnh_rib,
                                    prot_month)
        num_of_rf, max_rf = widows_benefits.calc_rf_d()
        month_and_year = widows_benefits.month_year()

        if gp_ques == "y":
            calc_selected = widows_benefits.wib_with_gpo()
        else:
            calc_selected = widows_benefits.calc_benefits_d()

        return render_template('results.html', calc_selected=calc_selected, month_and_year=month_and_year, bics=bics,
                               title=title, num_of_rf=num_of_rf, month_selected=month_selected,
                               year_selected=year_selected, zip=zip)

    elif bics == "dual_ab":
        title = 'RIB MBA'
        rib_pia = request.args.get('rib_pia')
        spo_pia = request.args.get('spouse_nh_pia')
        dual_entitlement = DualAB(spo_pia, rib_pia, month_selected, day_selected, year_selected, prot_month, prot_ques)
        rib_calc, portion, spo_calc = dual_entitlement.calc_benefits_spouse_portion()
        num_of_rf = dual_entitlement.calc_rf()
        month_and_year = dual_entitlement.month_year()
        if float(rib_pia) < float(spo_pia) / 2:
            return render_template('results.html', rib_calc=rib_calc, portion=portion, spo_calc=spo_calc, month_and_year=month_and_year, bics=bics, title=title, num_of_rf=num_of_rf, month_selected=month_selected, year_selected=year_selected, zip=zip)
        # return render_template('nothing')
    elif bics == "w":
        widow_pia = request.args.get('deceased_nh_pia')
        gp_ques = request.args.get('gp_ques')
        gp_amt = request.args.get('gp_amt')
        dwb = CalcDwb(widow_pia, month_selected, day_selected, year_selected, gp_amt)

        if gp_ques == "y":
            calc_selected = dwb.dwb_with_gpo()
        else:
            calc_selected = dwb.calc_benefits_w()

        return render_template('results.html', calc_selected=calc_selected,
                               bics=bics, month_selected=month_selected,
                               year_selected=year_selected,
                               zip=zip)
    else:
        return render_template('index.html')




