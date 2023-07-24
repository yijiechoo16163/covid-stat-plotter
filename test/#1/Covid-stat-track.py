import csv

import matplotlib.pyplot as plt

import os.path

class CovidDataAnalyzer:
    def __init__(self):
        self.data = {
            'new_cases': [],
            'recovered': [],
            'deaths': []
        }
    
    def log_data(self, new_cases, recovered, deaths):
        self.data['new_cases'].append(new_cases)
        self.data['recovered'].append(recovered)
        self.data['deaths'].append(deaths)
        analyzer.save_data('covid_data.csv')
    
    def save_data(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['new_cases', 'recovered', 'deaths'])
            writer.writerows(zip(self.data['new_cases'], self.data['recovered'], self.data['deaths']))
    
    def load_data(self, filename):
        self.data = {
            'new_cases': [],
            'recovered': [],
            'deaths': []
        }
        
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                self.log_data(int(row[0]), int(row[1]), int(row[2]))

    def plot_data(self, data_type, accumulation=False):
        x = range(1, len(self.data['new_cases']) + 1)
    
        if accumulation:
            data_type += '_accumulated'
            if data_type not in self.data:
                print(f"Data type '{data_type}' is not available.")
                return
            y = [sum(self.data[data_type][:i]) for i in x]
        else:
            if data_type not in self.data:
                print(f"Data type '{data_type}' is not available.")
                return
            y = self.data[data_type]

        plt.plot(x, y)
        plt.xlabel('Days')
        plt.ylabel('Number of Cases')
        plt.title(f'COVID-19 {data_type.capitalize()}')
        plt.show()

analyzer = CovidDataAnalyzer()

if os.path.isfile("covid_data.csv"):
    analyzer.load_data('covid_data.csv')
else:
    analyzer.save_data('covid_data.csv')

