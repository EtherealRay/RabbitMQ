import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.queue_declare(queue='hello123')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!!!!!!!!!21!!!!!!')

channel.basic_publish(exchange='',
                      routing_key='hello123',
                      body='Hello World 123')


print(" [x] Sent 'Hello World!' ")

connection.close()

