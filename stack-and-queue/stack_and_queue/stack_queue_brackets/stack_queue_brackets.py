from stack_and_queue.stack import Stack

def validate_brackets(brackets_str):
    stack_brackets = Stack()
    left_brackets = ['(','[','{']
    right_brackets = [')',']','}']
    stack_had_brackets = False

    for ch in brackets_str:
        if ch in left_brackets:
            stack_brackets.push(ch)
            stack_had_brackets = True
        
        if ch in right_brackets:
             if not stack_brackets.is_empty():
                
                bracket = stack_brackets.pop()
                if right_brackets.index(ch) != left_brackets.index(bracket):
                    return False
                else:
                    continue
             else:
                return False
    if stack_had_brackets:
        if stack_brackets.is_empty():
            return True
        else:
            return False
    return False

                
if __name__ == "__main__":
    print(validate_brackets('{}'))
    print(validate_brackets('{}(){}'))
    print(validate_brackets('()[[Extra Characters]]'))
    print(validate_brackets('(){}[[]]'))
    print(validate_brackets('{}{Code}[Fellows](())'))
    print(validate_brackets('[({}]'))
    print(validate_brackets('(]('))
    print(validate_brackets('{(})'))
    print(validate_brackets('{'))
    print(validate_brackets(')'))
    print(validate_brackets('[}'))



    

