from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


logger.info("welcome to our custom login")



STAGE_NAME= "Data Ingestion stage"

try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed \n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Validation stage"
try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<")
    data_validation= DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed \n")
except Exception as e:
    logger.exception(e)
    raise e

