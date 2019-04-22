from pyfcm import FCMNotification
 
push_service = FCMNotification(api_key="AAAA2nQVSHY:APA91bHtvk7-KIs5tNzTSL0nM6oiVflIDScUEii68sToMmbMzItnn9YGK-BWCUTN-AzmwgdYvJObeGXXhD4qEQfJ5CkKFDJ6vcQhDuo_j6Fd8EdrcxLAS5mj6agxQw5gOAqZ4Kknja0c")
 
# OR initialize with proxies
 
proxy_dict = {
          "http"  : "http://127.0.0.1:8899",
          "https" : "http://127.0.0.1:8899",
        }
push_service = FCMNotification(api_key="AAAA2nQVSHY:APA91bHtvk7-KIs5tNzTSL0nM6oiVflIDScUEii68sToMmbMzItnn9YGK-BWCUTN-AzmwgdYvJObeGXXhD4qEQfJ5CkKFDJ6vcQhDuo_j6Fd8EdrcxLAS5mj6agxQw5gOAqZ4Kknja0c", proxy_dict=proxy_dict)
 
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
 
registration_id = "cqXjukfFN2w:APA91bEKWYkk22XlZeeioYAhWIViljfVJcF31wlDxnOPOxAy1hSVOKAe2odC9t9x6MH02pUwGnKYcIN990khnHclFzblGbAcB0Qw7v9zAZEglfAyxP6MXedrrkEL-dXuVY-zHHhVUmFp"
message_title = "淹水警報！"
message_body = "高雄地區正在淹水 請盡速撤離"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
 
print(result)
 
# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
 
# print result