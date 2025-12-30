# ==================================
# Future Smart Farm System (Fern)
# ==================================

# ----- 미래 스마트팜 기준 (2100년 가정) -----
OPTIMAL = {
    "temperature": 26,    # ℃
    "humidity": 65,       # %
    "co2": 800,           # ppm
    "light": 16000,       # lux
    "soil": 55            # %
}

TOLERANCE = {
    "temperature": 6,
    "humidity": 15,
    "co2": 300,
    "light": 5000,
    "soil": 15
}


def score(value, optimal, tolerance):
    diff = abs(value - optimal)
    return max(0, 25 * (1 - diff / tolerance))


# ----- 환경 입력 -----
print("미래 스마트팜 환경 시뮬레이션")
print("환경 값을 입력하세요\n")

env = {}
env["temperature"] = float(input("온도 (℃): "))
env["humidity"] = float(input("습도 (%): "))
env["co2"] = float(input("CO₂ 농도 (ppm): "))
env["light"] = float(input("조도 (lux): "))
env["soil"] = float(input("토양 수분 (%): "))


# ----- 성장 적합도 계산 -----
total_score = 0
for key in OPTIMAL:
    total_score += score(env[key], OPTIMAL[key], TOLERANCE[key])

growth_rate = total_score / 10  # %


# ----- 스마트팜 자동 제어 판단 -----
control = []

if env["temperature"] < OPTIMAL["temperature"]:
    control.append("히터 가동")
elif env["temperature"] > OPTIMAL["temperature"]:
    control.append("냉각 시스템 가동")

if env["humidity"] < OPTIMAL["humidity"]:
    control.append("가습기 가동")
elif env["humidity"] > OPTIMAL["humidity"]:
    control.append("환기 시스템 가동")

if env["co2"] < OPTIMAL["co2"]:
    control.append("CO₂ 공급")
elif env["co2"] > OPTIMAL["co2"]:
    control.append("환기 강화")

if env["light"] < OPTIMAL["light"]:
    control.append("인공 조명 강화")

if env["soil"] < OPTIMAL["soil"]:
    control.append("관수 시스템 가동")


# ----- 결과 출력 -----
print("\n미래 스마트팜 생장 분석 결과")
print(f"성장 적합도 점수: {total_score:.2f} / 125")
print(f"예상 성장률: {growth_rate:.2f} %")

if growth_rate >= 7:
    print("판정: 미래 환경 적합")
elif growth_rate >= 4:
    print("판정: 제한적 생육 가능")
else:
    print("판정: 환경 부적합")

print("\n스마트팜 자동 제어 제안")
if control:
    for c in control:
        print(" -", c)
else:
    print(" - 모든 조건이 미래 기준에 부합")