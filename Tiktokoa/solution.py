class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        re = []
        for i in range(len(mat)): #number of rows
            res = []
            for j in range(len(mat[0])): # number of col
                if mat[i][j] == 0:
                    res.append(0)
                else:
                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    distance = self.bfs(i,j,mat,directions)
                    res.append(distance)
            re.append(res)
        return re
                                
                            
    def bfs(self, i, j, mat, directions):
        print(i,j)
        if mat[i][j] == 0:
            return 0
        else:
            for k in range(len(directions)):
                x = directions[k][0] + i
                y = directions[k][1] + j
                if  x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]):
                    return self.bfs(x, y, mat, directions) + 1


if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    s = Solution()
    res = s.updateMatrix(mat)
    print()
    print(res)