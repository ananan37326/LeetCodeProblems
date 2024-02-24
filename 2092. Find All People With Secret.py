class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])
        time_meetings = {}

        for src, dst, t in meetings:
            if t not in time_meetings:
                time_meetings[t] = defaultdict(list)
            time_meetings[t][src].append(dst)
            time_meetings[t][dst].append(src)

        def dfs(src, adj):
            if src in visit:
                return
            visit.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei, adj)

        for t in sorted(time_meetings.keys()):
            visit = set()
            for src in time_meetings[t]:
                if src in secrets:
                    dfs(src, time_meetings[t])

        return list(secrets)