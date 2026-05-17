#==================== Code 1================# 
jobs = { 
    "J1": 6, 
    "J2": 2, 
    "J3": 8, 
    "J4": 3, 
    "J5": 4 
} 
# Sort jobs based on processing time 
sorted_jobs = sorted(jobs.items(), key=lambda x: x[1]) 
print("Optimal Sequence (SPT Rule):") 
completion_time = 0 
total_completion_time = 0 
for job, time in sorted_jobs: 
    completion_time += time 
    total_completion_time += completion_time 
    print(f"{job} (Processing Time: {time}) -> Completion Time: {completion_time}") 
print("\nTotal Completion Time:", total_completion_time)

#===========Code 2 ==================# 
import pandas as pd 
# Processing times 
data = { 
    "Job": ["J1", "J2", "J3", "J4"], 
    "M1": [4, 3, 7, 2], 
    "M2": [5, 6, 4, 8] 
} 
df = pd.DataFrame(data) 
sequence = [] 
remaining_jobs = df.copy() 
 
while not remaining_jobs.empty: 
    min_time = remaining_jobs[["M1", "M2"]].min().min() 
    job_row = remaining_jobs[(remaining_jobs["M1"] == min_time) | 
                             (remaining_jobs["M2"] == min_time)].iloc[0] 
    job = job_row["Job"] 
    if job_row["M1"] == min_time: 
        sequence.insert(0, job) 
    else: 
        sequence.append(job) 
    remaining_jobs = remaining_jobs[remaining_jobs["Job"] != job] 
 
print("Optimal Sequence using Johnson’s Rule:") 
print(sequence)