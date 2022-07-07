def evaluate(expression):
    try:
        result = str(eval(expression))
    except Exception:
        return 'ERROR'
    return result
