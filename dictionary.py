#key value şeklinde çalışır
#örneğin 34 bilgisi bizi istanbul a götürür
# sehirler = ['kocaeli', 'istanbul']
# plakalar = [41,34]
# # print(plakalar[sehirler.index('istanbul')])
# plakalar  = {'kocaeli':41 , 'istanbul':34}
# print (plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6

# plakalar['kocaeli'] = 'new value'
# print(plakalar)

users = {
     'fatma akpunar' :{
        'age':22,
        'roles':['user'],
        'email':'fatmaakpunar42@gmail.com',
        'address':'istanbul',
        'phone':'0534 391 28 24'
     } , 
      'merve akpunar' :{
        'age':18,
        'roles':['admin','user'],
        'email':'meveakpunar234@gmail.com',
        'address':'istanbul',
        'phone':'0542 987 56 70'
      }
   
}
print(users['fatma akpunar']['age'])