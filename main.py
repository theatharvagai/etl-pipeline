import logging
import sys
from etl.pipeline import run_pipeline

# Setup logging for the main entry point
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("pipeline.log")
    ]
)
logger = logging.getLogger(__name__)

def main():
    """
    Main entry point for the Financial ETL Pipeline.
    """
    logger.info("==========================================")
    logger.info("Initializing Financial ETL Pipeline")
    logger.info("==========================================")
    
    try:
        run_pipeline()
        logger.info("Process finished successfully.")
    except KeyboardInterrupt:
        logger.warning("Pipeline interrupted by user.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Critical error during pipeline execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
