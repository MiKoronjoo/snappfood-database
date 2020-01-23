from entities.entity import Entity


class Comment(Entity):
    def __init__(self, commentId):
        tbl = Comment.select_tuples('Comment', ['commentId'], [commentId])[0]
        self.commentId = tbl[0]
        self.rate = tbl[2]
        self.text = tbl[1]

    @classmethod
    def add(cls, rate, text=''):
        cls.insert_tuple('Comment', ['rate', 'text'], [rate, text])
        tbl = Comment.select_tuples('Comment', ['rate', 'text'], [rate, text])
        return tbl[-1][0]  # commentId
