from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME= "Data Ingestion stage"

try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed \n")
except Exception as e:
    logger.exception(e)
    raise e


logger.info("welcome to our custom login")