a=[1,2,'srt',4,'rtr',0,'wewe']
def fun():
    for i in a:
        if type(i)==str and len(i)%2==1:
            yield i
print(list(fun()))
