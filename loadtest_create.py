from locust import HttpUser, task, between
import gevent.monkey
import random

gevent.monkey.patch_all()


class GeventApiUser(HttpUser):
    wait_time = between(3, 7)
    
    @task
    def get_users(self):
        random = random_number()
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
            "document": { "CI": random,
                        "name": "John",
                        "surname": "Sample",
                        "age": 42 }
                    }
        response = self.client.post(
            'https://sa-east-1.aws.data.mongodb-api.com/app/data-rakua/endpoint/data/v1/action/insertOne', 
            headers=headers, 
            json=body
        )
        print(f"Response: {response.text}")

        # response = self.client.post("https://sa-east-1.aws.data.mongodb-api.com/app/data-rakua/endpoint/data/v1")
        # print(f"Response: {response.text}")


def random_number() -> int:
    return random.randint(1, 99999999)


GeventApiUser.GEVENT_SUPPORT = True