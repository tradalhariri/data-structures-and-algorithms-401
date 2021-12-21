# from graph import Graph

def business_trip(graph,cities_names):
    
    cost = 0
    for i, city in enumerate(cities_names):
        if i  < len(cities_names) -1:
            neighbors = graph.get_neighbors(city)
            valid = False
            for edge in neighbors:
                if edge.vertex == cities_names[i+1]:
                    cost += edge.weight
                    valid = True
                    break
    return (valid , f"${cost}")



# if __name__ == "__main__":
#       graph = Graph()
#       pandora = graph.add_node("Pandora")
#       arendelle = graph.add_node("Arendelle")
#       metroville = graph.add_node("Metroville")
#       monstroplolis = graph.add_node("Monstroplolis")
#       narnia = graph.add_node("Narnia")
#       naboo = graph.add_node("Naboo")
      
#       graph.add_edge(pandora, arendelle,150)
#       graph.add_edge(pandora, metroville,82)

#       graph.add_edge(arendelle,pandora,150)
#       graph.add_edge(arendelle,metroville,99)
#       graph.add_edge(arendelle,monstroplolis,42)
#       graph.add_edge(metroville,arendelle,99)
#       graph.add_edge(metroville,monstroplolis,105)
#       graph.add_edge(metroville,pandora,82)
#       graph.add_edge(metroville,narnia,37)
#       graph.add_edge(metroville,naboo,26)
#       graph.add_edge(monstroplolis,arendelle,42)
#       graph.add_edge(monstroplolis,metroville,105)
#       graph.add_edge(monstroplolis,naboo,73)
#       graph.add_edge(narnia,metroville,37)
#       graph.add_edge(narnia,naboo,250)
#       graph.add_edge(naboo,narnia,250)
#       graph.add_edge(naboo,metroville,26)
#       graph.add_edge(naboo,monstroplolis,73)
      
#       print(graph.breadth_first(pandora))
#       print(business_trip( graph,[metroville,pandora]))
#       print(business_trip( graph,[arendelle,monstroplolis,naboo]))
#       print(business_trip( graph,[naboo,pandora]))
#       print(business_trip( graph,[narnia,arendelle,naboo]))



#       ## 
#       # a = Vertex("a")
#       # print(graph.breadth_first(a))