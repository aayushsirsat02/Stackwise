from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .utils import call_api
from django.contrib.auth.models import User


# Create your views here.

@login_required
def service_view(request):


    if request.method =="POST":
        application_type = request.POST.get("app_type")
        target_audience = request.POST.get("audience")
        users_size= request.POST.get("users")
        team_size = request.POST.get("team_size")
        budget = request.POST.get("budget" )
        priority= request.POST.get("priority" )
        auth = request.POST.get("auth")
        notes = request.POST.get("notes")
        print("POST RECEIVED")
        print("USER:", request.user, request.user.is_authenticated)

        
        
        user_message = f"""
I need a technical recommendation (including Frontend, Backend, Database, and Infrastructure) for a new software project based on the following constraints:

- **Application Type:** {application_type}
- **Target Audience:** {target_audience}
- **Estimated User Base:** {users_size}
- **Development Team Size:** {team_size}
- **Budget Constraint:** {budget}
- **Primary Priority (e.g., speed, low cost, scalability):** {priority}
- **Authentication Method:** {auth}
- **Additional Notes/Requirements:** {notes}

Please provide a detailed, justified technical stack recommendation.
"""
        
        
        htmlready_content = call_api(user_message=user_message)
        return render(request, "mainservice/form.html",{
            "result": htmlready_content
        })
        
    return render(request, "mainservice/form.html")


