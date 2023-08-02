def check_sum(*args):
    return 'not enough' if len(args) < 50 else 'verification passed'

print(check_sum(8,11))