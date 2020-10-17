import requests

topics = ['set-union',
          'set-difference', 'set-symmetric-difference',
          'cartesian-product', 'set-partition',
          'set-complement']
params = ['1', '2', '3', '4', '5', '6', '7']

param = ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '31', '32', '33', '34',
         '35', '36', '37', '41', '42', '43', '44', '45', '46', '47', '51', '52', '53', '54', '55', '56', '57', '61',
         '62', '63', '64', '65', '66', '67', '71', '72', '73', '74', '75', '76', '77']

param_intersection = ['11', '22', '33', '44', '55', '66', '77']
# for i in params:
#     for j in params:
#         param.append(i+j)
#
# print(param)
status_codes_list = []


for p in param:
    for i in range(20):
        x = requests.get('http://127.0.0.1:5000/' + 'set-complement' + '/' + str(i) + '/' + p)
        status_codes_list.append(x.status_code)
        if x.status_code is not 200:
            print('Error : ' + str(x.status_code))


# for p in param_intersection:
#     for i in range(20):
#         x = requests.get('http://127.0.0.1:5000/' + 'set-intersection' + '/' + str(i) + '/' + p)
#         status_codes_list.append(x.status_code)
#         if x.status_code is not 200:
#             print('Error : ' + str(x.status_code))


