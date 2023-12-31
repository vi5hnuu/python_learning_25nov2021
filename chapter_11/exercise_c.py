portfolio={
    'accounts':['sbi','iob'],
    'shares':['hdfc','icici','tm','tcs'],
    'ornaments':['10gm gold','1kg silver']
}
portfolio['mf']=['relience','absl']
print(portfolio)

portfolio['accounts']=['axis','bob']
print(portfolio)

lst=portfolio['shares']
portfolio['shares']=sorted(lst)
print(portfolio)

del(portfolio['ornaments'])
print(portfolio)