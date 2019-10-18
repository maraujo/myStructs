houses = [2,1,8,7,1,3]

def robber(houses):
	if len(houses) == 0:
		return None
	if len(houses) == 1:
		return houses[0]
	if len(houses) == 2:
		return max(houses[0], houses[1])

	sol_prev = houses[0]
	sol = max(houses[0],houses[1])
	new_sol = False
	for i in range(2, len(houses)):
		if new_sol != False:
			sol_prev = sol
			sol = new_sol
		new_sol = max(sol, houses[i] + sol_prev)
	return new_sol

print(robber(houses))
