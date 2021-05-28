from django.http.response import HttpResponse
from django.shortcuts import render
from . import solve
# Create your views here.   

def index(request):
    if request.method == 'POST':
        board = []
        for i in range(9):
            temp = []
            for j in range(9):
                try:
                    if request.POST.get('arr[' + str(i) + '][' + str(j) + ']', 0) == "":
                        temp.append(0)
                    else: 
                        temp.append(int(request.POST.get('arr[' + str(i) + '][' + str(j) + ']', 0)))
                except:
                    return HttpResponse("<h1>Invalid values: Enter only integer values</h1>")
            board.append(temp)
        board = solve.solution(board)
        params = {'board':board}
        return render(request, 'solver/result.html', params)

    return render(request, 'solver/index.html')
