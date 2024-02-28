class CommonData:
    def __init__(self):
        self.Common_data = {
            "data": object,
            "success": True,
            "status": 200,
            "msg": ""
        }

    def is_success(self, data, msg):
        self.Common_data["data"] = data
        self.Common_data["success"] = True
        self.Common_data["status"] = 200
        self.Common_data["msg"] = msg
        return self.Common_data

    def erro_data(self, status, msg):
        self.Common_data["data"] = object
        self.Common_data["status"] = status
        self.Common_data["success"] = False
        self.Common_data["msg"] = msg
        return self.Common_data

    def Get_Common_data(self):
        return self.Common_data

