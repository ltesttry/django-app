from testa.models import MyNotes, MyQuestion

def run():
    q = MyNotes.objects.all()
    print(q)