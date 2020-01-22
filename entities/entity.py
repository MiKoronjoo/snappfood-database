import sqlite3
from typing import List

DB_PATH = 'db.sqlite'
DBTuple = List[str]


class Entity:
    @classmethod
    def update_tuple(cls, table, attribute, value, condition):
        con_obj = sqlite3.connect(DB_PATH)
        con_obj.execute(f'UPDATE {table} SET "{attribute}" = \'{value}\' WHERE {condition};')
        con_obj.commit()
        con_obj.close()

    @classmethod
    def insert_tuple(cls, table: str, attributes: DBTuple, values: DBTuple) -> None:
        con_obj = sqlite3.connect(DB_PATH)
        values = ', '.join([f"'{v}'" for v in values])
        attributes = ', '.join([f'"{a}"' for a in attributes])
        con_obj.execute(f'INSERT INTO {table}({attributes}) VALUES({values})')
        con_obj.commit()
        con_obj.close()

    @classmethod
    def select_columns(cls, table: str, columns: DBTuple = None) -> List[tuple]:
        con_obj = sqlite3.connect(DB_PATH)
        if columns is None:
            col = '*'
        else:
            col = ', '.join(columns)
        cursor = con_obj.execute(f'SELECT {col} FROM {table};')
        selected_table = cursor.fetchall()
        con_obj.close()
        return selected_table

    @classmethod
    def select_tuples(cls, table: str, attributes: DBTuple, values: DBTuple) -> List[tuple]:
        con_obj = sqlite3.connect(DB_PATH)
        if not attributes or not values:
            condition = '1 = 1'
        else:
            condition = ' AND '.join([f'"{attributes[i]}" = \'{values[i]}\'' for i in range(len(attributes))])
        cursor = con_obj.execute(f'SELECT * FROM {table} WHERE {condition};')
        selected_table = cursor.fetchall()
        con_obj.close()
        return selected_table
