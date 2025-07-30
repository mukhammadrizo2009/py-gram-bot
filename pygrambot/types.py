class Update:

    def __init__(self, update_id: int, message: dict | None = None):
        self.update_id = update_id
        self.message = message
