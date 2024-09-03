
# # Create your views here.

# import pandas as pd
# from django.shortcuts import render
# from .forms import UploadCSVForm

# def upload_csv(request):
#     if request.method == 'POST':
#         form = UploadCSVForm(request.POST, request.FILES)
#         if form.is_valid():
#             # csv_file = request.FILES['file']
#             files = request.FILES.getlist('files')

#             dataframes = []

#             for file in files:
#                 df = pd.read_csv(file)
#                 dataframes.append(df)

#             combined_df = pd.concat(dataframes, ignore_index=True)

#             columns_to_display = combined_df.columns.tolist(['Question Number', 'Subject Contents','sydney_correct_count_percentage'])  # or specify specific columns
#             data = combined_df[columns_to_display].to_html()


#             # df = pd.read_csv(csv_file)
#             # columns_to_display = ['Question Number', 'Subject Contents','sydney_correct_count_percentage']  # specify your column names here
#             # data = df[columns_to_display].to_html()
#             return render(request, 'display.html', {'data': data})
#     else:
#         form = UploadCSVForm()
#     return render(request, 'upload.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import ImagesForm
from .models import Image,Csv

# Create your views here.
def index(request):
    images = Csv.objects.all()
    context = {'images': images}
    return render(request, "index.html", context)
def fileupload(request):
    form = ImagesForm(request.POST, request.FILES)
    if request.method == 'POST':
        images = request.FILES.getlist('pic')
        for image in images:
            image_ins = Csv(file = image)
            image_ins.save()
        return redirect('index')
    context = {'form': form}
    return render(request, "upload.html", context)

# def index(request):
#     return render(request, 'upload.html')

