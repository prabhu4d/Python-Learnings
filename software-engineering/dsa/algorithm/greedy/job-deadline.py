"""

"""

class Job:
    def __init__(self, ID, deadline, profit):
        self.ID = ID
        self.deadline = deadline
        self.profit = profit


def sortProfit(job):
    l = len(job)
    for i in range(l):
        mx = 0
        for j in range(i,l):
            if job[j].profit > mx:
                mx = job[j].profit
                job[i], job[j] = job[j], job[i]        
    return job

def jobSchedule(jobs, t):
    slots = [False]*t
    profit = 0

    for job in jobs:
        for j in range(job.deadline,-1,-1):
            if j<t and slots[j] == False:
                slots[j] = job.ID
                profit += job.profit
                break
    
    print(slots)
    print(profit)



if __name__ == "__main__":
    jobs = [
        Job('1', 2, 100),
        Job('2', 3, 400),
        Job('3', 1, 80),
        Job('4', 2, 110),
        Job('5', 30, 500),
        Job('6', 4, 90)
    ]

    jobs = sortProfit(jobs)
    totaljobs = 2
    jobSchedule(jobs, totaljobs)