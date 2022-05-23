from ..logger import Logger


class TestLogger():
    """
    Test logger
    """

    def test_info(self, capsys) -> None:
        """ Test: Add message to log """

        logger = Logger()

        messsage = 'Test message'
        logger.info(messsage)
        captured = capsys.readouterr()
        assert captured.out == messsage + '\n'
