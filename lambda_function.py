import json


def handler(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


#
# def lambda_handler(event, context):
#     try:
#         print(f"Event : {event} \n")
#         if event.get('resource') == '/search/{proxy+}':
#             return handle_search(event, context)
#         elif event.get('resource') == '/tehilim':
#             return handle_tehilim(event, context)
#     except Exception as e:
#         print(e)
#         return {
#             'statusCode': 404,
#             'body': str(e)
#         }
#
#
# def model_answer(body):
#     return {
#         'statusCode': 200,
#         'headers': {
#             'Access-Control-Allow-Headers': 'Content-Type',
#             'Access-Control-Allow-Origin': '*',
#             'Access-Control-Allow-Methods': 'OPTIONS,GET'
#         },
#         'body': body
#     }
#
#
#
# def handle_search(event, context):
#     params = event.get('queryStringParameters')
#
#     mode = params.get('mode')
#     word = params.get('word')
#     parasha = params.get('parasha')
#     print(f'{datetime.datetime.now()} - mode - {mode} word {word}')
#     secret = params.get('secret', 'coco')
#     step = params.get('step', 1)
#     step_range = params.get('range', False)
#     if parasha:
#         logger.info("Running parasha stat")
#         from src.aliyot import Aliyot
#         body = Aliyot().get_stat(parasha=parasha)
#         # import pandas
#         # logger.info("Pandas imported !")
#         #
#         # return model_answer({"verison": pandas.__version__})
#         print('Answer')
#         print(body)
#
#         return model_answer(json.dumps(body))
#     if step_range:
#         all_step_response = dict()
#         for _step in range(1, step):
#             all_step_response[_step] = word_search(word=word, mode=mode, step=step, secret=secret)
#         body = json.dumps(all_step_response)
#     else:
#         response = word_search(word=word, mode=mode, step=step, secret=secret)
#         body = json.dumps(response)
#
#         print(body)
#     return model_answer(body)


handler(None, None)
