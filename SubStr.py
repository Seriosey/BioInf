
test_str = str(input())
sub = str(input())
res = [i for i in range(len(test_str)) if test_str.startswith(sub, i)]


if len(res)==0:
    print('none')
else: print(*res, sep = ' ')