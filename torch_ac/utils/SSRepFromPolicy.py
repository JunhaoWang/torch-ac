def getSSRepFromPolicy(policy,stateToIndex):
	return 0


def getSSRepSample(policy,stateToIndex,start):
	collect_s = []
	for s in range(length(stateToIndex)):
		if s in vectorTraj:
			collect_s += vectorTraj[vectorTraj.index(s):]
	collect_s = dict(Counter(collect_s))
	result = []
	for s in range(numState):
		if s not in collect_s:
			result.append(0)
		else:
			result.append(collect_s[s])
