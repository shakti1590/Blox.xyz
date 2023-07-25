class SessionIdGenerator:
    def __init__(self, max_users):
        self.max_users = max_users
        self.bitmap = [0] * ((max_users + 31) // 32)  
        self.available_ids = []
        self.next_id = 0

    def get_unique_session_id(self):
        if self.available_ids:
            return self.available_ids.pop()
        else:
            while self.bitmap[self.next_id // 32] & (1 << (self.next_id % 32)):
                self.next_id = (self.next_id + 1) % self.max_users
            session_id = self.next_id
            self.bitmap[session_id // 32] |= 1 << (session_id % 32)
            self.next_id = (self.next_id + 1) % self.max_users
            return session_id

    def release_session_id(self, session_id):
        if not (0 <= session_id < self.max_users):
            raise ValueError("Invalid session ID")
        self.bitmap[session_id // 32] &= ~(1 << (session_id % 32))
        self.available_ids.append(session_id)
max_users = 1000000
session_generator = SessionIdGenerator(max_users)
session_id_1 = session_generator.get_unique_session_id()
session_generator.release_session_id(session_id_1)
session_id_2 = session_generator.get_unique_session_id()
