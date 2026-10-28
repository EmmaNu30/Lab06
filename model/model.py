from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        conn = get_connection()
        if conn is None:
            print("Errore di connessione al database.")
            return None

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM strumento"

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            strumenti = []
            for row in result:
                strumento = Strumento(
                    codice=row["codice"],
                    tipo=row["tipo"],
                    marca=row["marca"],
                    anno_acquisto=row["anno_acquisto"],
                    valore=row["valore"]
                )
                strumenti.append(strumento)

            cursor.close()
            conn.close()
            return strumenti
        except Exception as e:
            print(f"Errore durante la query: {e}")
            cursor.close()
            conn.close()
            return None

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        conn = get_connection()
        if conn is None:
            print("Errore di connessione al database.")
            return None

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM strumento WHERE tipo = %s"

        try:
            cursor.execute(query, (tipo,))
            result = cursor.fetchall()
            strumenti = []
            for row in result:
                strumento = Strumento(
                    codice=row["codice"],
                    tipo=row["tipo"],
                    marca=row["marca"],
                    anno_acquisto=row["anno_acquisto"],
                    valore=row["valore"]
                )
                strumenti.append(strumento)

            cursor.close()
            conn.close()
            return strumenti
        except Exception as e:
            print(f"Errore durante la query di ricerca: {e}")
            cursor.close()
            conn.close()
            return None