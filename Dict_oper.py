cameras = {'canon': 200, 'sony': 300}
print(cameras)

cameras.update({'samsung': 500})
print(cameras)

cameras['xyz'] = 100
print(cameras)

print(cameras['xyz'])

print(cameras.keys())
print(cameras.values())
print(cameras.items())

