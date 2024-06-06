from random import randint
import matplotlib.pyplot as plt
import os
import matplotlib

matplotlib.use('Agg')


def draw_plot(data):
    # Given data

    # Prepare data for the plot
    labels = [f'{key}' for key in data]
    profits = [value[0] for value in data.values()]

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Create a bar chart
    plt.bar(labels, profits)

    # Set the labels
    plt.xlabel('Metric (Buy Date - Sell Date)')
    plt.ylabel('Max Profit')

    # Set the title
    plt.title('Max Profit by Metric and Date')

    # Save the figure as a .jpg file in the current folder

    # Delete all files in the ../../frontend/images folder

    # Get the directory of the current script file
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Construct the absolute path to the images directory
    folder_path = os.path.join(script_dir, '../../frontend/images/')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    plt.savefig(folder_path + f'p{randint(1, 100)}.jpg', format='jpg')

    # Display the plot
    # plt.show()
