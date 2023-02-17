print()

def get_list_of_colors(colors, n):
    return colors[:n]
 
colors = ["red", "orange", "green", "violet", "blue", "yellow"]
 
for i in range(1,len(colors)+1):
    print(get_list_of_colors(colors, i))
 
 
 