from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from .models import StudentRegister

def step_container(request):
    return render(request, "std/step_container.html")



def load_step(request, step):
    templates = {
        1: 'std/step1.html',
        2: 'std/step2.html',
        3: 'std/step3.html',
        4: 'std/step4.html',
    }

    template = templates.get(step)

    if not template:
        raise Http404("Step not found")

    return render(request, template)
    

def save_step(request, step):
    if request.method == 'POST':

        data = request.POST

        if step == 1:
            request.session['name'] = data.get('name')
            request.session['age'] = data.get('age')
            request.session['email'] = data.get('email')

   
        elif step == 2:
            request.session['address'] = data.get('address')
            request.session['city'] = data.get('city')
            request.session['state'] = data.get('state')

       
        elif step == 3:
            request.session['course'] = data.get('course')

 
        elif step == 4:
            request.session['phone'] = data.get('phone')

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'invalid request'}, status=400)



def submit_final(request):
   
    StudentRegister.objects.create(
        name=request.session.get('name'),
        age=request.session.get('age'),
        email=request.session.get('email'),
        address=request.session.get('address'),
        city=request.session.get('city'),
        state=request.session.get('state'),
        course=request.session.get('course'),
        # phone=request.session.get('phone'),  # Only if added in step4
    )


    request.session.flush()

    return render(request, 'std/completed.html')
