# from datetime import datetime
# import requests


# url="http://127.0.0.1:5001/geo/findCenterAndRadius/"
# data=[
#     {
#         "X":0,
#         "Y":0,
#         "Z":1
#     },
#     {
#         "X":10,
#         "Y":10,
#         "Z":1
#     },
#     {
#         "X":10,
#         "Y":10,
#         "Z":1
#     }
# ]
# a=datetime.now()
# for i in range(1,100):
#     result=requests.post(url,json=data)
#     print(result.text,"---",i)

# b=datetime.now()

# print(a,"++++",b)