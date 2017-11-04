from django.db import models

import datetime


class Wps(models.Model):
    CODE_CHOICE = (
        ('API 1104', 'API 1104'),
        ('ASME IX', 'ASME IX'),
        ('D1.1', 'D1.1'),
        ('', '')
    )
    od_low_size = models.IntegerField(default=0)
    od_high_size = models.IntegerField(default=0)
    wt_low = models.FloatField(default=0)
    wt_high = models.FloatField(default=0)
    grade = models.CharField(max_length=25, default='')
    process = models.CharField(max_length=30, default='')
    code = models.CharField(
        max_length=50,
        choices=CODE_CHOICE,
        default=''
    )
    pwht = models.BooleanField(default=False)


# Project Description
class Project(models.Model):
    name = models.CharField(max_length=150, default='')
    description = models.CharField(max_length=250, default='')
    customer = models.CharField(max_length=150, default='')
    state = models.CharField(max_length=20, default='')
    wps = models.ManyToManyField(Wps)


class Drawings(models.Model):
    line_number = models.CharField(max_length=150, default='')
    drawing = models.FileField()
    revision = models.IntegerField()
    project = models.ManyToManyField(Project)


class Nde(models.Model):
    NDE_TYPE_CHOICES = (
        ('', ''),
        ('VT', 'VT'),
        ('RT', 'RT'),
        ('AUT', 'AUT'),
        ('UT', 'UT'),
        ('PT', 'PT'),
        ('MT', 'MT'),
    )
    nde_type = models.CharField(max_length=3, choices=NDE_TYPE_CHOICES, default='')
    nde_company = models.CharField(max_length=60, default='')
    nde_identifier = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.nde_company


class Welder(models.Model):
    procedures = models.ManyToManyField(Wps)
    name = models.CharField(max_length=150, default='')
    stencil = models.CharField(max_length=10, default='')
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.name


class Weld(models.Model):
    TYPE_CHOICES = (
        ('FW', 'Field Weld'),
        ('SW', 'Shop Weld'),
    )
    DISPOSITION_CHOICES = (
        ('NA', ''),
        ('ACC', 'Accepted'),
        ('REJ', 'Rejected'),
    )

    number = models.CharField(max_length=150, default='')
    nde_number = models.CharField(max_length=150, default='')
    weld_date = models.DateField(auto_now=False, default=datetime.datetime.now())
    nde_date = models.DateField(auto_now=False, default=datetime.datetime.now())
    pipe_size = models.IntegerField()
    pipe_thickness = models.DecimalField(max_digits=4, decimal_places=3)
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='FW',
    )
    disposition = models.CharField(
        max_length=3,
        choices=DISPOSITION_CHOICES,
        default='NA',
    )
    line_number = models.CharField(max_length=150, default='193-HG-1500-4')
    welders = models.ManyToManyField(Welder)
    material_type = models.CharField(max_length=150, default='CS')
    line_strength = models.CharField(max_length=150, default='900')
    weld_type = models.CharField(max_length=150, default='BW')
    rt = models.CharField(max_length=150, default='100%')
    wps = models.ManyToManyField(Wps)
    nde_info = models.ManyToManyField(Nde)
    material_a = models.CharField(max_length=150, default='')
    heat_a = models.CharField(max_length=150, default='')
    grade_a = models.CharField(max_length=150, default='')
    material_b = models.CharField(max_length=150, default='')
    heat_b = models.CharField(max_length=150, default='')
    grade_b = models.CharField(max_length=150, default='')
    cutout = models.BooleanField(default=False)
    comments = models.TextField(max_length=150, default='')

    def __str__(self):
        return self.number
