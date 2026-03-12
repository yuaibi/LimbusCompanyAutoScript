from scheduler.scheduler import Scheduler
from utils.logger import logger

def main():

    logger.info("Starting bot...")

    scheduler = Scheduler()
    scheduler.run()

if __name__ == "__main__":
    main()