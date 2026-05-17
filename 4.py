
arrival_rate = 4 # λ (customers per hour) 
service_rate = 6 # μ (customers per hour) 
 
# Check stability condition 
if arrival_rate >= service_rate: 
    print("System is unstable (arrival rate must be less than service rate)") 
else: 
    # Utilization factor 
    rho = arrival_rate / service_rate 
 
    # Performance measures 
    L = arrival_rate / (service_rate - arrival_rate) 
    Lq = (arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate)) 
    W = 1 / (service_rate - arrival_rate) 
    Wq = arrival_rate / (service_rate * (service_rate - arrival_rate)) 
 
    print("Utilization (rho):", rho) 
    print("Average number in system (L):", L) 
    print("Average number in queue (Lq):", Lq) 
    print("Average time in system (W):", W) 
    print("Average waiting time in queue (Wq):", Wq)