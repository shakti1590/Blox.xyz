bank_a = {
    "user1": 3000,
    "user2": 400,
}

bank_b = {
    "user3": 900,
    "user4": 1500,
    # Add more
}
def transfer_money(sender_bank, sender_account, receiver_bank, receiver_account, amount):
    sender_balance = sender_bank_accounts.get(sender_account)
    if sender_balance is None or sender_balance < amount:
        return False, "Insufficient balance"
    sender_bank_accounts[sender_account] -= amount
    receiver_balance = receiver_bank_accounts.get(receiver_account)
    if receiver_balance is None:
        receiver_bank_accounts[receiver_account] = amount
    else:
        receiver_bank_accounts[receiver_account] += amount
    return True, "Transfer successful"
sender_bank_accounts = bank_a
receiver_bank_accounts = bank_b
sender_account = "user1"
receiver_account = "user3"
amount = 200
success, message = transfer_money(
    sender_bank_accounts, sender_account, receiver_bank_accounts, receiver_account, amount)
print(message)
