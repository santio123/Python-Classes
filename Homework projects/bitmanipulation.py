def solve_circuit(a, b):
    gate_and = a & b
    gate_or  = a | b
    gate_xor = a ^ b
    gate_not = ~a & 1

    get_bit    = (a >> 1) & 1
    set_bit    = a | (1 << 1)
    clear_bit  = a & ~(1 << 1)
    toggle_bit = a ^ (1 << 1)

    return gate_and, gate_or, gate_xor, gate_not

if __name__ == "__main__":
    val_a, val_b = 1, 0
    print(solve_circuit(val_a, val_b))