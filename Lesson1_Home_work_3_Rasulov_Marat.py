for n in range(1, 101):
    def transform_string(number: int) -> str:
        ending = number % 10
        if 10 <= number < 21 or ending >= 5 or ending ==0:
            format_string = f'{number} процентов'
        elif ending == 1:
            format_string = f'{number} процент'
        else:
            format_string = f'{number} процента'
        return format_string
    print(transform_string(n))



