def lucky_ticket(ticket_number):
    
    ticket_number = repr(ticket_number)
    left_sum = ticket_number[:3]
    right_sum = ticket_number[-3:]
 
    def leftright_sum(plus_part):
        counter = 0
        for n in plus_part:
            counter += int(n)
        return counter
 
    if leftright_sum(left_sum) == leftright_sum(right_sum):
        return True
    else:
        return False
 
print(lucky_ticket(445544))
print(lucky_ticket(789858))
print(lucky_ticket(421430))