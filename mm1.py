__metaclass__=type
import random
import csv

#define a class called 'Customer'
#objects of the customer
class Customer:
	def __init__(self,arrival_time,service_start_time,service_time):
		self.arrival_time=arrival_time
		self.service_start_time=service_start_time
		self.service_time=service_time
		self.service_end_time=self.service_start_time+self.service_time
		self.wait=self.service_start_time-self.arrival_time

#a simple function to sample from negative exponential
def generate_expo(lambd):
	return random.expovariate(lambd)

# function callbacklamda, mu, simulation_time
def foo(lambd,mu,simulation_time):
	#initialise time to 0
	t=0
	while t<simulation_time:

		#calculate arrival time and service time for new customer
		if len(Customers)==0:
			arrival_time=generate_expo(lambd)
			service_start_time=arrival_time
		#added arrival time
		else:
			arrival_time+=generate_expo(lambd)
			service_start_time=max(arrival_time,Customers[-1].service_end_time)
		service_time=generate_expo(mu)

		#create new customer
		Customers.append(Customer(arrival_time,service_start_time,service_time))

		#increment clock till next end of service
		t=arrival_time

		
#----------------------------------

	#calculate summary statistics
	Waits=[a.wait for a in Customers]
	Mean_Wait=sum(Waits)/len(Waits)

	Total_Times=[a.wait+a.service_time for a in Customers]
	Mean_Time=sum(Total_Times)/len(Total_Times)

	Service_Times=[a.service_time for a in Customers]
	Mean_Service_Time=sum(Service_Times)/len(Service_Times)
    #Server Utilisation
	Utilisation=sum(Service_Times)/t

	#output to the screen list of values
	print ""
	print "Summary results:"
	print ""
	print "Arrival rate: ", lambd
	print "Number of customers: ",len(Customers)
	print "Mean Service Time: ",Mean_Service_Time
	print "Mean Wait Time: ",Mean_Wait
	print "Observed waiting time in the system: ",Mean_Time
	print "Theoretical Result Calculated", Theoretical_result
	print ""
	# output to the file to store customer entire enter and exit time
	outfile=open('MM1Q-detailed_log_output-(%s,%s,%s).csv' %(lambd,mu,simulation_time),'wb')
	output=csv.writer(outfile)
	output.writerow(['Customer','Arrival_time','Wait','Service_Start_time','Service_Time','Service_End_time'])
	f=0
	for customer in Customers:
		f=f+1
		outrow=[]
		outrow.append(f)
		outrow.append(customer.arrival_time)
		outrow.append(customer.wait)
		outrow.append(customer.service_start_time)
		outrow.append(customer.service_time)
		outrow.append(customer.service_end_time)
		output.writerow(outrow)
	outfile.close()
	return Mean_Time
#main function
#instance variables
lambd = 0.1
mu = 1
simulation_time = 1000
i=0
Theoretical_result = 0.0
#compare result with obtained and store in file to experiment
outfile=open('MM1.csv','wb')
output=csv.writer(outfile)
output.writerow(['No','Arrival_Rate','Observed waiting time','Theoretical_result'])
#generate ten arrivale rates starting from 0.1 till 0.9
for x in xrange(1,10):
	Theoretical_result = 1 / (mu - lambd)
	Customers=[]
	# function call
	Observed_time = foo(lambd,mu,simulation_time)
	i=i+1
	#output to file
	outrow=[]
	outrow.append(i)
	outrow.append(lambd)
	outrow.append(Observed_time)
	outrow.append(Theoretical_result)
	lambd+=0.1  # increment lambda to next arrival rate
	output.writerow(outrow)
	
outfile.close() #file close




