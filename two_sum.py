def two_sum(target):
    for i in range(0,5):
        for j in range(i,5):
            if sum[i]+sum[j] == target:
                print(i,j)
                break
            else:
                j+=1
                # print("Can not match target.")
        i+=1

sum = [2,9,4,1,5,6]
target = 7
two_sum(target)