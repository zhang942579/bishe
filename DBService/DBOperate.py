from DBService.DBConnect import ExecSql


class DBOperate:

    def __init__(self):
        self.execSql = ExecSql()

    def answers_stati_select(self, answers_id):

        query = "SELECT * FROM answers_stati WHERE answers_id = " + answers_id

        return self.execSql.exec_sql("select_one", query)

    def answers_stati_update(self, answers_id):
        query = "update answers_stati set number_uses =  number_uses+1 where answers_id= " + answers_id

        return self.execSql.exec_sql("update", query)

    def answers_stati_allSelect(self):
        query = "SELECT * FROM answers_stati"
        return self.execSql.exec_sql("select_list", query)

    def clothing_stati_select(self, clothing_id):

        query = "SELECT * FROM clothing_stati WHERE clothing_id = " + clothing_id

        return self.execSql.exec_sql("select_one", query)

    def clothing_stati_update(self, clothing_id):
        query = "update clothing_stati set number_uses =  number_uses+1 where clothing_id= " + clothing_id

        return self.execSql.exec_sql("update", query)

    def clothing_stati_allSelect(self):
        query = "SELECT * FROM clothing_stati"
        return self.execSql.exec_sql("select_list", query)

    def posture_stati_select(self, posture_id):

        query = "SELECT * FROM posture_stati WHERE posture_id = " + posture_id

        return self.execSql.exec_sql("select_one", query)

    def posture_stati_update(self, posture_id):
        query = "update posture_stati set number_uses =  number_uses+1 where posture_id= " + posture_id

        return self.execSql.exec_sql("update", query)

    def posture_stati_allSelect(self):
        query = "SELECT * FROM posture_stati"
        return self.execSql.exec_sql("select_list", query)

    def scene_stati_select(self, scene_id):

        query = "SELECT * FROM scene_stati WHERE scene_id = " + scene_id

        return self.execSql.exec_sql("select_one", query)

    def scene_stati_update(self, scene_id):
        query = "update scene_stati set number_uses =  number_uses+1 where scene_id= " + scene_id

        return self.execSql.exec_sql("update", query)

    def scene_stati_allSelect(self):
        query = "SELECT * FROM scene_stati"
        return self.execSql.exec_sql("select_list", query)

    def module_stati_select(self, module_id):

        query = f"SELECT * FROM module_stati WHERE module_id = '{module_id}'"

        return self.execSql.exec_sql("select_one", query)

    def module_stati_update(self, module_id):
        query = f"update module_stati set number_uses_total =  number_uses_total+1 where module_id='{module_id}'"

        return self.execSql.exec_sql("update", query)

    def module_stati_allSelect(self):
        query = "SELECT * FROM module_stati"
        return self.execSql.exec_sql("select_list", query)