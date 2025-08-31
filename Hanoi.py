def Hanoi(n,frompeg,topeg,auxpeg):
    if n == 1:
        print(f"Move disk 1 from {frompeg} to {topeg}")
        return
    Hanoi(n-1, frompeg, auxpeg, topeg)
    print(f"Move disk {n} from {frompeg} to {topeg}")
    Hanoi(n-1, auxpeg, topeg, frompeg)

def Hanoi_stack(n, frompeg, topeg, auxpeg):
    from_stack = list(range(n, 0, -1))  
    to_stack = []
    aux_stack = []
    
    total_moves = 2**n - 1
    move_count = 0    
    if n % 2 == 0:
        topeg, auxpeg = auxpeg, topeg

    while move_count < total_moves:
        if move_count % 3 == 0:
            if from_stack and (not to_stack or from_stack[-1] < to_stack[-1]):
                disk = from_stack.pop()
                to_stack.append(disk)
                print(f"Move disk {disk} from {frompeg} to {topeg}")
            else:
                disk = to_stack.pop()
                from_stack.append(disk)
                print(f"Move disk {disk} from {topeg} to {frompeg}")
        
        elif move_count % 3 == 1:
            if from_stack and (not aux_stack or from_stack[-1] < aux_stack[-1]):
                disk = from_stack.pop()
                aux_stack.append(disk)
                print(f"Move disk {disk} from {frompeg} to {auxpeg}")
            else:
                disk = aux_stack.pop()
                from_stack.append(disk)
                print(f"Move disk {disk} from {auxpeg} to {frompeg}")

        else:
            if aux_stack and (not to_stack or aux_stack[-1] < to_stack[-1]):
                disk = aux_stack.pop()
                to_stack.append(disk)
                print(f"Move disk {disk} from {auxpeg} to {topeg}")
            else:
                disk = to_stack.pop()
                aux_stack.append(disk)
                print(f"Move disk {disk} from {topeg} to {auxpeg}")

        move_count += 1
Hanoi_stack(5, 'A', 'C', 'B')