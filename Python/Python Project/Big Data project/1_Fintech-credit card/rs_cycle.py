def webcon_method(self,spark):
            "Reading card input"
            if self.get_card_input_json["RSWEBCON"]["PRTPAR"] == "Y":
                print("FLAG80 = TRUE")

            "Reading date card input"
            CARD_DATE = self.get_card_input_json["RSWEBCON"]["INPDT"]

            "Convert the string to a datetime object"
            date_obj = datetime.strptime(CARD_DATE, "%Y%m%d")

            "Format the datetime object into yyyy-MM-dd"
            formatted_date = date_obj.strftime("%Y-%m-%d")

            # Reading table from text file into dataframe
            df_webc = spark.read.text(self.source_path + self.get_job_json["RSWEBCON"]["WEBC_SRC_FILE"])
            file_schema = self.get_job_json['RSWEBCON']['RSWEBC_FILE_SCHEMA']
            df_webc = rscycle_spark_config.convert_texttodataframe(df_webc, file_schema)
            df_webc.show(5)

            # Reading table from postgresSQL into dataframe
            df_rscens = rscycle_db_utility.read_table(spark, self.connection_string, self.get_job_json['RSWEBCON']['TBL_RSCENS'])
            df_plan = rscycle_db_utility.read_table(spark, self.connection_string, self.get_job_json['RSWEBCON']['TBL_RSPLAN'])
            df_rscnflg = rscycle_db_utility.read_table(spark, self.connection_string, self.get_job_json['RSWEBCON']['TBL_RSCNFLG'])
            df_rsconf = rscycle_db_utility.read_table(spark, self.connection_string, self.get_job_json['RSWEBCON']['TBL_CONF'])
            df_rstpafl=rscycle_db_utility.read_table(spark, self.connection_string, self.get_job_json['RSWEBCON']['TBL_RSTPA'])

            df_webc= df_webc.filter(df_webc["rtype3"]!="HDR")
            df_webc = df_webc.filter(F.col("PLAN")!= "AAAA")