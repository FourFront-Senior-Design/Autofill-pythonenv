'''
Creates the best match between the ocr words and the database words
to minimize the edit distance.
This will help label the OCR words to the correct column in the database
'''
import queue

class BestMatch:
    INF = 1000 * 1000 * 1000

    '''
    Creates the graph of size n x n
    '''
    def __init__(self, ocrData, accessData):
        self.ocr = ocrData
        self.access = accessData
        if len(self.ocr) > len(self.access):
            diff = len(self.ocr) - len(self.access)
            self.access.extend([''] * diff)
        elif len(self.ocr) < len(self.access):
            diff = len(self.access) - len(self.ocr)
            self.ocr.extend([''] * diff)
        self.__createGraph()

    def __createGraph(self):
        self.graph = []
        length = len(self.access)
        for i in range(length):
            temp = []
            for j in range(length):
                dist = self.__levenshteinDistance(self.access[i], self.ocr[j])
                temp.append(dist)
            self.graph.append(temp)

    '''
    The weight of the edges are in terms of edit distance
    '''
    def __levenshteinDistance(self, word1, word2):
        if word1 == None:
            word1 = ""
        if word2 == None:
            word2 = ""
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        distances = range(len(word1) + 1)
        for index2, char2 in enumerate(word2):
            newDistances = [index2 + 1]
            for index1, char1 in enumerate(word1):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                                 distances[index1 + 1],
                                                 newDistances[-1])))
            distances = newDistances
        return distances[-1]

    '''
    Implementing the min-cost max flow algorithm to get the best match
    '''
    def __minCostMaxFlow(self):
        n = len(self.graph)
        m = n*2 + 2
        f = [[0 for x in range(m)] for y in range(m)]
        s = m - 2
        t = m - 1
        cost = 0
        while True:
            dist = [self.INF for x in range(m)]
            p = [0 for x in range(m)]
            inq = [False for x in range(m)]
            q = queue.Queue()
            dist[s] = 0
            p[s] = -1
            q.put(s)
            while not q.empty():
                v = q.get()
                inq[v] = False
                if v == s:
                    for i in range(n):
                        if f[s][i] == 0:
                            dist[i] = 0
                            p[i] = s
                            inq[i] = True
                            q.put(i)
                elif v < n:
                    for j in range(n, n + n):
                        if f[v][j] < 1 and dist[j] > dist[v] + self.graph[v][j-n]:
                            dist[j] = dist[v] + self.graph[v][j-n]
                            p[j] = v
                            if not inq[j]:
                                q.put(j)
                                inq[j] = True

                else:
                    for j in range(n):
                        if f[v][j] < 0 and dist[j] > dist[v] - self.graph[j][v-n]:
                            dist[j] = dist[v] - self.graph[j][v-n]
                            p[j] = v
                            if not inq[j]:
                                q.put(j)
                                inq[j] = True

            currcost = self.INF
            for i in range(n, n+n):
                if f[i][t] == 0 and dist[i] < currcost:
                    currcost = dist[i]
                    p[t] = i
            if currcost == self.INF:
                break
            cost = cost + currcost
            cur = t
            while cur != -1:
                prev = p[cur]
                if prev != -1:
                    f[prev][cur] = 1
                    f[cur][prev] = -1
                cur = p[cur]

        answer = [0 for x in range(n)]
        for i in range(n):
            for j in range(n):
                if f[i][j+n] == 1:
                    answer[i] = j

        return answer

    '''
    Running the min cost - max flow algorithm and converting the
    answer map the word in the access database to the word 
    in the ocr
    '''
    def create(self):
        answer = self.__minCostMaxFlow()
        length = len(self.graph)
        bestMatch = []
        for i in range(length):
            bestMatch.append([self.access[i], self.ocr[answer[i]]])
        return bestMatch


