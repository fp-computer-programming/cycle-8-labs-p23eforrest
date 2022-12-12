rows = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan",
"Phil", "Eman", "Alex", "Nicholas"],
["Christian", "Josh", "Matt", "Francesco"],
["Patrick", "Nico", "Trevayne"]]
#nested list row

def print_names(rows):
    #creates function
    for row in rows:
        for name in row:
            #prints all names
            print(name)
            
print_names(rows)
