import collections

def solution(tickets):
    graph = collections.defaultdict(list)
    
    for a, b in sorted(tickets, key = lambda x: x[1]): #도착공항 기준으로 알파벳순 정렬
        graph[a].append(b) #출발a, 도착b
    
    route = []
    
    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop(0))
        route.append(start)
        
    dfs("ICN")
    return route[::-1] #더이상 갈 수 있는 공항 없을 때 그 공항을 경로에 추가