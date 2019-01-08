from django.db import models

class TimeSlot(models.Model):
    doc = models.ForeignKey('auth.User',related_name="doc_time_slot",on_delete=models.CASCADE)
    time_slot_available = models.TimeField()
    appointed = models.CharField(max_length=4,default="no")
    def __str__(self):
        return self.doc.username + " " + str(self.time_slot_available)
