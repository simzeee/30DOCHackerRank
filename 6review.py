# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())

for i in range(test_cases):
    test_string = input()
    even = ""
    odd = ""
    
    for j in range(len(test_string)):
        if j % 2 == 0:
            even += test_string[j]
        else:
            odd += test_string[j]
    
    print(f'{even} {odd}')