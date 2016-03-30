Title: Installing and using Sentry on your Django projects
Date: 2016-03-21 23:28
Category: Web Development
Tags: Django, Python, Logging
Summary: Sentry is the perfect logging tool to use with your Django projects
Keywords: python
          django
          sentry
          logging
          server
          administration
          devops


[Sentry][1] is a very known, stable and powerful logging tool built with Django, which enable
an easy management for your application logging.

If you're a Django developer it's really
simple to use and will add a lot of benefits. Including organized logs supporting notifications
by email, to your hipchat room ...

You can use the hosted version of Sentry or install it on your own server. On this tutorial
we will install. Oh sorry, I think I have nothing to add on how to install it, just check [the official Sentry
documentation][2] where you will find a simple and clear instruction on how to do this.

I will just suggest some useful staff to use on production:

- If you are familiar with Docker and would like to use it, you can check [this docker image for Sentry][3].

- Run sentry-worker without -B, which mean running Celery beat, instead run it on another process, you can achieve
that with another supervisor config.

```bash

    [program:sentry-cron]
    directory=/www/sentry/
    command=/www/sentry/bin/sentry celery beat
    autostart=true
    autorestart=true
    redirect_stderr=true
    killasgroup=true

```

- Install and use [RabbitMQ][4] as broker instead of redis, specially if you have a large application which could lead
to many logging, if you have a micro/small server, you can stick with Redis.


[1]: https://www.getsentry.com
[2]: https://docs.getsentry.com/on-premise/server/installation/
[3]: https://hub.docker.com/_/sentry/
[4]: https://www.rabbitmq.com/download.html
