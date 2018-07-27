from django.db import models

class student_feedback(models.Model):
    ID = models.AutoField(primary_key=True)
    student_id = models.IntegerField(null=False)
    username = models.CharField(max_length=20, default=0)
    course_id = models.CharField(null=False, max_length=20)
    course = models.CharField(max_length=20,default=0)
    time = models.DateTimeField(null = True, blank=True)
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return u'%s-%s' % (str(self.student_id), str(self.course_id))
