import random

# userIDの生成(0~9の暗号)
def generate_id(n=128):
    candidate = "0123456789abcdefghijklmnopqrstuvwxyz"
    lis = [random.choice(candidate) for _ in range(n)]
    return "".join(lis)

if '__main__' == __name__:
    print(generate_id())