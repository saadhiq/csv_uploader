
# Create your views here.

import pandas as pd
from django.shortcuts import render
from .forms import UploadCSVForm

def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            # csv_file = request.FILES['file']
            files = request.FILES.getlist('files')

            dataframes = []

            for file in files:
                df = pd.read_csv(file)
                dataframes.append(df)

            combined_df = pd.concat(dataframes, ignore_index=True)

            columns_to_display = combined_df.columns.tolist(['Question Number', 'Subject Contents','sydney_correct_count_percentage'])  # or specify specific columns
            data = combined_df[columns_to_display].to_html()


            # df = pd.read_csv(csv_file)
            # columns_to_display = ['Question Number', 'Subject Contents','sydney_correct_count_percentage']  # specify your column names here
            # data = df[columns_to_display].to_html()
            return render(request, 'display.html', {'data': data})
    else:
        form = UploadCSVForm()
    return render(request, 'upload.html', {'form': form})

