from django.http import HttpResponse


class StripeWH_Handler:
    ''' Handle Strpie Webhooks '''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        ''' Hanlde a generic/unknown/unexpected webhook event '''
        return HttpResponse(
            content=f'Unhandled webhook received {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        ''' Hanlde the payment_intent.succeed webhook from stripe '''
        return HttpResponse(
            content=f'Webhook received {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        ''' Hanlde the payment_intent.payment_failed webhook from stripe '''
        return HttpResponse(
            content=f'Payment failed Webhook received {event["type"]}',
            status=200)
