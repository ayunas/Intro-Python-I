import ast
string1 = str({'city': 'athens', 'lat': 58, 'lon': 43})
string2 = str({'difficulty': 'hard', 'size': '1 gb'})
strdict1 = ast.literal_eval(string1)
strdict2 = ast.literal_eval(string2)
obj = {**strdict1, **strdict2}

print(obj, type(obj))
