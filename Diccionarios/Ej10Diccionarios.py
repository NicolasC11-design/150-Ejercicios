dic = {"a": 1, "b": 2, "c": 1, "d": 3}
unicos = {}
for k, v in dic.items():
    if v not in unicos.values():
        unicos[k] = v
print(unicos)