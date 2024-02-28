from common.commondata import CommonData
from DBService.DBOperate import DBOperate


class DataStatistics:
    def __init__(self):
        self.CommonData = CommonData()
        self.DBOperate = DBOperate()

    def answers_increase(self, answers_id):
        result = self.DBOperate.answers_stati_update(answers_id)
        results = self.DBOperate.module_stati_update("answers")

        if result and results:
            return self.CommonData.is_success([result, results], "成功")
        else:
            return self.CommonData.erro_data(500, "数据更新失败")

    def clothing_increase(self, clothing_id):
        result = self.DBOperate.clothing_stati_update(clothing_id)
        results = self.DBOperate.module_stati_update("clothing")
        if result & results:
            return self.CommonData.is_success([result, results], "成功")
        else:
            return self.CommonData.erro_data(500, "数据更新失败")

    def posture_increase(self, posture_id):
        result = self.DBOperate.posture_stati_update(posture_id)
        results = self.DBOperate.module_stati_update("posture")
        if result & results:
            return self.CommonData.is_success([result, results], "成功")
        else:
            return self.CommonData.erro_data(500, "数据更新失败")

    def scene_increase(self, scene_id):
        result = self.DBOperate.scene_stati_update(scene_id)
        results = self.DBOperate.module_stati_update("scene")
        if result & results:
            return self.CommonData.is_success([result, results], "成功")
        else:
            return self.CommonData.erro_data(500, "数据更新失败")

