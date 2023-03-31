#Breanna Eafon
def count_hashtag(string,substring):
    count=0
    for ch in string:
        if ch== substring:
            count+=1
    return count

def hash_spam(x):
    if count_hashtag(x,"#")>=4:
        return ("this tweet will  be considered as a spam!")
    else:
        return none


print(hash_spam("hello####,#"))
