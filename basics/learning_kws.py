def test(**kw): #receive any number os parameters based on a dict
    for key in kw.values():
        print("Key: "+str(key))

test(a="a",b="b",c="c")
print("____")
test(j="a", k="b", l="c", m="d")