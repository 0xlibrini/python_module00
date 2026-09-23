
def helper_count(i , number):
    if i == number + 1:
        return
    print(i)
    helper_count(i + 1, number)
     
        
    

def ft_count_harvest_recursive():
    number = int(input("Days until harvest: "))
    helper_count(1, number)


ft_count_harvest_recursive()