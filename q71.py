#breanna Eafon
def count_hashtag(string,substring):
    count=0
    for ch in string:
        if ch== substring:
            count+=1
    return count

count_hashtag("hello#", "#")
