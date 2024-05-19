def min_removals(str):
    count = 0
    for s in str:
        while True:
            if s.find("aa") == 0:
                s = s.replace('a','',1)
                count += 1
            elif s.find("bb") == 0:
                s = s.replace('b','',1)
                count += 1
            elif s.find("ab") == 0:
                s = s.replace('ab','b',1)
                count += 1               
            elif s.find("ba") == 0:
                s = s.replace('ba','a',1)
                count += 1                      
            else: break

    return count

if __name__ == "__main__":
    test_case = int(input())
    results = []
    
    for tc in range(1,test_case+1):
        N = int(input())
        str = input().split()
        C = min_removals(str)
        results.append(f"#{tc} {C}")
    
    for result in results:
        print(result)