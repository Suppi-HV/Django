
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination, Comments

# Create your views here.
def index(request):

    # dest1= Destination()
    # dest1.name='Mumbai'
    # dest1.desc='The city That Never Sleeps'
    # dest1.img='destination_1.jpg'
    # dest1.price=700
    # dest1.offer=False

    # dest2= Destination()
    # dest2.name='Hydrabad'
    # dest2.desc='First Biriyani,Then Sherwani'
    # dest2.img='destination_2.jpg'
    # dest2.price=650
    # dest2.offer=True


    # dest3= Destination()
    # dest3.name='Bengaluru'
    # dest3.desc='Beautiful city'
    # dest3.img='destination_3.jpg'
    # dest3.price=750
    # dest3.offer=False


    # dests=[dest1,dest2,dest3]
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})



# def details(request, id ):
#     # Get query parameters (e.g., name and desc)
#     desc = get_object_or_404(Destination, id=id)
    
#     return render(request, 'details.html', {'desc': desc})








# def destination_detail(request, pk):
#     destination = get_object_or_404(Destination, pk=pk)
    
#     # Fetch top-level comments and count their replies
#     comments = Comments.objects.filter(destination=destination, parent__isnull=True)\
#         .annotate(reply_count=Count('replies'))  # Count the replies for each comment
    
#     # Fetch all replies (if needed separately)
#     replies = Comments.objects.filter(destination=destination).exclude(parent__isnull=True)
    
#     if request.method == 'POST':
#         comment_text = request.POST['comment']
#         parent_id = request.POST.get('parent_id')  # Get parent comment ID if replying
        
#         if parent_id:
#             parent_comment = get_object_or_404(Comments, id=parent_id)
#             Comments.objects.create(
#                 comment=comment_text, 
#                 user=request.user, 
#                 destination=destination, 
#                 parent=parent_comment  # This is a reply to an existing comment
#             )
#         else:
#             Comments.objects.create(
#                 comment=comment_text, 
#                 user=request.user, 
#                 destination=destination  # This is a new comment
#             )
#         return redirect('details', pk=destination.pk)
    
#     total_comments = comments.count()
#     total_replies = replies.count()
    
#     return render(request, 'details.html', {
#         'destination': destination,
#         'comments': comments,  # Now each comment has a reply_count attribute
#         'replies': replies,
#         'total_comments': total_comments,
#         'total_replies': total_replies,
#     })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination, Comments
from django.db.models import Count, F



def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)

    if not request.user.is_authenticated and pk > 2:
        return render(request, 'register_first.html')
    
    # Fetch top-level comments and count their replies
    comments = Comments.objects.filter(destination=destination, parent__isnull=True)\
        .annotate(reply_count=Count('replies'))  # Count the replies for each comment
    
    # Fetch all replies
    replies = Comments.objects.filter(destination=destination).exclude(parent__isnull=True)

    if request.method == 'POST':
        # Comment submission logic
        comment_text = request.POST.get('comment')  # Use .get() to avoid MultiValueDictKeyError
        if not comment_text:
            # Optionally handle the case where no comment was provided
            return redirect('details', pk=destination.pk)

        parent_id = request.POST.get('parent_id')  # Get parent comment ID if replying
        
        # Handle comment or reply creation
        if parent_id:
            parent_comment = get_object_or_404(Comments, id=parent_id)
            Comments.objects.create(
                comment=comment_text, 
                user=request.user, 
                destination=destination, 
                parent=parent_comment  # This is a reply to an existing comment
            )
        else:
            Comments.objects.create(
                comment=comment_text, 
                user=request.user, 
                destination=destination  # This is a new comment
            )
        return redirect('details', pk=destination.pk)

    

    total_comments = comments.count()
    total_replies = replies.count()

    return render(request, 'details.html', {
        'destination': destination,
        'comments': comments,  # Now each comment has likes and dislikes
        'replies': replies,
        'total_comments': total_comments,
        'total_replies': total_replies,
    })

from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required
def like_dislike_comment(request, comment_id, action):
    comment = get_object_or_404(Comments, id=comment_id)

    if action == "like":
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)  # Unlike
        else:
            comment.likes.add(request.user)  # Like
            comment.dislikes.remove(request.user)  # Remove dislike if present

    elif action == "dislike":
        if request.user in comment.dislikes.all():
            comment.dislikes.remove(request.user)  # Remove dislike
        else:
            comment.dislikes.add(request.user)  # Dislike
            comment.likes.remove(request.user)  # Remove like if present

    return redirect(request.META.get("HTTP_REFERER", "details"))
