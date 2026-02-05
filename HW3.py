arrival_time: int = int(input('how much time it took for the meal to arrive? '))
price: int = int(input('what was the price? '))
is_quick_service: bool = arrival_time < 15
is_expensive: bool = price > 100
if is_quick_service and not is_expensive:
    print('recommended')
else:
    print('not recommended')