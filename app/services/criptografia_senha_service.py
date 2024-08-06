import bcrypt

class CriptografiaSenhaService():

    @staticmethod
    def hash_senha(senha: str) -> str:
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        print(senha_hash)
        return senha_hash

    @staticmethod
    def verificar_senha(senha: str, senha_com_hash: str) -> bool:
        if bcrypt.checkpw(senha.encode("utf-8"), senha_com_hash.encode('utf-8')):
            return True
        return False
    