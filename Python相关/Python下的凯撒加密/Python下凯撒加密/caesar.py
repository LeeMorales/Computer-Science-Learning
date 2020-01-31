import sys
times=0
  
#初始化一个字母表
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  
plain=input("Please input your plain text: ")
value=input("Please input your key(included negatives): ")
  
try:
    value=int(value)
except ValueError:
    print("Please input an integer.")
    sys.exit()
 
#将用户输入的内容转换为列表，每个字母都是列表中的一个对象。
secret_list=list(plain)
secret_list_len=len(secret_list)
  
print("")
print("secret: ",end='')
 
#循环一次就处理一个字母
while times < secret_list_len:
    times=times+1
  
#num实际上就是最终字母的移位量。
    #这分为几步：
    #第一步：取出plain这个列表的第某个对象，times为循环次数。第一次循环就处理第一个字母哦！但由于列表从0开始，因此-1。
    #第二步：alphabet.index用来将用户输入在plain列表的字母，查到alphabet列表对应的位置。
    #第三步：在这个位置上加上value这个用户设置的移位量。最终的变量将是一个已经移动位置的alphabet列表对象顺序。
    try:
    #如果这个try完全正常，则说明这是一个小写字母(能在alphabet中找到该字母)，同时不存在列表超出范围(list index out of range)的问题。那么，将密文保存到output。
        num=int(alphabet.index(plain[times-1])+int(value))
        output=alphabet[num]
    except ValueError:
    #如果发生了ValueError，则说明这不是一个小写字母(不能在alphabet中找到该字母)。
        try:
        #如果这个try完全正常，则说明这是一个大写字母(能在alphabet_upper中找到该字母)，同时不存在列表超出范围的问题。那么，将密文保存到output。
            num=int(alphabet_upper.index(plain[times-1])+int(value))
            output=alphabet_upper[num]
        except IndexError:
        #如果发生了IndexError，则说明这是一个大写字母，但是列表超出范围。那么，如果列表是向前超出范围的，将回到后面；亦而反之。这是通过修改num实现的。修正之后，将密文保存到output。
            if num>25:
                num=int(num%26)
            if num<-25:
                num=int(-(-num%26))
            output=alphabet_upper[num]
        except ValueError:
        #如果发生了ValueError，则说明这不是一个英文字母(无论是alphabet或alphabet_upper都不存在该字母)。那么，这个字符将不会被加密，直接保存到output。
            output=plain[times-1]
    except IndexError:
    #如果发生了IndexError，则说明这是一个小写字母，但是列表超出范围。那么，如果列表是向前超出范围的，将回到后面；亦而反之。这是通过修改num实现的。修正之后，将密文保存到output。
        if num>25:
            num=int(num%26)
        if num<-25:
            num=int(-(-num%26))
        output=alphabet[num]
  
    #最终，将保存在output中的密文输出。
    print(output,end='')
    #由于是循环输出，每次都会换行，将导致输出的密文难以阅读。因此用end=''选项不换行。
  
#由于不换行，最后一行看着很难受，故换一行。
print("")
