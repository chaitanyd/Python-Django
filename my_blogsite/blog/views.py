from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug" : "hike-in-the-mountains",
        "images" : "mountains.jpg",
        "author" : "Chaitany",
        "date" : date(2023, 10, 10),
        "title" : "Mountain Hiking",
        "excerpt" : """There's nothing like views you get when hiking in the mountains
                       And I wasn't even prepared for what happened while I was enjoying the view!""",
        "content" : """
                    Mountain climbing has been on the bucket list of many people. It is an activity which is considered
                    to be very exciting and adventurous. Moreover, it is something you will find to be very common all across the world.
                    
                    Mountain climbing has been on the bucket list of many people. It is an activity which is considered
                    to be very exciting and adventurous. Moreover, it is something you will find to be very common all across the world.
                    
                    Mountain climbing has been on the bucket list of many people. It is an activity which is considered
                    to be very exciting and adventurous. Moreover, it is something you will find to be very common all across the world.
                    
                    Mountain climbing has been on the bucket list of many people. It is an activity which is considered
                    to be very exciting and adventurous. Moreover, it is something you will find to be very common all across the world.
        """

    }
]

def start_page(request):
    return render(request, "index.html")


def posts(request):
    return render(request, "all-posts.html")


def post_details(request, slug):
    return render(request, "post-detail.html")

