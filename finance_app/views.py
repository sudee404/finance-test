from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from .models import Income, IncomeInstance
from django.http import JsonResponse, HttpResponse
from .forms import LoginForm, UserForm, IncomeInstanceForm

# Create your views here.


@login_required(login_url='login')
def index(request):
    """This is the home page view"""
    # let's create a context dictionary to hold our data
    context = {}
    # first let's retrieve the user's income object and add it to context
    income = Income.objects.get_or_create(owner=request.user)[0]
    context['user_income'] = income
    context['instances'] = income.get_instances()
    context['form'] = IncomeInstanceForm()

    return render(request, 'index.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)

            return redirect('index')
    context['form'] = UserForm()

    return render(request, 'sign_up.html', context=context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            new_user = form.clean()
            # Lets login our newly created user
            # Make sure to authenticate the data first to check for errors
            try:
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        )

                login(request, new_user)
            except:
                context['errors'] = True
            else:
                # if no errors are found, lets switch back to homepage
                return redirect('index')
    context['form'] = LoginForm()

    return render(request, 'sign_in.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')


def add_income(request):
    if request.method == 'POST':
        form = IncomeInstanceForm(request.POST)
        form.instance.income = get_object_or_404(Income, owner=request.user)
        try:
            form.save(commit=True)
        except:
            return HttpResponse('failed')
        return redirect('index')


def get_income(request):
    if request.method == 'GET':
        pk = request.GET.get('pk')
        income = get_object_or_404(IncomeInstance, pk=pk)
        data = {
            'description': income.description,
            'amount': income.amount,
            'age_start': income.age_start,
            'age_stop': income.age_stop,
            'growth': income.growth
        }
        return JsonResponse(data)


def update_income(request):
    if request.method == 'POST':

        income = get_object_or_404(IncomeInstance, id=request.POST.get('instance_id'))
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        age_start = request.POST.get('age_start')
        age_stop = request.POST.get('age_stop')
        growth = request.POST.get('growth')

        if description:
            income.description = description
        if amount:
            income.amount = amount
        if age_start:
            income.age_start = age_start
        if age_stop:
            income.age_stop = age_stop
        if growth:
            income.growth = growth

        income.save()

        return redirect('index')


def delete_income(request):
    if request.method == 'GET':
        pk = request.GET.get('pk')
        income = get_object_or_404(IncomeInstance, pk=pk)
        income.delete()
        return HttpResponse('success')


def get_plots(request):
    """This function returns points to be plotted"""
    # We are going to use pandas library to make a dataframe and 
    # pass its values to chart js javascrip code on our frontend

    import pandas as pd
    # Lets get our details from the user's income
    incomes = get_object_or_404(Income, owner=request.user).get_instances()
    # Use a pandas dataframe to hold our data for easier manipulation

    df = pd.DataFrame(index=[i for i in range(40,91)])
    # add income data to the dataframe
    for income in incomes:
        # add a column with all values as 0
        df[income.description] = 0
        # set values from age start to stop
        df[income.description].loc[income.age_start:income.age_stop] = income.amount
        if income.growth:
            # if growth is available set the new value from 65 to the stopping age
            df[income.description].loc[65:income.age_stop] = income.growth
    # Create a column with tottal of the values
    df['Total Income'] = df.sum(axis=1)
    # pass the data to a JSONRESponse in form of a dictionary
    data = {
        'y_data': unpack_dataframe(df),
        'x_data': [int(i) for i in df.index.values],
    }
    return JsonResponse(data)

def unpack_dataframe(df):
    """Unpack Pandas dataframe into a list of dictionaries 

    Args:
        df (pd.DataFrame): A pandas DataFrame

    Returns:
        list: A list of dictionaries
    """
    lst = []
    for column in df.columns:
        data = {}
        data[column] = [int(i) for i in df[column].values]
        lst.append(data)

    
    return lst
