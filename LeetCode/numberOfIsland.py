import collections
from nntplib import GroupInfo


class Solution:
    def numIslands(matrix: list[list[str]] ):
        
        if matrix == [[]]:
            return "no island found"
        else:
            #print ("inside else")
            rows = len(matrix)
            columns = len(matrix[0])
            island = 0
            visited = []
            #print (visited)
            #print (rows, columns)
            
        
        def bfs(r, c):
            #print ("inside bfs")
            queued = collections.deque()
            visited.append((r,c))
            queued.append((r,c))
            #print (visited)
            #print (queued)
            while queued:
                row, column = queued.popleft()
                #print (row, column)
                directions = [[-1, 0], [1,0], [0,1], [0,-1]]
                for  rw, cl in directions:
                    #print (rw, cl)
                    r = row + rw
                    c = column + cl
                    #print (c, r)
                    if(r >= 0 and r < rows and
                       c >= 0 and c < columns and
                       matrix[r][c] == '1' and
                       (r,c) not in visited):
                        #print ("inside bfs if")
                        
                        queued.append((r,c))
                        visited.append((r,c,))
                        #print (visited)
                        
             
        for r in range(rows):
           
            for c in range(columns):
                
                if matrix[r][c] == "1" and (r,c) not in visited:
                    
                    
                    bfs(r, c)
                    island += 1
                    
        print (island)
    
    
    grid= [ ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"] ]

    numIslands(grid)
                                    