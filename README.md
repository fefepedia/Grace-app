# Grace-app
Here is This is an HTML file that includes a template for a dashboard page. The page has a title "Dashboard", and it includes three sections: two panels and a canvas element for a pie chart. The first panel displays a value called "first_number", the second panel displays a pie chart, and the third panel has a button that, when clicked, opens a new window with the file "text.html".

The page also includes a script tag that imports the Chart.js library, which is used to create the pie chart. The script then defines a function called "openWindow" that opens a new window with the specified dimensions. Finally, the script creates a new pie chart using the Chart.js library and the canvas element with the ID "pie-chart". The chart displays a single dataset labeled "Second Number" and the data for the chart is specified by the value "second_number".

a Flask route that serves a template called "dashboard.html" when the user navigates to the "/dashboard" URL. The template is rendered with two variables, "first_number" and "second_number", which are passed as arguments to the "render_template" function.

The code also reads a JSON file called "data.json" and loads the data into a Python dictionary called "data". It then extracts the values for "first_number", "second_number", and "text_content" from the dictionary and assigns them to variables with the same names. These variables will be available to use in the template when it is rendered.

It is a simple object with three properties: "first_number", "second_number", and "text_content". Each property has a value, which can be a number (in the case of "first_number" and "second_number") or a string (in the case of "text_content").
