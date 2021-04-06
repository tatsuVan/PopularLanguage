from flask import Flask, render_template
from assets.database import db_session
from assets.models import Data

app = Flask(__name__)

jp_data = db_session.query(Data).filter(Data.country == 'japan').all()[-1]
ca_data = db_session.query(Data).filter(Data.country == 'canada').all()[-1]
us_data = db_session.query(Data).filter(Data.country == 'usa').all()[-1]
au_data = db_session.query(Data).filter(Data.country == 'australia').all()[-1]
sg_data = db_session.query(Data).filter(Data.country == 'singapore').all()[-1]
nz_data = db_session.query(Data).filter(Data.country == 'newzealand').all()[-1]
wr_data = db_session.query(Data).filter(Data.country == 'world').all()[-1]

datas = [jp_data, ca_data, us_data, au_data, sg_data, nz_data]


@app.route('/')
def index():
    return render_template('index.html', datas=datas, wr_data=wr_data)


# server.py
if __name__ == '__main__':
    app.run(debug=False)
