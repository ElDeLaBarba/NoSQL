from locust import HttpUser, task, between
import gevent.monkey

gevent.monkey.patch_all()

class GeventApiUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_users(self):
        headers = {
            "Content-Type": "application/json",
            "Access-Control-Request-Headers": "*",
            "api-key": "6cG4xVaAQtDzS2qifzr14hzdwpR4nlvd8hbdjuQSGDVWE1E20skRxi04qnZZAVFS",
            "Accept": "application/json"
        }
        body = {
            "dataSource": "Cluster0",
            "database": "NoSQL",
            "collection": "Personas",
            "filter": { "age": { "$lt": 1000 } }
        }
        response = self.client.post(
            'https://sa-east-1.aws.data.mongodb-api.com/app/data-rakua/endpoint/data/v1/action/find', 
            headers=headers, 
            json=body
        )
        print(f"Response: {response.text}")

        # response = self.client.post("https://sa-east-1.aws.data.mongodb-api.com/app/data-rakua/endpoint/data/v1")
        # print(f"Response: {response.text}")

GeventApiUser.GEVENT_SUPPORT = True