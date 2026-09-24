def ft_seed_inventory(seed_type: str, quantity: int , unit:str ) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(seed_type , "seeds :", quantity , unit , "available")
    elif unit == "grams":
        print(seed_type ,"seeds :", quantity , unit , "total")
    elif  unit == "area":
        print(seed_type , "seeds : covers", quantity , unit , "sqaure meters")
    else:
        print("Unknown unit type")

ft_seed_inventory("carrot", 8, "grams")
