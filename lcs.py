def lcs(s,t):
	len_s = len(s)
	len_t = len(t)
	l = [[0 for i in range(0,len_t+1)] for j in range(0,len_s+1)]
	b = [[0 for i in range(0,len_t+1)] for j in range(0,len_s+1)]
	for i in range(1, len_s+1):
		for j in range(1, len_t+1):
			if s[i-1] == t[j-1]:
				l[i][j] = l[i-1][j-1] + 1
				b[i][j] = 3
			else:
				if l[i-1][j] >= l[i][j-1]:
					l[i][j] = l[i-1][j]
					b[i][j] = 2
				else:
					l[i][j] = l[i][j-1]
					b[i][j] = 1
#	r = ""
#





#	r = findLCS(b,len_s,len_t,r,s)
	return l[len_s][len_t]
def findLCS(b,i,j,r,s):
	if b[i][j] == 0:
		return r
	if b[i][j] == 3:
		r = findLCS(b,i-1,j-1,r,s)
		return r + s[i-1]
	elif b[i][j] == 2:
		return findLCS(b,i-1,j,r,s)
	else:
		return findLCS(b,i,j-1,r,s)
str1 = "LIBYAN TELECOM AND TECHNOLOG"
str2 = "LIBYAN TELECOM AND TECHNOLOGY"
lcs(str1,str2)
