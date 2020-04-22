#在有多种情况下使用逻辑运算符。
#举个例子：
#（1）买车贷款，信誉良好，and 有较高收入，才能获得贷款。
#（2）买车贷款，信誉良好，or 有较高收入，才能获得贷款。
#（3）买车贷款，信誉良好，没有（not）犯罪记录的情况下，才能获得贷款。
has_good_credit=True
has_good_income=True
if has_good_credit and has_good_income:
    print('可以申请贷款')
else:
    print('不能申请贷款')
#（2）
has_good_credit=False
has_good_income=False
if has_good_credit or has_good_income:
    print('可以申请贷款')
else:
    print('不能申请贷款')
#（3）
has_good_credit=True
has_criminal_record=False
if has_good_credit and not has_criminal_record:
    print('可以申请贷款')
