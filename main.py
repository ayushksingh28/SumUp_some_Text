from textSummarizer.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from textSummarizer.pipelines.stage_02_data_validation import DataValidationTrainingPipeline
#from textSummarizer.pipelines.stage_03_data_transformation import DataTransformationTrainingPipeline
#from textSummarizer.pipelines.stage_04_model_trainer import ModelTrainerTrainingPipeline
#from textSummarizer.pipelines.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e