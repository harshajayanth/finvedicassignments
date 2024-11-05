def luhn_check(card_number):
    card_number = str(card_number)[::-1]
    total = 0
    
    for i, digit in enumerate(card_number):
        n = int(digit)
        
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9 
        
        total += n
    
    return total % 10 == 0

# Example usage
if __name__ == "__main__":
    card_number = input("Enter a credit card number: ")
    
    if luhn_check(card_number):
        print("The credit card number is valid.")
    else:
        print("The credit card number is invalid.")
