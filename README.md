SVG Plotter App

This Django web application allows you to create SVG graphics based on the given XY, YZ, or XZ plane and coordinates provided in the format {'x1': int, 'y2': int, 'z2': int}.
Installation

Make sure you have Python and Django installed on your system. You can install the required packages by running the following command in your virtual environment:

bash

pip install -r requirements.txt

Usage

    Clone this repository to your local machine.
    Navigate to the project directory using the command line.
    Start the Django development server by running the following command:

bash

python manage.py runserver

    Open your web browser and go to http://localhost:8000/ to access the SVG Plotter app.
    Choose the plane (XY, YZ, or ZX) and enter the coordinates in the format {
    'x1': int, 'x2': int,'y1': int,'y2': int, 'xz': int, 'z2': int
    }.
    Click the "Generate" button to create the SVG graphic based on your input.

That's it! You can now use the SVG Plotter app to create SVG graphics easily.
Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.

Happy plotting!