import logging

def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """Sets up a logger with the specified name, log file, and logging level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create file handler which logs messages to the specified file
    fh = logging.FileHandler(log_file)
    fh.setLevel(level)
    
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(fh)
    
    return logger