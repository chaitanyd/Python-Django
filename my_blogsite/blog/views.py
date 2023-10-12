from django.shortcuts import render, get_object_or_404
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "images": "mountains.jpg",
        "author": "Chaitany",
        "date": date(2023, 10, 10),
        "title": "Mountain Hiking",
        "excerpt": """There's nothing like views you get when hiking in the mountains
                       And I wasn't even prepared for what happened while I was enjoying the view!""",
        "content": """
                    Mountain climbing has been on the bucket list of many people. It is an activity which is considered
                    to be very exciting and adventurous. Moreover, it is something you will find to be very common all across the world.
                    
                    Mountain climbing has been on the bucket list of many people. It is an activity which is considered
                    to be very exciting and adventurous. Moreover, it is something you will find to be very common all across the world.
                    
                    Mountain climbing has been on the bucket list of many people. It is an activity which is considered
                    to be very exciting and adventurous. Moreover, it is something you will find to be very common all across the world.
                    
                    Mountain climbing has been on the bucket list of many people. It is an activity which is considered
                    to be very exciting and adventurous. Moreover, it is something you will find to be very common all across the world.
        """

    },
    {
        "slug": "programming-is-fun",
        "images": "coding.jpg",
        "author": "Chaitany",
        "date": date(2023, 10, 12),
        "title": "Programming is fun",
        "excerpt": """
                    Programming is about building things. You’re building software applications that are helpful 
                    and useful to people. When you succeed in doing this, it conveys a sense of accomplishment. 
                    It makes you feel good. It makes you feel proud. That’s fun
                    """,

        "content": """
                    Yes! Lots of people code for fun, and for many different reasons. For some people,
                    it’s the fun of building an application — the result is what matters. For others, 
                    it’s the process of creating something that works. Coding can be very engaging. 
                    Each line of code, if it works, causes something to happen in the console. 
                    Watching your idea take shape step-by-step is a blast. And the feeling after 
                    discovering a bug (and fixing it) is hard to replicate.

                    Any person can enjoy coding. However, people who enjoy problem-solving often thrive as programmers.
                    And while you don’t have to have an ‘engineering mind’ to do well,you’ll love coding if you also 
                    love building things.

                    In the world of programming, you’ll find artists, musicians, engineers, machinists, businesspeople 
                    — virtually every kind of person.And that’s one of the best things about coding: Anyone can do it,
                    and everyone can bring their own unique strengths to the table and create something great.
        """

    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2023, 10, 11),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def start_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[:3]
    return render(request, "index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "all-posts.html", {
        "all_posts": all_posts
    })


def post_details(request, slug, post=""):
    # identified_post = next(posts for in all_posts if post[slug] == slug)
    # identified_post = get_object_or_404(posts, slug=slug)
    return render(request, "post-detail.html")