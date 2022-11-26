s = '>lmaooo >About 265,032,704 search results<'
position = s.index('>About')
position2 = s.index('search results<')
print(position, position2)
print(s[position+7:position2])