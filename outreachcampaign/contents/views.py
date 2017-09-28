# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

import json

# Create your views here.
def index(request):
    return render(request, 'contents/index.html', {"first_name": "Ruben", "company_name": "Surfly", "website": "surfly.com", "pitch": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam pulvinar, tellus nec ornare elementum, dolor nisi elementum sem, non elementum metus velit in elit. Sed efficitur nibh pulvinar tincidunt volutpat. Fusce sagittis mi at elit tincidunt hendrerit. Suspendisse potenti. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.", "consultant_name": "Carolina", "consultant_avatar": "../../../static/images/Carolina.png"})

# def parse_json(data):
#     lead = json.loads(data)
#     first_name = lead["first_name"]
#     company_name = lead["company_name"]
#     website = lead["website"]
#     pitch = lead["pitch"]
#     consultant_name = lead["consultant_name"]
#     consultant_avatar = lead["consultant_avatar"]
