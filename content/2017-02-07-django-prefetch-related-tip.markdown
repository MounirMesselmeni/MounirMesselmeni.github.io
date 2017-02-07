Title: Accessing prefetched objects inside your model's methods
Date: 2017-02-06 23:28
Category: Web Development
Tags: Django, Python, Django ORM
Summary: Accessing hidden prefetched fields in Django
Keywords: python
          django
          django orm
          prefetch_related
          select_related
          model
          queryset
          methods
          bussiness logic
          dry


I had many time the need to optimize some perfomance issues with some ORM queries, then many times the [prefetch_related][1] and [select_related][2] were my best friends for this topic. But when calling some business logic which reside in some model's methods which try to calculate or to fetch some related model data the optimization will not have any effect as these method are using `filter` or some queryset aggregations `Sum` or `Count` ...

The solution to this problem is either to redefine the logic to use prefetched data or more clean to make these methods now if there already prefeteched objects, that's the best solution in my cases:

A basic models example `models.py`:

```python

    class Teacher(models.Model):
        name = models.CharField(max_length=255)

        def students_count(self):
            return self.student_set.filter(age__gte=20).count()
        
    class Student(models.Model):
        name = models.CharField(max_length=255)
        teacher = models.ForeignKey(Teacher)
        age = models.IntegerField(default=20)

```

```python

    for t in Teacher.objects.all():
        print(teacher.students_count())
    # This will results to the number of teachers + 1 SQL queries

```

Let's use `prefetch_related`:

```python

    for t in Teacher.objects.all().prefetch_related('student_set'):
        print(teacher.students_count())
    # Our prefetch have no effect as the method students_count is using filter which
    # will ignore the prefetched objects
    
```

We have to fix the method `students_count` to consider checking for prefetched objects:

```python

    class Teacher(models.Model):
        name = models.CharField(max_length=255)

        def students_count(self):
            if hasattr(self, '_prefetched_objects_cache') and 'student' in self._prefetched_objects_cache:
                return len([x for x in self.student_set.all() if x.age >= 20])
            return self.student_set.filter(age__gte=20).count()

```

This way even calling `students_count` in a single instance without calling `prefetch_related` on the queryset will use the filter instead of the prefetched, this can be useful in many cases but I better to use this only when you need to.

Thanks for reading


[1]: https://docs.djangoproject.com/en/1.10/ref/models/querysets/#prefetch-related
[2]: https://docs.djangoproject.com/en/1.10/ref/models/querysets/#select-related