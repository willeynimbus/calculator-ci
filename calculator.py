def lambda_handler(event, context):
    operation = event.get('operation')
    a = event.get('a')
    b = event.get('b')

    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    else:
        return 'Invalid operation'
