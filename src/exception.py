from src.logger import logging
import sys

def error_message_detail(error, error_detail: sys):
    """
    Formats detailed error messages with the file name, line number, and error message.
    """
    _, _, tb = error_detail.exc_info()  # Correctly access sys.exc_info()
    if tb is not None:
        file_name = tb.tb_frame.f_code.co_filename
        line_number = tb.tb_lineno
        error_message = (
            f"Error occurred in python script [{file_name}] "
            f"at line number [{line_number}] with error message [{error}]"
        )
        return error_message
    else:
        return f"Error occurred: {error} (no traceback available)"

class CustomError(Exception):
    """
    Custom exception class that includes detailed error messages.
    """
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return self.error_message
    

    
if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomError(e, sys.exc_info())

