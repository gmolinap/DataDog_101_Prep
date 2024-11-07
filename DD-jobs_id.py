"""
jobs = [
    [1,30,[2]],
    [2,10,[3]],
    [3,20]
]


1. job ID
2. job time
3. child job IDs

It seems like a graph, i can solve it with recursion
There're circular dependencies? No


Recursion → job time - add the job time, and recursivily calculate time for each child job, return the sum
job map (dictionary) O(n)
"""

def TotalJobtime(jobs, jobID):
    job_time_map = {job[0]: (job[1],job[2]) for job in jobs}

    def time_calculation(jobID):
        job_time, child_job_id = job_time_map[jobID]
        print(job_time)
        print(child_job_id)

    
        time_counter = job_time
        for i in child_job_id:
            time_counter  += time_calculation(i)
        return time_counter
    
    return time_calculation(jobID)





jobs = [
    [1,30,[2]], 
    [2,10,[3]],
    [3,20,[]],
]

print(TotalJobtime(jobs,1))




diccionario = {5:['20','30']}

first,second = diccionario[5]
print(first,second )