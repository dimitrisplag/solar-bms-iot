from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'landing.html')

@login_required
def home(request):
    return render(request, 'home.html')

# Φτιάχνουμε μια προσαρμοσμένη φόρμα που να ζητάει ΚΑΙ email
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email") # Κάνουμε το email υποχρεωτικό

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email') # Το password μπαίνει αυτόματα από το Django

# Η λειτουργία (view) που θα διαχειρίζεται την εγγραφή
def register(request):
    if request.method == 'POST':
        # Αν ο χρήστης πάτησε "Εγγραφή", παίρνουμε τα δεδομένα του
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Αποθήκευση του χρήστη στη βάση δεδομένων (db.sqlite3)
            login(request, user) # Κάνουμε τον χρήστη αυτόματα login μετά την εγγραφή
            return redirect('/') # Τον στέλνουμε στην αρχική σελίδα
    else:
        # Αν απλά μπήκε στη σελίδα, του δείχνουμε την άδεια φόρμα
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})
