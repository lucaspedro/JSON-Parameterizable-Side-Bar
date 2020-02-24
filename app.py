from flask import Flask, render_template
import os
import json
from flask import Markup


app = Flask(__name__, static_folder="static", template_folder="templates")

####################################################################
####################################################################

# Here you can change the configuration json file:

file_json_menu = "menu_json.json"

# Just place the well-formatted file in the / static / data folder and change its name here.

####################################################################
####################################################################

def rec_gen_lines(curr_node, node_len, level):
    ret = ""
    for i in range(node_len):
        title = curr_node[i]["title"]
        icon = curr_node[i]["icon"]
    
        try:
            aux = curr_node[i]["child"]
            ret += render_template('line_renderer.html', title=title, icon=icon, has_child=True, node_pos=(i+1), node_len=node_len, level=level)
            ret_child = rec_gen_lines(curr_node[i]["child"], len(curr_node[i]["child"]), level+1)

        except:
            ret += render_template('line_renderer.html', title=title, icon=icon, has_child=False, node_pos=(i+1), node_len=node_len, level=level)
            ret_child = ""


        ret = ret + ret_child
        if (i + 1) == node_len:
            ret += "</ul></li>"

    return str(ret)

def tmpl_show_menu():

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", file_json_menu)
    jsonObject = json.load(open(json_url))

    ret = ""
    for key in jsonObject:      ##removing menu tag
        value = jsonObject[key]

    lines = Markup(rec_gen_lines(value, len(value), 0))
    #flash(lines)
    return  render_template('nav.html', lines=lines)

@app.route("/")
@app.route('/home')
def home():
    ret = render_template('header.html')
    ret += tmpl_show_menu()
    ret += render_template('index.html', title="Home")

    return ret

@app.route('/<name>')
def hello_name(name):
    return render_template('404.html', title=format(name))

if __name__ == '__main__':
    app.run(debug=True)