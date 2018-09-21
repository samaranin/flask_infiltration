from flask import render_template
from app import app
import numpy as np
import infiltration as inf
import json


@app.route('/')
@app.route('/index')
def index():
    a_ij = inf.calculate_aj()
    c = np.linspace(0, 160, 50)
    t = np.linspace(16, 75, 50)
    tk = np.zeros((50, 50), dtype=float)

    i = 0
    for c_val in c:
        j = 0
        for t_val in t:
            tk[i, j] = inf.tk_ct(a_ij, c_val, t_val)
            j += 1
        i += 1

    return render_template("index.html",
                           x=json.dumps(c.tolist()), y=json.dumps(t.tolist()),  z=json.dumps(tk.transpose().tolist()), height="700")
