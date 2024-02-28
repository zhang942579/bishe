from common.commondata import CommonData
from DBService.DBOperate import DBOperate


class DataDisplayServer:

    def __init__(self):
        self.CommonData = CommonData()
        self.DBOperate = DBOperate()

    def answers_Display(self):
        result = self.DBOperate.answers_stati_allSelect()
        total = self.DBOperate.module_stati_select("answers")
        if result and total:
            data_results = []
            for data in result:
                data_result = {
                    "id": data[1],
                    "number_uses": data[2],
                    "proportion": round(data[2]/total[2], 2)
                }
                data_results.append(data_result)

            return self.CommonData.is_success(data_results, "成功")
        else:
            return self.CommonData.erro_data(500, "数据更新失败")

    def clothing_Display(self):
        result = self.DBOperate.clothing_stati_allSelect()
        total = self.DBOperate.module_stati_select("clothing")
        if result and total:
            data_results = []
            for data in result:
                data_result = {
                    "id": data[1],
                    "number_uses": data[2],
                    "proportion": round(data[2]/total[2], 2)
                }
                data_results.append(data_result)

            return self.CommonData.is_success(data_results, "成功")
        else:
            return self.CommonData.erro_data(500, "数据更新失败")

    def posture_Display(self):
        result = self.DBOperate.posture_stati_allSelect()
        total = self.DBOperate.module_stati_select("posture")
        if result and total:
            data_results = []
            for data in result:
                data_result = {
                    "id": data[1],
                    "number_uses": data[2],
                    "proportion": round(data[2]/total[2], 2)
                }
                data_results.append(data_result)

            return self.CommonData.is_success(data_results, "成功")
        else:
            return self.CommonData.erro_data(500, "数据更新失败")

    def scene_Display(self):
        result = self.DBOperate.scene_stati_allSelect()
        total = self.DBOperate.module_stati_select("scene")
        if result and total:
            data_results = []
            for data in result:
                data_result = {
                    "id": data[1],
                    "number_uses": data[2],
                    "proportion": round(data[2]/total[2], 2)
                }
                data_results.append(data_result)

            return self.CommonData.is_success(data_results, "成功")
        else:
            return self.CommonData.erro_data(500, "数据更新失败")