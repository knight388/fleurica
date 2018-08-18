from .forms import UserCreationForm

def signup(request):
	sform = UserCreationForm()

	return {'sform':sform}

def login(request):
	return {}	