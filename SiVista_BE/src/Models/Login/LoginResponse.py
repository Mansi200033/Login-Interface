class LoginResponse:
    #Message>>str, Status>>str, Token>>str
    def __init__(self,message,status) -> None:
        self.message=message
        self.status=status
        #self.token=token
    