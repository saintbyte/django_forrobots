#!/usr/bin/env python
urlpatterns = patterns('',
    url(r'^clientaccesspolicy\.xml$' , 'forrobots.views.clientaccesspolicy'),
    url(r'^crossdomain\.xml$'        , 'forrobots.views.crossdomain'),
    url(r'^robots\.txt$'             , 'forrobots.views.robotstxt'),
) + urlpatterns.
