x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if x>0 and y>0 and z>0:
    print('3 ta musbat.')
elif (x>0 and y<0 and z<0) or (x<0 and y>0 and z<0) or (x<0 and y<0 and z>0):
    print('1 ta musbat. 2 ta manfiy.')
elif (x>0 and y>0 and z<0) or (x<0 and y>0 and z>0) or (x>0 and y<0 and z>0):
    print('2 ta musbat. 1 manfiy.')
else:
    print('3 ta manfiy.')