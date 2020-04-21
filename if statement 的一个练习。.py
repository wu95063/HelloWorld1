#练习：
#房子的价格是100万
#如果购房客户的信用良好，则客户只需要交付总房款的30%
#否则，购房客户需要交付总放款的60%
#请写出客户的首付款为多少。
price=1000000
credit_good=True
if credit_good:
    print(f'Your down_payment:{price*0.3} ')
else:
    print(f'Your down_payment:{price*0.6}')