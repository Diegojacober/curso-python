# Abstração
"""
Quando encontrar o erro NotImplemented erro signfica que esta usando a classe abstrata, e deve
herdar a classe criando uma subclasse
"""

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.log'

class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self.log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self.log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE,'a+',encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
            
class LogPrintMixin(Log):
    def log(self, msg):
        print(f'Mensagem de log:\n{msg}!!')
    
if __name__ == '__main__':
    # l = Log()
    # l.log('Qualquer coisa')
    
    lf = LogFileMixin()
    lf.log_success('Escrevendo um success no log')
    lp = LogPrintMixin()
    lp.log_success('Oba')