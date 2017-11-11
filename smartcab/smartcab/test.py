def get_maxQ(Q, state):

    maxQ = max(Q.get(str(state)).items(), key=lambda x: x[1])

    return maxQ

Q={
    '1':{'first':1,'second':1,'third':1},
    '2':{'first':1,'second':2,'third':3},
    '3':{'first':1,'second':2,'third':3}
     }

print 'hello'
print get_maxQ(Q, 1)