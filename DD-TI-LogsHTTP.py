"""
1. You are given the list of logs of HTTP requests in the given format:
[IP, HTTP Verb, status, response time, size, request time]
Write the code to answer the various queries. For example, list all HTTP requests for the last 2 months or show all requests with 200 status, etc.


Interviewer changes the query structure frequently and you should answer how you are going to attack that particular query.
In the end, after the discussion of the pros and cons of different approaches you need to code that. 

Questions? 5 min
logs HTTP
IP, HTTP Verb, status, response time, size, request time

### GABRIEL
1) How many requests needs this system afford? Shall we do first a Naive approach or we need to approach to a scalable solution.
Which is going to be the PK? IP?
Can we combine several DS? Returning for example the last HTTP and first HTTP response.
Needs to be a function for analyzing the list of logs
Is it OK if i write in Python?

### IMPROVED
1) What are the permormance requirements? Are we expecting thousands of requests per second?
2) How often are we accessing the type of query? Are we going to access the last HTTP request of X month every second?
3) Are we storing the logs indefinetly?


Approach
We should create a class to store logs and then create the methods to access them.

1. Method that retrives last HTTP request of X month (tree binary search  → request_time →As its easy to get the information of the list given a month by
dividing it, and going to the closest date that we have)  Complexity: O(log n) because it will take into acc the size of the array how ever as it's going to 
[descartar] the months that we dont need , the time will reduce considerably
2. Methods that retrives queries with an specific status (Dictionary with key values based on the status, and print it values in a list), O(1)
3. Method that retrives the last query (Piles) O(1)
 

Commentaries solution:
Elasticsearch kind of indexed logs, and then we can query the logs with the queries that we need.
"""

#import dictionaries

class Log_Entry:
    def __init__(self, IP, HTTP_verb, status, response_time, size, request_time):
        self.IP = IP
        self.HTTP_verb = HTTP_verb
        self.status = status
        self.response_time = response_time
        self.size = size
        self.request_time = request_time

class HTTP_logs: #for storing the logs and managing the queries, it means, the class that will have the methods
    def __init__(self):
        self.logs = [] # list of logs
        self.status_queries = {} #dictionary with the status of queries
        self.logs_stack = [] #Stack to keep logs in chronology

    def add_log(self,log_entry):
        self.logs.appends(log_entry)
        print(self.logs)
        self.logs_stack.append(log_entry)
        if log_entry.status not in self.status.queries:
            self.status_queries[log_entry.status] = []
            print(self.status_queries)
        self.status_queries[log_entry.status].append(log_entry)
        
    def queries_status(self, status):
        return self.status_queries.get(status, [])
    
    def retrive_last_query(self):
        return self.logs_stack[-1]
    

#Test
log = HTTP_logs()
log.add_log(Log_Entry("192.202.2, 200, 1.2, 200, 2020-02-02, 2020-02-02"))
log.add_log(Log_Entry("192.202.2, 200, 1.2, 200, 2020-02-02, 2020-02-02"))
log.add_log(Log_Entry("192.202.2, 200, 1.2, 200, 2020-02-02, 2020-02-02"))

print(log.queries_status(200))
print(log.retrive_last_query())

    