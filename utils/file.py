import os


class CFile:
    @staticmethod
    def mkfileIfNotExist(filename):
        """
        如果不存在该文件则新建
        """
        with open(filename, 'a'):
            pass

    @staticmethod
    def mkdirIfNotExist(dirpath):
        """
        如果不存在该文件夹则新建
        """
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)

    @staticmethod
    def getFileType(filename):
        """
        获取文件类型
        """
        return filename.split('.').pop().lower()