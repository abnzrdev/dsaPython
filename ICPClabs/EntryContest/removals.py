test_case = int(input(""))
for i in range(test_case):
    size = int(input(""))
    alice_list = list(map(int, input("").split()))
    bob_list = list(map(int, input("").split()))
    if alice_list == bob_list:
        print("Bob")
    else:
        print("Alice")