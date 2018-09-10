from app import app
import numpy as np
import infiltration as inf


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

    return(
        '''
            <html>
                <head>
                    <title>Home Page - Infiltration visualization</title>
                </head>
                <body>
                    <h1>''' + str(tk) + '''</h1>
                </body>
            </html>
        '''
    )
