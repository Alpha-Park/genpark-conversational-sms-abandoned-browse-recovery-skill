class ConversationalSmsAbandonedBrowseRecoveryClient:
    def generate_sms_recovery_prompt(self, customer_first_name='Alex', viewed_product='Hydro-Shield Insulated Parka', inventory_left=4):
        body = 'Hey Alex, noticed you were checking out the Hydro-Shield Parka! Only ' + str(inventory_left) + ' units remain in your size. Reply YES to reserve with 10% VIP discount.'
        return {
            'campaign_message_id': 'sms_rcv_5519',
            'sms_body_text': body,
            'urgency_framing': 'SCARCITY_LOW_STOCK',
            'one_click_checkout_link': 'https://checkout.attentive.genpark.ai/c/5519',
            'tcpa_compliant_optout_included': True,
            'projected_conversion_rate_pct': 18.6,
            'campaign_preview_url': 'https://postscript.sms.genpark.ai/previews/5519.json'
        }
