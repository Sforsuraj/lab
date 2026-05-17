
import random 
# Job processing times 
jobs = [5, 3, 8, 6, 2] 
num_jobs = len(jobs) 
num_particles = 5 
iterations = 50 
 
# Function to calculate total completion time 
def fitness(schedule): 
    time = 0 
    total = 0 
    for job in schedule: 
        time += jobs[job] 
        total += time 
    return total 
  
# Initialize particles 
particles = [] 
for i in range(num_particles): 
    particle = list(range(num_jobs)) 
    random.shuffle(particle) 
    particles.append(particle) 
 
pbest = particles[:] 
pbest_value = [fitness(p) for p in particles] 
gbest = pbest[pbest_value.index(min(pbest_value))] 
 
# PSO iterations 
for _ in range(iterations): 
    for i in range(num_particles): 
        # Random swap to simulate velocity update 
        a, b = random.sample(range(num_jobs), 2) 
        particles[i][a], particles[i][b] = particles[i][b], particles[i][a] 
 
        current_value = fitness(particles[i]) 
 
        if current_value < pbest_value[i]: 
            pbest[i] = particles[i][:] 
            pbest_value[i] = current_value 
 
    gbest = pbest[pbest_value.index(min(pbest_value))] 
 
print("Best Job Order:", gbest) 
print("Minimum Completion Time:", fitness(gbest))