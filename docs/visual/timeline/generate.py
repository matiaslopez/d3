import json

G, Y, R = [x for x in xrange(3)]

letters = {
    R: {"letter": "R", "string": "Red", "col_string": "red_score", "node_value": []},
    Y: {"letter": "Y", "string": "Yellow", "col_string": "yellow_score", "node_value": []},
    G: {"letter": "G", "string": "Green", "col_string": "green_score", "node_value": []},
}

# run loadChildren.py
# ch = get_children_extended()
# h_filtered = [c for c in ch if c.values['development_value-0'].value > 0 and  c.values['development_value-1'].value > 0 and c.values['development_value-2'].value > 0]
# ####vals = [[v.values['development_value-0'].value,v.values['development_value-1'].value,v.values['development_value-2'].value] for v in h_filtered]
# vals = [[v.values['development_value-0'].value-1,v.values['development_value-1'].value-1,v.values['development_value-2'].value-1] for v in h_filtered]
# vals_dict = {0:[], 1:[], 2: []}
# for k in vals:
#     vals_dict[k[0]].append(k)
# vals_dict
# red_vals = [ inside_v for v in vals_dict.itervalues() for inside_v in v[:8]]


#version with household and temperament as launch stage:
# h_filtered = [c for c in ch if c.values['household_value'].value > 0 and c.values['development_value-0'].value > 0 and  c.values['development_value-1'].value > 0 and c.values['development_value-2'].value > 0]
# ####vals = [[v.values['development_value-0'].value-1,
#               v.values['development_value-1'].value-1,
#               v.values['development_value-2'].value-1,
#               v.values['household_value'].value-1,] for v in h_filtered]
# vals_dict = {0:[], 1:[], 2: []}
# for k in vals:
#     vals_dict[k[3]].append(k[0:3]) #append to the household measure
# vals_dict
# small_pop = [ (k,inside_v) for (k,v) in vals_dict.iteritems() for inside_v in v[:10]]
# full_pop = [ (k,inside_v) for (k,v) in vals_dict.iteritems() for inside_v in v[:40]]



children_raw = [
    [G, G, Y],
    [R, R, G],
    [R, G, G],
    [Y, Y, Y],
    [G, R, G],
]

if True:
    full_pop = [
            (0, [0, 2, 1]), (0, [2, 1, 0]), (0, [0, 0, 1]), (0, [2, 0, 2]), (0, [1, 1, 1]), (0, [1, 1, 2]), (0, [2, 0, 1]), (0, [2, 0, 1]), (0, [2, 1, 2]), (0, [2, 0, 1]), (0, [2, 0, 2]), (0, [2, 2, 2]),
            (1, [2, 2, 1]), (1, [2, 0, 0]), (1, [1, 1, 1]), (1, [2, 0, 1]), (1, [2, 1, 2]), (1, [2, 2, 2]), (1, [0, 2, 1]), (1, [2, 1, 2]), (1, [2, 2, 2]), (1, [2, 2, 1]), (1, [2, 2, 1]), (1, [2, 2, 1]), (1, [2, 2, 2]), (1, [2, 2, 2]), (1, [2, 2, 0]), (1, [2, 2, 2]), (1, [2, 0, 1]), (1, [2, 0, 1]), (1, [2, 2, 2]), (1, [2, 0, 1]), (1, [2, 1, 1]), (1, [1, 1, 2]), (1, [1, 0, 1]), (1, [1, 0, 1]), (1, [2, 1, 2]), (1, [1, 1, 2]), (1, [2, 0, 2]), (1, [1, 1, 2]), (1, [2, 1, 2]), (1, [2, 0, 2]), (1, [2, 0, 2]), (1, [2, 0, 2]), (1, [2, 0, 2]), (1, [2, 1, 1]), (1, [2, 2, 1]), (1, [2, 2, 1]), (1, [2, 2, 1]), (1, [1, 2, 2]), (1, [1, 1, 1]), (1, [2, 2, 1]),
            (2, [2, 0, 1]), (2, [2, 1, 2]), (2, [2, 2, 1]), (2, [1, 0, 2]), (2, [1, 2, 2]), (2, [1, 0, 1]), (2, [1, 0, 1]), (2, [2, 2, 2]), (2, [2, 2, 1]), (2, [0, 0, 0]), (2, [2, 0, 2]), (2, [2, 2, 1]), (2, [1, 0, 0]), (2, [1, 1, 2]), (2, [1, 0, 2]), (2, [2, 1, 1]), (2, [1, 1, 2]), (2, [1, 1, 2]), (2, [2, 1, 2]), (2, [0, 1, 2]), (2, [2, 0, 1]), (2, [2, 0, 2]), (2, [2, 0, 1]), (2, [1, 1, 2]), (2, [2, 2, 1]), (2, [2, 1, 1]), (2, [0, 0, 1]), (2, [1, 1, 1]), (2, [2, 2, 2]), (2, [2, 1, 0]), (2, [2, 0, 0]), (2, [2, 2, 1]), (2, [2, 0, 1]), (2, [2, 0, 1]), (2, [2, 1, 2]), (2, [2, 1, 2])]


    small_pop = [
         (0, [0, 2, 1]), (0, [2, 1, 0]), (0, [0, 0, 1]), (0, [2, 0, 2]), (0, [1, 1, 1]), (0, [1, 1, 2]), (0, [2, 0, 1]), (0, [2, 0, 1]), (0, [2, 1, 2]), (0, [2, 0, 1]),
         (1, [2, 2, 1]), (1, [2, 0, 0]), (1, [1, 1, 1]), (1, [2, 0, 1]), (1, [2, 1, 2]), (1, [2, 2, 2]), (1, [0, 2, 1]), (1, [2, 1, 2]), (1, [2, 2, 2]), (1, [2, 2, 1]),
         (2, [2, 0, 1]), (2, [2, 1, 2]), (2, [2, 2, 1]), (2, [1, 0, 2]), (2, [1, 2, 2]), (2, [1, 0, 1]), (2, [1, 0, 1]), (2, [2, 2, 2]), (2, [2, 2, 1]), (2, [0, 0, 0])]

    # small_pop = full_pop
    children = {}

    for i, k in enumerate(small_pop):
        children[i+1] = {"name": "S{:03}".format(i+1), "values": k[1], "node_value": [], "household": k[0]}

    nodes = []
    links = []

    nodes.append({"node": 0, "name": "Population", "id": "any_score"})

    # for k in sorted(letters.keys(), reverse=True):
    for k in sorted(letters.keys(), reverse=False):
        letters[k]["node_value"].append(len(nodes))
        nodes.append({"node": len(nodes), "name": "Household {}".format(letters[k]["string"]), "id": letters[k]["col_string"]})
        letters[k]["node_value"].append(len(nodes))
        nodes.append({"node": len(nodes), "name": "Final score {}".format(letters[k]["string"]), "id": letters[k]["col_string"]})


    for qqq in [0, 1, 2]:
        base_line = len(nodes)
        # ord_list = sorted([(k,v) for k,v in children.iteritems()], key=(lambda x: x[1]["values"][qqq]), reverse=True)
        ord_list = sorted([(k,v) for k,v in children.iteritems()], key=(lambda x: x[1]["values"][qqq]))

        for i, (child_id, vals) in enumerate(ord_list):
            # {"node": 1, "name": "Subject 1", "id": "yellow_score", "id_old": "hour_score"},
            children[child_id]["node_value"].append(len(nodes))
            nodes.append({"node": len(nodes), "name": "{}-T{}".format(vals["name"], qqq),
                     "id": letters[vals["values"][qqq]]["col_string"]})


    for k in sorted(letters.keys()):
        links.append({"source": 0, "target": letters[k]["node_value"][0], "value": 0.3})

    for child_id, vals in children.iteritems():
        # {"source": 0, "target": 2, "value": 0.08},
        links.append({"source": letters[vals["household"]]["node_value"][0],
                    "target": vals["node_value"][0], "value": 0.08})
        links.append({"source": vals["node_value"][0],
                    "target": vals["node_value"][1], "value": 0.08})
        links.append({"source": vals["node_value"][1],
                    "target": vals["node_value"][2], "value": 0.08})
        links.append({"source": vals["node_value"][2],
                    "target": letters[vals["values"][2]]["node_value"][1], "value": 0.08})

    res = {"nodes": nodes, "links": links, "subjects": len(children)}
    print json.dumps(res)

if True:
    print "------------------"
    children_real_raw = [[0, 2, 1], [0, 0, 0], [0, 1, 2], [0, 2, 1], [0, 0, 1], [0, 1, 1], [0, 0, 1], [0, 0, 1],
     [1, 1, 1],  [1, 0, 2],  [1, 2, 2],  [1, 0, 1],  [1, 0, 1],  [1, 0, 0],  [1, 1, 2],  [1, 0, 2],
     [2, 2, 1], [2, 0, 1], [2, 0, 0], [2, 0, 1], [2, 1, 2], [2, 1, 2], [2, 2, 2], [2, 2, 1]]



    children = {}

    for i, k in enumerate(children_real_raw):
        children[i+1] = {"name": "S{:03}".format(i+1), "values": k, "node_value": []}

    nodes = []
    links = []

    nodes.append({"node": 0, "name": "Population", "id": "any_score"})

    # for k in sorted(letters.keys(), reverse=True):
    for k in sorted(letters.keys()):
        letters[k]["node_value"].append(len(nodes))
        nodes.append({"node": len(nodes), "name": "Initial {}".format(letters[k]["string"]), "id": letters[k]["col_string"]})
        letters[k]["node_value"].append(len(nodes))
        nodes.append({"node": len(nodes), "name": "Final {}".format(letters[k]["string"]), "id": letters[k]["col_string"]})


    for qqq in [0, 1,2]:
        base_line = len(nodes)
        # ord_list = sorted([(k,v) for k,v in children.iteritems()], key=(lambda x: x[1]["values"][qqq]), reverse=True)
        ord_list = sorted([(k,v) for k,v in children.iteritems()], key=(lambda x: x[1]["values"][qqq]))

        for i, (child_id, vals) in enumerate(ord_list):
            # {"node": 1, "name": "Subject 1", "id": "yellow_score", "id_old": "hour_score"},
            children[child_id]["node_value"].append(len(nodes))
            nodes.append({"node": len(nodes), "name": "{}-T{}".format(vals["name"], qqq),
                     "id": letters[vals["values"][qqq]]["col_string"]})


    for k in sorted(letters.keys()):
        links.append({"source": 0, "target": letters[k]["node_value"][0], "value": 0.3})

    for child_id, vals in children.iteritems():
        # {"source": 0, "target": 2, "value": 0.08},
        links.append({"source": letters[vals["values"][0]]["node_value"][0],
                    "target": vals["node_value"][0], "value": 0.08})
        links.append({"source": vals["node_value"][0],
                    "target": vals["node_value"][1], "value": 0.08})
        links.append({"source": vals["node_value"][1],
                    "target": vals["node_value"][2], "value": 0.08})
        links.append({"source": vals["node_value"][2],
                    "target": letters[vals["values"][2]]["node_value"][1], "value": 0.08})

    res = {"nodes": nodes, "links": links, "subjects": len(children)}
    print json.dumps(res)