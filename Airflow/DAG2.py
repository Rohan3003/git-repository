import re
def generate_request_body(status_data, request_template):
    """
    Replaces placeholders in a request template with corresponding values from a status dictionary.

    Args:
        status_data (dict): A dictionary containing the status values to be used for replacing placeholders.
        request_template (str): The template string containing placeholders to be replaced.

    Returns:
        str: The modified request template with all placeholders replaced.
    """
    # Find all placeholders in the request template
    placeholders = re.findall(r'\$\{([^\}]+)\}', request_template)

    # Replace each placeholder with the corresponding value from the status dictionary
    for placeholder in placeholders:
        placeholder_pattern = r'\$\{%s\}' % placeholder
        placeholder_value = str(status_data.get(placeholder))
        request_template = re.sub(placeholder_pattern, placeholder_value, request_template)

    return request_template


status_data1 =  {
    'name': 'Rohan',
    'age' : 30,
    'city' : 'New York'
}

request_template1 = 'Hello! My name is ${name} and my age is ${age} and I am from ${city}'

print(generate_request_body(status_data=status_data1, request_template=request_template1))