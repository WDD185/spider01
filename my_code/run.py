from get_static import GetGlobalStatic,GetAreaStatic


class Main:
    def __init__(self):
        self.op1 = GetGlobalStatic()
        self.op2 = GetAreaStatic()

    def run_country_start(self):
        self.op1.start()

    def run_country_eight(self):
        self.op1.analysis_eight_mouth()

    def run_province_start(self):
        self.op2.start()

    def run_province_eight(self):
        self.op2.analysis_eight_mouth()


if __name__ == '__main__':
    Main().run_province_eight()
