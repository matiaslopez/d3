import json

G, Y, R = [x for x in xrange(3)]

letters = {
    R: {"letter": "R", "string": "Red", "col_string": "red_score", "node_value": []},
    Y: {"letter": "Y", "string": "Yellow", "col_string": "yellow_score", "node_value": []},
    G: {"letter": "G", "string": "Green", "col_string": "green_score", "node_value": []},
}


import csv
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    children = {}
    for row in reader:
        children[row["CASO"]] = {}
        vals = [ (int(k.split("_")[1]),int(v)) for k,v in row.iteritems() if k[0:4]=="TOMA" ]
        # children[row["CASO"]]["values"] = { (k,v) for k,v in row.iteritems()       }
        children[row["CASO"]]["values"] = [v for k,v in sorted(vals)]
        children[row["CASO"]]["node_value"] = []
        children[row["CASO"]]["name"] = row["CASO"]


if True:
    # for i, k in enumerate(small_pop):
        # children[i+1] = {"name": "S{:03}".format(i+1), "values": k[1], "node_value": [], "household": k[0]}

    nodes = []
    links = []

    nodes.append({"node": 0, "name": "Population", "id": "any_score"})

    for k in sorted(letters.keys()):
        letters[k]["node_value"].append(len(nodes))
        nodes.append({"node": len(nodes), "name": "Initial {}".format(letters[k]["string"]), "id": letters[k]["col_string"]})
        letters[k]["node_value"].append(len(nodes))
        nodes.append({"node": len(nodes), "name": "Final {}".format(letters[k]["string"]), "id": letters[k]["col_string"]})

    trials_range = range(len(children.itervalues().next()["values"]))
    for trial_n in trials_range:
        base_line = len(nodes)
        # ord_list = sorted([(k,v) for k,v in children.iteritems()], key=(lambda x: x[1]["values"][trial_n]), reverse=True)
        ord_list = sorted([(k,v) for k,v in children.iteritems()], key=(lambda x: x[1]["values"][trial_n]))

        for i, (child_id, vals) in enumerate(ord_list):
            # {"node": 1, "name": "Subject 1", "id": "yellow_score", "id_old": "hour_score"},
            children[child_id]["node_value"].append(len(nodes))
            nodes.append({"node": len(nodes), "name": "{}-T{}".format(vals["name"], trial_n + 1),
                     "id": letters[vals["values"][trial_n]]["col_string"]})


    for k in sorted(letters.keys()):
        links.append({"source": 0, "target": letters[k]["node_value"][0], "value": 0.5})

    for child_id, vals in children.iteritems():
        # {"source": 0, "target": 2, "value": 0.04},
        links.append({"source": letters[vals["values"][0]]["node_value"][0],
                    "target": vals["node_value"][0], "value": 0.04})
        # links.append({"source": letters[vals["household"]]["node_value"][0],
                    # "target": vals["node_value"][0], "value": 0.04})
        for trial_n in trials_range[:-1]:
            links.append({"source": vals["node_value"][trial_n],
                        "target": vals["node_value"][trial_n+1], "value": 0.04})

        links.append({"source": vals["node_value"][trials_range[-1]],
            "target": letters[vals["values"][trials_range[-1]]]["node_value"][1], "value": 0.04})

    res = {"nodes": nodes, "links": links, "subjects": len(children)}
    print json.dumps(res)

