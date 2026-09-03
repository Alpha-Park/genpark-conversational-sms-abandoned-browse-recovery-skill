from client import ConversationalSmsAbandonedBrowseRecoveryClient

def main():
    client = ConversationalSmsAbandonedBrowseRecoveryClient()
    res = client.generate_sms_recovery_prompt('Jordan', 'Wireless ANC Earbuds', 2)
    print('SMS Abandoned Browse Recovery: ' + res['campaign_message_id'])
    print('Message: "' + res['sms_body_text'] + '"')
    print('Preview URL: ' + res['campaign_preview_url'])

if __name__ == '__main__':
    main()
