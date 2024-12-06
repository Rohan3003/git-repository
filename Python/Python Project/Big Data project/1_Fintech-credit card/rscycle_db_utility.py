def read_table(spark, connection_str: DbConfig, table_name, env=None):
    """Creating a Dataframe from PostgreSQL table using specified DB Config Object"""
    host = permision_for_read_write(connection_str, env)
    try:
        df = (
            spark.read.format("jdbc")
            .option(
                "url", db_constants.jdbc_post_url + host + "/" + db_constants.database
            )
            .option("driver", db_constants.driver)
            .option("dbtable", db_constants.schema + "." + str(table_name))
            .option("user", connection_str["username"])
            .option("password", connection_str["password"])
            .load()
        )
        logger.info("Reading table successful :" + table_name)
    except Exception as e:
        logger.info("read_table Error: Spark Dataframe creation failed")
        raise f"read_table Error: Spark Dataframe creation failed - " + e
    return df