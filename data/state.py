class State:
    def __init__(self):
        self.channel_id = None
        self.study_time = None
        self.duration_time = None
        self.enabled = False

        self.week_schedule = {}

        self.last_start_date = None
        self.last_reminder_date = None
        self.last_end_date = None
