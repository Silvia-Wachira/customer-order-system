from django.apps import AppConfig
# from core.order.viewsets import SendSMS


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.order'
    label = 'core_order'


# #TODO: create incoming messages route
# @app.route('/incoming-messages', methods=['POST'])
# def incoming_messages():
#    data = request.get_json(force=True)
#    print(f'Incoming message...\n ${data}')
#    return Response(status=200)

# #TODO: create delivery reports route.
# @app.route('/https://null/delivery-reports', methods=['POST'])
# def delivery_reports():
#    data = request.get_json(force=True)
#    print(f'Delivery report response...\n ${data}')
#    return Response(status=200) 
