from django.db import models


# Create your models here.
class HAC(models.Model):
    AGE_CHOICES = [(i, str(i)) for i in range(0, 120)]
    SEX_CHOICES = [(0, '0 - Female'), (1, '1 - Male')]
    CP_CHOICES = [(1, '1 - Typical angina'), (2, '2 - Atypical angina'), (3, '3 - Non-anginal pain'), (4, '4 - Asymptomatic')]
    FBS_CHOICES = [(0, '0 - <120mg/dl'), (1, '1 - >120mg/dl')]
    RESTECG_CHOICES = [(0, '0 - Normal'), (1, '1 - ST-T wave abnormality'), (2, '2 - Left ventricular hypertrophy')]
    EXNG_CHOICES = [(0, '0 - No'), (1, '1 - Yes')]
    SLP_CHOICES = [(0, '0 - No'), (1, '1 - Yes')]
    CAA_CHOICES = [(i, str(i)) for i in range(0, 4)]
    THALL_CHOICES = [(0, '0 - Normal'), (1, '1 - Fixed defect'), (2, '2 - Reversable defect')]
    OUTPUT_CHOICES = [(0, '0 - No HA'), (1, '1 - HA')]

    age = models.IntegerField(choices=AGE_CHOICES, default=20)
    sex = models.IntegerField(choices=SEX_CHOICES, default=0)
    cp = models.IntegerField(choices=CP_CHOICES, default=0)
    trtbps = models.FloatField(default=0.0)
    chol = models.FloatField(default=0.0)
    fbs = models.IntegerField(choices=FBS_CHOICES, default=0)
    restecg = models.IntegerField(choices=RESTECG_CHOICES, default=0)
    thalachh = models.FloatField(default=0.0)
    exng = models.IntegerField(choices=EXNG_CHOICES, default=0)
    oldpeak = models.FloatField(default=0.0)
    slp = models.IntegerField(choices=SLP_CHOICES, default=0)
    caa = models.IntegerField(choices=CAA_CHOICES, default=0)
    thall = models.IntegerField(choices=THALL_CHOICES, default=0)
    output = models.IntegerField(choices=OUTPUT_CHOICES, default=0)

    def __str__(self):
        return f"HeartAttack (id={self.id})"

    