import pickle

shoplist = ['apple', 'banana', 'pomegranate', 'papaya']
shoplist.sort()

print "Shopping list is: ",
print shoplist

fname = "./shoplist.dat"
f = open(fname, 'wb')
pickle.dump(shoplist, f)
f.close()

g = open(fname, 'rb')
storedlist = pickle.load(g)

print "Stored list is: ",
print storedlist


