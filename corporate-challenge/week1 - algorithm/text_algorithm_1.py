import sys

# pi[k] : 인덱스 0부터 k까지 만들 수 있는열부분문자열에서 가장 긴 lps 문자열 길이
# lps : longest proper prefix which is suffix, 가장 긴 접두사이면서 접미사인 문자열
# pi 배열 만드는 함수 
def computepi(pat, pi):
	leng = 0 # 기존까지 가장 긴 lps 길이
	i = 1
	while i < len(pat):
		# 기존 인덱스까지 값이 같은지 비교
		# 같다면, 다음 인덱스끼리 비교 위해 i+1
		if pat[i] == pat[leng]:
			leng += 1
			pi[i] = leng
			i += 1
		# 값이 같지 않다면, leng-1로 직전 인덱스와 비교
		# i는 변화 없기 때문에 직전 인덱스와 비교 가능
		else:
			if leng != 0:
				leng = pi[leng-1]
			# leng == 0인데 같지 않다면 lps 문자열이 없단 뜻이므로 i 이동
			else:
				pi[i] = 0
				i += 1

def text_search(pat, txt):
	# 패턴 문자열 길이
	pat_len = len(pat)
	# 타겟 문자열 길이
	txt_len = len(txt)

	# 패턴 문자열 길이만큼 pi 배열 만들기
	pi = [0] * pat_len
	# 해당 패턴의 pi 배열 계산
	computepi(pat, pi)
	# 타겟 문자열 인덱스
	i = 0
	# 패턴 문자열 인덱스
	j = 0

	while i < txt_len:
		# 패턴과 타겟이 같은 경우 계속해서 다음 인덱스 비교
		if pat[j] == txt[i]:
			i += 1
			j += 1
		# 같지 않다면 pi배열에서 lps 길이만큼 직전 인덱스와 비교
		elif pat[j] != txt[i]:
			if j != 0:
				j = pi[j-1]
			# j == 0이라면 일치하는 부분이 없으므로 비교대상 타겟 문자열 이동
			else:
				i += 1
		# 패턴 인덱스가 패턴 끝까지 다 돌았다면 (패턴을 찾았다면)
		if j == pat_len:
			return True
	# 타겟 문자열 끝까지 돌았는데도 패턴을 찾지 못했다면
	return False

if __name__ == '__main__':
	argument = sys.argv
	if len(argument) == 1:
		print("-----Please insert a file to read-----")
		exit()
	f = open('./' + argument[1], 'r')
	N = int(f.readline())
	S = [''.join(filter(str.isalpha, i)) for i in str(f.readline()).split(',')]
	Q = int(f.readline())
	targets =[''.join(filter(str.isalpha, i)) for i in str(f.readline()).split(',')] 
	result = []

	for txt in targets:
		for pat in S:
			val = text_search(pat, txt)
			result.append(val)
		print(result)
