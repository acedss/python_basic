message = "Hello"

print(f"*{message:<20}*")
print(f"-{message:>20}-")
print(f"<{message:^20}>")
print(f"/{message:20}/")

n = 100
print(type(n))


print(f"*${n:>20.2f}*")
print(f"-${n:<20.4f}-")
print(f"<${n:^20.2f}>")
print(f"/${n:20.2f}/")

PI = 3.141592653589793
print(f'|{PI:>20.2f}|')
print(f'|{PI:<20.4f}|')
print(f'|{PI:^20.6f}|')
print(f'|{PI:20.8f}|')

