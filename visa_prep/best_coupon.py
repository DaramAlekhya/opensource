bill_amount = int(input())
discount1 = bill_amount * 0.1
discount2 = 100
max_discount = max(discount1, discount2)
final_amount = bill_amount - max_discount
print(final_amount)
