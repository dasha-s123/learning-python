def send_messages(list_full, list_empty):
    """перемещает сообщения, отправляет их"""

    # Цикл последовательно отправляет сообщения
    # А затем перемещает их в список отправленных сообщений
    while list_full:
        message = list_full.pop()
        print(message)
        list_empty.append(message)


messages_to_send = ['I love python', 'My name is dasha', 'I read a book rn']
sent_messages = []

send_messages(list_full=messages_to_send, list_empty=sent_messages)
print(f'\n{messages_to_send}')
print(sent_messages)