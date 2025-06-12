from jinja2 import Template


# Load the template from file
with open('template_file_test.py.tpl', 'r') as file:
    template_content = file.read()

# Create a Jinja2 template object
template = Template(template_content)

# Define values for the placeholders
context = {
    'function_name': 'my_generated_function'
}

# Render the template with the provided context
generated_code = template.render(context)

# Output the generated code
print(generated_code)

#  -----------------------------------------------------------

# Save the generated code to a Python file
# with open('generated_code.py', 'w') as file:
#     file.write(generated_code)
#
# # Alternatively, you can execute the generated code directly
# exec(generated_code)
