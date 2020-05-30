class Sol:
    def is_valid_palindromII(self,str):
        count=0
        j=len(str)-1
        for i in range(len(str)//2):
            if str[i]!=str[j]:
                count+=1
            j-=1
        return count<2

if __name__ == '__main__':
    p=Sol()
    print(p.is_valid_palindromII('abbcca'))
