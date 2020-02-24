# JSON Parameterizable Side Bar

This is an implementation of a parameterizable side bar, where the menu items are defined by a JSON configuration file. Through this file the algorithm defines a hierarchical menu, where there are nested items. This challenge is a recursive problem, it was implemented using the Flask framework written in Python and based on the WSGI Werkzeug library and the Jinja2 library. The implemented side bar also involved the use of WEB languages such as CSS and HTML, in addition to the use of the Bootstrap toolkit for layout construction.

# Configuration

The implementation includes packages bellow:
* Flask
* os
* json


To install the necessary packages just follow the steps below:

```
# Install Flask Python package
$ pip install Flask

# Install OS Python package
$ pip install os

# Install JSON Python package
$ pip install json
```

# Recursive Implementation

The main challenge of the implementation is in the nature of the distribution of information within a JSON structure. This type of data structure carries nested information, which is perfect for representing a side bar menu like this. However, to work with this hierarchy model, it is necessary to implement it in a recursive way, in order to map the menu buttons. It was an interesting challenge to carry out this implementation, I hope that the company's opportunities also involve challenges of this caliber.



The main function that performs the recursive mapping of the menu buttons is shown below:
```

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
```


# How to Use

To change the configuration file, just place it in the correct file folder (/ static / data), then change its name in the main file "app.py", as shown in the following excerpt:

```
####################################################################

# Here you can change the configuration json file:

file_json_menu = "menu_json.json"

# Just place the well-formatted file in the / static / data folder and change its name here.

####################################################################
```

The JSON configuration file must follow the following pattern defined to work correctly:

```
{
	"menu":
	[
		{
			"title": "Dashboards",
			"icon": "view_quilt",
			"child":
			[
				{
					"title": "Wind",
					"icon": "stop",
					"child":
					[
						{
							"title": "STC",
							"routeName": "dashboards",
							"icon": "pie_chart"
						}
					]
				}
			]
		}
	]
}
```
# Comments

The proposed implementation involved the use of a CSV file to generate the JSON of the configuration, however this data structure is not viable to represent this type of information, which makes the protocol to represent this information complex. Because of this, only the input with JSON  file was worked to generate the Layout.

# Demonstration

Next, a video shows the final result of the implementation, where two proposals for menu configurations were tested, the first being a small version of only 3 levels and the second already bringing a multi-level json file creating a much larger menu.

https://youtu.be/lIvNWc1xGvk
