n, m = map(int, input().split())  # 자연수 N과 M을 입력받음

visited = [False] * (n + 1)  # 방문 여부를 체크하는 리스트
result = []  # 결과를 저장하는 리스트


def backtrack(cnt):
    if cnt == m:  # M개를 선택한 경우
        print(' '.join(map(str, result)))  # 결과를 출력하고
        return  # 함수를 종료함

    for i in range(1, n + 1):
        if not visited[i]:  # 아직 방문하지 않은 경우
            visited[i] = True  # 방문 여부를 체크하고
            result.append(i)  # 결과 리스트에 추가함
            backtrack(cnt + 1)  # 다음 수를 선택하기 위해 재귀 호출함
            visited[i] = False  # 백트래킹을 위해 방문 여부를 체크를 해제함
            result.pop()  # 결과 리스트에서 마지막 요소를 제거함


backtrack(0)  # 백트래킹 알고리즘을 실행함