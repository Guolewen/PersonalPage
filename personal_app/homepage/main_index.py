from flask import Flask, redirect, url_for, send_from_directory, Blueprint, request
from flask import render_template
from ..db.conndb import connect2db

blueprint_index = Blueprint('index', __name__, template_folder='templates/homepage', static_folder='static/homepage')

@blueprint_index.route('/', methods=['GET', 'POST'])
def hello_world():

    db = connect2db()
    list_dict = []
    with db.connect() as conn:
        results= conn.execute('SELECT * FROM research')
        for row in results:
            research_id, title, authors, link, highlights, abstract, paperinfo = row
            list_dict.append(dict(research_id=research_id, title=title, authors=eval(authors.replace('null', 'None')),
                                link=link, highlights=eval(highlights), abstract=abstract, paperinfo=paperinfo))

    if request.method == 'POST':
        print("Data Should be Inserted")
        pass

    return render_template('index.html', research_data=list_dict)


@blueprint_index.route('/download_cv', methods=["GET", "POST"])
def download_cv():
    print(blueprint_index.static_folder)
    return send_from_directory(blueprint_index.static_folder, filename='guolewen.pdf')


@blueprint_index.route('/research_paper')
def research_paper():
    return redirect('https://storage.googleapis.com/lewenguo_testbucket/testpdf/Serial%20Position%20Effects%20On%20Stock%20Liquidity.pdf'
                    )
