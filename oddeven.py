def Split(mix):
    even_li = []
    odd_li = []
    for i in mix:
        if (i % 2 == 0):
            even_li.append(i)
        else:
            odd_li.append(i)
    print("Even Numbers:", even_li)
    print("Odd Numbers:", odd_li)
mix = [4, 65, 48, 56, 41, 93, 56, 5, 7]
Split(mix)