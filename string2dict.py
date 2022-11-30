

dict_list = ["{'ajay':27}", "{'Sanjay':28}", "{'Prathap':15}", " {'Vikrant':27}"]

#  [{'ajay': 27}, {'Sanjay': 28}, {'Prathap': 15}, {'Vikrant': 27}]

dict_out = []
for di in dict_list:
    toks = di.strip()[1:-1].split(':')
    k, v = toks[0], toks[1]
    dict_out.append({k[1:-1]: v})