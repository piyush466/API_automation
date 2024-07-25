import logging
class Loggen:

    @staticmethod
    def logger():
        """
        Configures and returns a logger instance.

        Returns:
        logging.Logger: A configured logger instance with DEBUG level,
                         writing logs to a file with a specific format.
        """
        logs = logging.getLogger(__name__)
        logs.setLevel(logging.DEBUG)
        filehandle = logging.FileHandler("/Users/user/PycharmProjects/API_personal_framework/piyush_apis_framework/Logs_file/api_logs.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandle.setFormatter(formatter)
        logs.addHandler(filehandle)
        return logs
