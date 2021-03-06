'''
문제 1)
제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다.
그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 얼마인지 알아보기 위해, 상상력을 발휘하여 아래와 같은 가정을 하였다.

- 제1회 코드 페스티벌 본선에 진출하여 a등(1 ≤ a ≤ 100)등을 하였다. 단, 진출하지 못했다면 a = 0으로 둔다.
- 제2회 코드 페스티벌 본선에 진출하여 b등(1 ≤ b ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 b = 0으로 둔다.

제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.

[입력]
첫 번째 줄에 제이지가 상상력을 발휘하여 가정한 횟수 T(1 ≤ T ≤ 1,000)가 주어진다.

다음 T개 줄에는 한 줄에 하나씩 제이지가 해본 가정에 대한 정보가 주어진다.
각 줄에는 두 개의 음이 아닌 정수 a(0 ≤ a ≤ 100)와 b(0 ≤ b ≤ 64)가 공백 하나를 사이로 두고 주어진다.

[출력]
각 가정이 성립할 때 제이지가 받을 상금을 원 단위의 정수로 한 줄에 하나씩 출력한다. 입력이 들어오는 순서대로 출력해야 한다.
'''
class Solution():
    money_2017 = [(1, 5000000), (3, 3000000), (6, 2000000), (10, 500000), (15, 300000), (21, 100000)]
    money_2018 = [(1, 5120000), (3, 2560000), (7, 1280000), (15, 640000), (31, 320000)]
    def solution(self, str):
        ranks = [*map(int, str.split())]
        sum = 0
        if ranks[0]:
            for money in self.money_2017:
                if ranks[0] <= money[0]:
                    sum = sum + money[1]
                    break
        if ranks[1]:
            for money in self.money_2018:
                if ranks[1] <= money[0]:
                    sum = sum + money[1]
                    break
        print(sum)

s = Solution()
for i in range(int(input())):
    s.solution(input())
