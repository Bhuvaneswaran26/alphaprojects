
cricketlovers={"Faridh","Bhuvanes","Ranjith","Jagadish","Banti","Dinesh","Fazeel"}
kabaddilovers={"Shabeer","Shanker","vishwa","Faridh","Bhuvanes","Jagadish","Fazeel"}
print("Data Analysis using sets")
print("cricketlovers {}".format(cricketlovers))
print("kabaddilovers {}".format(kabaddilovers))
print("people who like both cricket and kabaddi {}".format(cricketlovers.intersection(kabaddilovers)))
print("peopele who are intrested only in cricket {}".format(cricketlovers.difference(kabaddilovers)))
print("people who are only intrested in kabaddi {}".format(kabaddilovers.difference(cricketlovers)))
print("people who are not intrested in single sport {}".format(cricketlovers.symmetric_difference(kabaddilovers)))
print("----Data Analysis is completed----")
print("Let us check wheather there is no both lovers -- {} ".format(cricketlovers.isdisjoint(kabaddilovers)))
print("Let us all the kabaddilovers are cricketlovers --{}".format(cricketlovers.issuperset(kabaddilovers)))
print("let us check all the cricketlovers are kabaddilovers -- {}".format(cricketlovers.issubset(kabaddilovers)))