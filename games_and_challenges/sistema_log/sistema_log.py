from datetime import datetime


class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.txt', 'a+') as f:
            data_atual = datetime.today()
            data_em_texto = data_atual.strftime('%d/%m/%Y %H:%M')
            f.write(f'{msg} DATA: {data_em_texto}')
            f.write('\n')

    def log_info(self, info):
        self.write(f'INFO: {info}')

    def log_error(self, error):
        self.write(f'ERROR: {error}')


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._internet = False

    def conectar(self):
        if not self._ligado:
            error_ligado = f'{self._nome.title()} nao esta ligado!'
            print(error_ligado)
            self.log_error(error_ligado)
            return
        if self._internet:
            error_internet = f'{self._nome.title()} ja esta conectado'
            print(error_internet)
            self.log_error(error_internet)
            return
        log_success_conectar = f'{self._nome.title()} esta conectado'
        print(log_success_conectar)
        self.log_info(log_success_conectar)
        self._internet = True

    def desconectar(self):
        if not self._ligado:
            error_nao_ligado = f'{self._nome.title()} nao esta ligado!'
            print(error_nao_ligado)
            self.log_error(error_nao_ligado)
            return
        if not self._internet:
            error_nao_conectado = f'{self._nome.title()} ja nao esta conectado'
            print(error_nao_conectado)
            self.log_error(error_nao_conectado)
            return
        log_success_desconectar = f'{self._nome.title()} foi desconectado'
        print(log_success_desconectar)
        self.log_info(log_success_desconectar)
        self._internet = False


celular = Smartphone('Samsung M21s')
celular.ligar()
celular.conectar()
celular.conectar()
