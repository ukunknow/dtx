def generate_ticket_code(N):
    if N == 1:
        return "A"

    prev_ticket_code = "A"
    for i in range(2, N + 1):
        new_ticket_code = ""
        count = 1
        for j in range(1, len(prev_ticket_code)):
            if prev_ticket_code[j] == prev_ticket_code[j - 1]:
                count += 1
            else:
                new_ticket_code += str(count) + prev_ticket_code[j - 1]
                count = 1
        new_ticket_code += str(count) + prev_ticket_code[-1]
        prev_ticket_code = new_ticket_code

    return prev_ticket_code

N = int(input())

result = generate_ticket_code(N)
print(result)
