from discord_webhook import DiscordWebhook
import os
import random

MESSAGES_TO_SEND = 50

def webhook(filename):
    webhooks = []
    with open(filename, 'r') as file:
        for line in file:
            webhook_url = line.strip()
            if webhook_url.startswith("https://discord.com/api/webhooks/"):
                webhooks.append(webhook_url)
    return webhooks

def spam(message, webhooks):
    for _ in range(MESSAGES_TO_SEND):
        webhook_url = random.choice(webhooks)
        webhook = DiscordWebhook(url=webhook_url, content=message)
        response = webhook.execute()
        print(f"Message sent to {webhook_url} ({_+1}/{MESSAGES_TO_SEND})")

def main():
    filename = "webhook.txt"
    if not os.path.isfile(filename):
        print("Webhook file not found.")
        return

    webhooks = webhook(filename)
    if not webhooks:
        print("No valid webhooks found in the file.")
        return

    message = input("Enter the message to send: ")
    spam(message, webhooks)

if __name__ == "__main__":
    main()
