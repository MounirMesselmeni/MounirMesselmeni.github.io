Title: How to order a calculated count field in Django's admin
Date: 2016-03-21 23:28
Category: Web Development
Tags: Django, Python, Django Admin
Summary: Ordering a counted related field with annotate via the awesome django admin
Keywords: python
          django
          admin
          django admin
          order
          ordering
          count
          annotate
          queryset
          modeladmin


You can easily add a field which count a specific related model from a reverse `ForeignKey` relation or 
a `ManyToMany` relation, but ordering this field could not be easy from the first time.

Here we will see how to use annotate to add this field and how to order it. You only have to define `admin_order_field`
as in the following.

A basic models example `models.py`:

```python

    class Teacher(models.Model):
        name = models.CharField(max_length=255)
        
    class Student(models.Model):
        name = models.CharField(max_length=255)
        teacher = models.ForeignKey(Teacher)

```

And the `admin.py`

```python

    @admin.register(Teacher)
    class TeacherAdmin(admin.ModelAdmin):
        list_display = (
            'id',
            'students_count',
        )
    
        def get_queryset(self, request):
            return Teacher.objects.annotate(students_count=Count('student'))
    
        def students_count(self, obj):
            return obj.students_count
    
        students_count.short_description = _('Students count')
        students_count.admin_order_field = 'students_count'
    
```
