import random
import matplotlib.pyplot as plt
import os
now = os.getcwd()

def DoTest(n,select,cost,profit):
	"""
	n:시행할 횟수
	select:뽑을 횟수
	"""
	average = 0
	for i in range(n):
		average-=cost
		select_list = random.sample(range(1,21),select)
		answer = random.randint(1,20)
		if answer in select_list:
			average+=profit
	average = average / n
	return average

def main(n,cost,profit):
	result = []
	for i in range(1,21):
		result.append(DoTest(n,i,cost,profit))
	plt.plot(range(1,21),result,'b',label='Case 1')
	result = []
	for i in range(1,21):
		result.append(DoTest(n,i,cost,profit))
	plt.plot(range(1,21),result,'r',label='Case 2')
	result = []
	for i in range(1,21):
		result.append(DoTest(n,i,cost,profit))
	plt.plot(range(1,21),result,'g',label='Case 3')
	plt.xlabel('The number of times you pick')
	plt.ylabel('Profit')
	plt.grid(True)
	plt.title(f'Cost:{cost} profit:{profit} ({n}times)')
	plt.legend()
	plt.savefig(f'{now}//{cost} {profit} {n}times.png')
	plt.clf()

main(10,1,1)
main(100,1,1)
main(1000,1,1)
main(10,1,10)
main(100,1,10)
main(1000,1,10)
main(10,1,20)
main(100,1,20)
main(1000,1,20)
