class UserInputError(Exception):

    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('请输入数字')
    print(userinput)
except UserInputError as e:
    print(e)
finally:
    del userinput
