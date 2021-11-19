from stack_and_queue.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_validate_brackets_return_true():
    assert validate_brackets('{}{Code}[Fellows](())') == True

def test_validate_brackets_return_false():
    assert validate_brackets('{') == False

def test_validate_brackets_return_false():
    assert validate_brackets('[({}]') == False

def test_validate_brackets_return_false_for_one_chr_str():
    assert validate_brackets('[') == False

def test_validate_brackets_return_true_for_two_chrs_str():
    assert validate_brackets('{}') == True