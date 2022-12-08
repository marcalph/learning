sent_mails = []
def send_email(recipient='recipient', subject='subject', body='body', unwanted_prm="unwanted"):
    sent_mails.append((recipient, subject, body, unwanted_prm))
    print(sent_mails)
    return False


def commit_order(transaction):
    send_email(subject=f"Your order number {transaction.transaction_id}", body="Thank you for buying...")