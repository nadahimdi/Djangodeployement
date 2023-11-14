from django.shortcuts import render
from joblib import load;
# Create your views here.
model = load('./savedModels/model.joblib')
def predictor(request):
    return render(request,"main.html")



from django.shortcuts import render

def formInfo(request):
    if request.method == 'POST':
        # Get the values directly from the request.POST dictionary
        closed_at = float(request.POST.get('closed_at'))
        funding_rounds = float(request.POST.get('funding_rounds'))
        funding_total_usd = float(request.POST.get('funding_total_usd'))
        milestones = float(request.POST.get('milestones'))
        relationships = float(request.POST.get('relationships'))
        lat = float(request.POST.get('lat'))
        founded_at_year = float(request.POST.get('founded_at_year'))
        first_funding_at_year = float(request.POST.get('first_funding_at_year'))
        last_funding_at_year = float(request.POST.get('last_funding_at_year'))
        first_milestone_at_year = float(request.POST.get('first_milestone_at_year'))
        last_milestone_at_year = float(request.POST.get('last_milestone_at_year'))
       
        active_years = float(request.POST.get('active_years'))
        lng = float(request.POST.get('lng'))
        category_input = request.POST.get('Category')
        country_input = request.POST.get('Country')

        # Define your category names
        category_names = ['advertising', 'analytics', 'automotive', 'biotech', 'cleantech', 'consulting', 'design', 'ecommerce', 'education', 'enterprise', 'fashion', 'finance', 'games_video', 'government', 'hardware', 'health', 'hospitality', 'legal', 'local', 'manufacturing', 'medical', 'messaging', 'mobile', 'music', 'nanotech', 'network_hosting', 'news', 'nonprofit', 'other', 'pets', 'photo_video', 'public_relations', 'real_estate', 'search', 'security', 'semiconductor', 'social', 'software', 'sports', 'transportation', 'travel', 'web' ]  # Add other categories as needed

        # Create a dictionary to store the transformed category values
        category_values = {f'category_{category}': 1 if category_input.lower() == category else 0 for category in category_names}

        # Define your country names
        country_names = ['AFG', 'AGO', 'ALB', 'AND', 'ANT', 'ARA', 'ARE', 'ARG', 'ARM', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BWA', 'CAN', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COL', 'CRI', 'CSS', 'CUB', 'CYM', 'CYP', 'CZE', 'DEU', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ESP', 'EST', 'ETH', 'FIN', 'FRA', 'FST', 'GBR', 'GEO', 'GHA', 'GIB', 'GLP', 'GRC', 'GRD', 'GTM', 'HKG', 'HRV', 'HTI', 'HUN', 'IDN', 'IND', 'IOT', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KOR', 'KWT', 'LAO', 'LBN', 'LIE', 'LKA', 'LTU', 'LUX', 'LVA', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'MEX', 'MKD', 'MLT', 'MMR', 'MTQ', 'MUS', 'MYS', 'NAM', 'NCL', 'NFK', 'NGA', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'POL', 'PRI', 'PRK', 'PRT', 'PRY', 'PST', 'QAT', 'REU', 'ROM', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SLE', 'SLV', 'SMR', 'SOM', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SYC', 'SYR', 'THA', 'TTO', 'TUN', 'TUR', 'TWN', 'TZA', 'UGA', 'UKR', 'UMI', 'URY', 'USA', 'UZB', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'YEM', 'ZAF', 'ZMB', 'ZWE']

        # Create a dictionary to store the transformed country values
        country_values = {f'country_{country}': 1 if country_input == country else 0 for country in country_names}

        # Convert the values to a list of lists
        input_data = [[closed_at, funding_rounds, funding_total_usd, milestones, relationships,
                        lat, founded_at_year, first_funding_at_year, last_funding_at_year,
                        first_milestone_at_year, last_milestone_at_year, active_years,
                        lng, *category_values.values(), *country_values.values()]]

        # Call your machine learning model function with the transformed values
        y_pred = model.predict(input_data)
        company_state = "Open" if y_pred[0] == 1 else "Closed"

# Render the result.html template with the result
    return render(request, 'result.html', {'company_state': company_state})


