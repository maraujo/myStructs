houses = [2,14,7,3,6]

def robber(houses):
	if len(houses) == 0:
		return None
	if len(houses) == 1:
		return houses[0]
	if len(houses) == 2:
		return max(houses[0], houses[1])

	sol = []
	sol.append(houses[0])
	sol.append(max(houses[0],houses[1]))

	for i in range(2, len(houses)):
		sol.append(max (sol[i - 1], houses[i] + sol[i - 2]))
	return sol[-1]

print(robber(houses))
