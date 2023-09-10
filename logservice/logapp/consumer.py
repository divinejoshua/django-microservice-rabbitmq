import json
import pika
import threading
ROUTING_KEY = 'user.created.key'
EXCHANGE = 'user_exchange'
THREADS = 5
QUEUE_NAME = "logg_user_action"

class UserCreatedListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct')
      
        result = self.channel.queue_declare(queue=QUEUE_NAME, exclusive=True)
        queue_name = result.method.queue
        
        self.channel.queue_bind(queue=queue_name, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        self.channel.basic_qos(prefetch_count=THREADS*10)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback)
        
    def callback(self, channel, method, properties, body):

        # Get message content 
        if(properties.content_type=="user_created_method"):
            message = json.loads(body)
            userDetails = json.loads(message)

            # Perform any action with the message here 
            print("Log : "+userDetails["email"]+ " user registered")

        channel.basic_ack(delivery_tag=method.delivery_tag)
        
    def run(self):
        print ('Inside LogginService:  Created Listener ')
        self.channel.start_consuming()
    
   