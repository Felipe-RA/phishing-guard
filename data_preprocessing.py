import re
from collections import OrderedDict
from math import log2
from pprint import pprint
from urllib.parse import urlparse


def parse_url(url):
    """
    Parses a URL and extracts its components.

    Args:
    url (str): The URL to parse.

    Returns:
    dict: A dictionary containing the URL components such as scheme, netloc, path, query, fragment,
          and query parameters as key-value pairs.

    Example:
    For the URL "https://www.example.com:8080/login?user=abc#section",
    the function will return:
    {
        'scheme': 'https',
        'netloc': 'www.example.com:8080',
        'path': '/login',
        'query': 'user=abc',
        'fragment': 'section',
        'params': {'user': ['abc']}
    }
    """
    parsed = urlparse(url)
    
    return {
        'scheme': parsed.scheme,
        'netloc': parsed.netloc,
        'path': parsed.path,
        'params': parsed.params,
        'query': parsed.query,
        'fragment': parsed.fragment
    }

def get_url_length(url):
    """
    Calculates the total length of a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The length of the URL.
    """
    return len(url)

def get_number_of_dots_in_url(url):
    """
    Counts the number of dots in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of dots ('.') in the URL.
    """
    return url.count('.')

def has_repeated_digits_in_url(url):
    """
    Checks if the URL contains repeated consecutive digits.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    bool: True if there are repeated consecutive digits, False otherwise.
    """

    return bool(re.search(r'(\d)\1', url))

def get_number_of_digits_in_url(url):
    """
    Counts the number of digits (0-9) in a URL.

    Args:
    url (str): The complete URL.

    Returns:
    int: The count of digits in the URL.
    """
    return len(re.findall(r'\d', url))

def get_number_of_special_char_in_url(url):
    """
    Counts the number of special characters (e.g., "@", "#", "$", "%", "&", "-") in a URL.

    Args:
    url (str): The complete URL.

    Returns:
    int: The count of special characters in the URL.
    """
    return len(re.findall(r'[@#$%&-]', url))

def get_number_of_hyphens_in_url(url):
    """
    Counts the number of hyphens ("-") in a URL.

    Args:
    url (str): The complete URL.

    Returns:
    int: The count of hyphens in the URL.
    """
    return url.count('-')

def get_number_of_underline_in_url(url):
    """
    Counts the number of underscores in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of underscores ('_') in the URL.
    """
    return url.count('_')

def get_number_of_slash_in_url(url):
    """
    Counts the number of forward and backward slashes in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of slashes ('/' and '\\') in the URL.
    """
    return url.count('/') + url.count('\\')

def get_number_of_questionmark_in_url (url):
    """
    Counts the number of question marks in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of question marks ('?') in the URL.
    """
    return url.count('?')

def get_number_of_equal_in_url(url):
    """
    Counts the number of equal signs in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of equal signs ('=') in the URL.
    """
    return url.count('=')

def get_number_of_at_in_url(url):
    """
    Counts the number of at symbols in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of at symbols ('@') in the URL.
    """
    return url.count('@')

def get_number_of_dollar_in_url(url):
    """
    Counts the number of dollar signs in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of dollar signs ('$') in the URL.
    """
    return url.count('$')


def get_number_of_exclamation_marks_in_url(url):
    """
    Counts the number of exclamation marks in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of exclamation marks ('!') in the URL.
    """
    return url.count('!')

def get_number_of_hashtags_in_url(url):
    """
    Counts the number of hashtags in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of hashtags ('#') in the URL.
    """
    return url.count('#')

def get_number_of_percent_signs_in_url(url):
    """
    Counts the number of percent signs in a URL.
    
    Args:
    url (str): The complete URL.
    
    Returns:
    int: The count of percent signs ('%') in the URL.
    """
    return url.count('%')

def get_domain_length(parsed_url):
    """
    Calculates the length of the domain name from a parsed URL.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    int: The length of the domain name.
    """
    domain = parsed_url['netloc'].split(':')[0]  # Exclude port number if present
    return len(domain)

def get_number_of_dots_in_domain(parsed_url):
    """
    Counts the number of dots in the domain name.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    int: The count of dots ('.') in the domain name.
    """
    domain = parsed_url['netloc'].split(':')[0]
    return domain.count('.')

def has_hyphens_in_domain(parsed_url):
    """
    Checks if the domain name contains hyphens.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    bool: True if there are hyphens ('-') in the domain name, False otherwise.
    """
    domain = parsed_url['netloc'].split(':')[0]
    return '-' in domain

def has_special_characters_in_domain(parsed_url):
    """
    Checks if the domain name contains special characters.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    bool: True if there are special characters in the domain name, False otherwise.
    """
    domain = parsed_url['netloc'].split(':')[0]
    return bool(re.search(r'[@#$%&-]', domain))

def get_number_of_special_characters_in_domain(parsed_url):
    """
    Counts the number of special characters in the domain name.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    int: The count of special characters in the domain name.
    """
    domain = parsed_url['netloc'].split(':')[0]
    return len(re.findall(r'[@#$%&-]', domain))


def has_digits_in_domain(parsed_url):
    """
    Determines if the domain name contains digits.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    bool: True if the domain contains digits, False otherwise.
    """
    domain = parsed_url['netloc'].split(':')[0]  # Exclude port if present
    return bool(re.search(r'\d', domain))

def get_number_of_digits_in_domain(parsed_url):
    """
    Counts the number of digits in the domain name.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    int: The count of digits in the domain name.
    """
    domain = parsed_url['netloc'].split(':')[0]
    return len(re.findall(r'\d', domain))

def has_repeated_digits_in_domain(parsed_url):
    """
    Checks if the domain name has repeated digits.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    bool: True if there are repeated digits in the domain, False otherwise.
    """
    domain = parsed_url['netloc'].split(':')[0]
    return bool(re.search(r'(\d)\1', domain))

def get_number_of_subdomains(parsed_url):
    """
    Counts the number of subdomains in the URL.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    int: The number of subdomains.
    """
    domain = parsed_url['netloc'].split(':')[0].split('.')
    # Count subdomains excluding the main domain (last two parts)
    return len(domain) - 2 if len(domain) > 2 else 0

def has_dot_in_subdomain(parsed_url):
    """
    Determines if any subdomain contains a dot.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    bool: True if a subdomain contains a dot, False otherwise.
    """
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]  # Ignore main domain
    return any('.' in subdomain for subdomain in subdomains)

def has_hyphen_in_subdomain(parsed_url):
    """
    Checks if any subdomain contains a hyphen.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    bool: True if a subdomain contains a hyphen, False otherwise.
    """
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]  # Ignore main domain
    return any('-' in subdomain for subdomain in subdomains)

def get_average_subdomain_length(parsed_url):
    """
    Calculates the average length of subdomains.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    float: Average length of subdomains.
    """
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]  # Ignore main domain
    if subdomains:
        return sum(len(subdomain) for subdomain in subdomains) / len(subdomains)
    return 0.0

def get_average_number_of_dots_in_subdomain(parsed_url):
    """
    Calculates the average number of dots in subdomains.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    float: Average number of dots in subdomains.
    """
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]
    if subdomains:
        return sum(subdomain.count('.') for subdomain in subdomains) / len(subdomains)
    return 0.0

def get_average_number_of_hyphens_in_subdomain(parsed_url):
    """
    Calculates the average number of hyphens in subdomains.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    float: Average number of hyphens in subdomains.
    """
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]
    if subdomains:
        return sum(subdomain.count('-') for subdomain in subdomains) / len(subdomains)
    return 0.0


def has_special_characters_in_subdomain(parsed_url):
    """
    Determines if any subdomain contains special characters.
    
    Args:
    parsed_url (dict): The parsed URL components.
    
    Returns:
    bool: True if any subdomain contains special characters, False otherwise.
    """
    special_chars = re.compile(r'[@#$%&-]')
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]  # Ignore main domain
    return any(special_chars.search(subdomain) for subdomain in subdomains)



def get_number_of_special_characters_in_subdomain(parsed_url):
    """
    Counts the number of special characters in subdomains.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    int: Total count of special characters in the subdomains.
    """
    special_chars = re.compile(r'[@#$%&-]')
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]
    return sum(len(special_chars.findall(subdomain)) for subdomain in subdomains)

def has_digits_in_subdomain(parsed_url):
    """
    Checks if any subdomain contains digits.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    bool: True if any subdomain contains digits, False otherwise.
    """
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]
    return any(re.search(r'\d', subdomain) for subdomain in subdomains)

def get_number_of_digits_in_subdomain(parsed_url):
    """
    Counts the number of digits in subdomains.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    int: Total count of digits in the subdomains.
    """
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]
    return sum(len(re.findall(r'\d', subdomain)) for subdomain in subdomains)

def has_repeated_digits_in_subdomain(parsed_url):
    """
    Checks for repeated consecutive digits in subdomains.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    bool: True if any subdomain has repeated digits, False otherwise.
    """
    subdomains = parsed_url['netloc'].split(':')[0].split('.')[:-2]
    return any(re.search(r'(\d)\1', subdomain) for subdomain in subdomains)

def has_path(parsed_url):
    """
    Determines whether the URL has a path component.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    bool: True if the URL has a path, False otherwise.
    """
    return bool(parsed_url['path'])

def get_path_length(parsed_url):
    """
    Measures the length of the path in the URL.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    int: The length of the path.
    """
    return len(parsed_url['path'])

def has_query(parsed_url):
    """
    Checks if the URL contains a query string.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    bool: True if there is a query string, False otherwise.
    """
    return bool(parsed_url['query'])

def has_fragment(parsed_url):
    """
    Checks if the URL contains a fragment.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    bool: True if there is a fragment, False otherwise.
    """
    return bool(parsed_url['fragment'])

def has_anchor(parsed_url):
    """
    Determines if the URL includes an anchor (often part of the fragment).

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    bool: True if an anchor is present, False otherwise.
    """
    return '#' in parsed_url['fragment']

def calculate_entropy(text):
    """
    Calculates the Shannon entropy of a string.

    Args:
    text (str): The input text for which to calculate entropy.

    Returns:
    float: The Shannon entropy of the input text.
    """
    if not text:
        return 0
    probability = {x: text.count(x) / len(text) for x in set(text)}
    entropy = -sum(p * log2(p) for p in probability.values())
    return entropy

def get_entropy_of_url(url):
    """
    Calculates the Shannon entropy of the entire URL.

    Args:
    url (str): The complete URL.

    Returns:
    float: The entropy of the URL.
    """
    return calculate_entropy(url)

def get_entropy_of_domain(parsed_url):
    """
    Calculates the Shannon entropy of the domain name in the URL.

    Args:
    parsed_url (dict): The parsed URL components.

    Returns:
    float: The entropy of the domain name.
    """
    domain = parsed_url['netloc'].split(':')[0]  # Exclude port if present
    return calculate_entropy(domain)

## function so we dont have to do all that each time lol

def preprocess_url_features(url):
    """
    Processes a URL to extract various features and returns them in an ordered dictionary.
    
    Args:
    url (str): The URL to be processed.
    
    Returns:
    OrderedDict: A dictionary containing all the extracted features in a defined order.
    The order is defined at this DOI:
    
        Front. Comput. Sci., 06 March 2024
        Sec. Computer Security
        Volume 6 - 2024 | https://doi.org/10.3389/fcomp.2024.1308634
    """
    parsed_url = parse_url(url)
    
    preprocessed_url = OrderedDict()

    preprocessed_url['url_length'] = get_url_length(url)
    preprocessed_url['number_of_dots_in_url'] = get_number_of_dots_in_url(url)
    preprocessed_url['having_repeated_digits_in_url'] = has_repeated_digits_in_url(url)
    preprocessed_url['number_of_digits_in_url'] = get_number_of_digits_in_url(url)
    preprocessed_url['number_of_special_char_in_url'] = get_number_of_special_char_in_url(url)
    preprocessed_url['number_of_hyphens_in_url'] = get_number_of_hyphens_in_url(url)
    preprocessed_url['number_of_underline_in_url'] = get_number_of_underline_in_url(url)
    preprocessed_url['number_of_slash_in_url'] = get_number_of_slash_in_url(url)
    preprocessed_url['number_of_questionmark_in_url'] = get_number_of_questionmark_in_url (url)
    preprocessed_url['number_of_equal_in_url'] = get_number_of_equal_in_url(url)
    preprocessed_url['number_of_at_in_url'] = get_number_of_at_in_url (url)
    preprocessed_url['number_of_dollar_in_url'] = get_number_of_dollar_in_url(url)
    preprocessed_url['number_of_exclamation_in_url'] = get_number_of_exclamation_marks_in_url(url)
    preprocessed_url['number_of_hashtag_in_url'] = get_number_of_hashtags_in_url(url)
    preprocessed_url['number_of_percent_in_url'] = get_number_of_percent_signs_in_url(url)
    preprocessed_url['domain_length'] = get_domain_length(parsed_url)
    preprocessed_url['number_of_dots_in_domain'] = get_number_of_dots_in_domain(parsed_url)
    preprocessed_url['number_of_hyphens_in_domain'] = has_hyphens_in_domain(parsed_url)
    preprocessed_url['having_special_characters_in_domain'] = has_special_characters_in_domain(parsed_url)
    preprocessed_url['number_of_special_characters_in_domain'] = get_number_of_special_characters_in_domain(parsed_url)
    preprocessed_url['having_digits_in_domain'] = has_digits_in_domain(parsed_url)
    preprocessed_url['number_of_digits_in_domain'] = get_number_of_digits_in_domain(parsed_url)
    preprocessed_url['having_repeated_digits_in_domain'] = has_repeated_digits_in_domain(parsed_url)
    preprocessed_url['number_of_subdomains'] = get_number_of_subdomains(parsed_url)
    preprocessed_url['having_dot_in_subdomain'] = has_dot_in_subdomain(parsed_url)
    preprocessed_url['having_hyphen_in_subdomain'] = has_hyphen_in_subdomain(parsed_url)
    preprocessed_url['average_subdomain_length'] = get_average_subdomain_length(parsed_url)
    preprocessed_url['average_number_of_dots_in_subdomain'] = get_average_number_of_dots_in_subdomain(parsed_url)
    preprocessed_url['average_number_of_hyphens_in_subdomain'] = get_average_number_of_hyphens_in_subdomain(parsed_url)
    preprocessed_url['having_special_characters_in_subdomain'] = has_special_characters_in_subdomain(parsed_url)
    preprocessed_url['number_of_special_characters_in_subdomain'] = get_number_of_special_characters_in_subdomain(parsed_url)
    preprocessed_url['having_digits_in_subdomain'] = has_digits_in_subdomain(parsed_url)
    preprocessed_url['number_of_digits_in_subdomain'] = get_number_of_digits_in_subdomain(parsed_url)
    preprocessed_url['having_repeated_digits_in_subdomain'] = has_repeated_digits_in_subdomain(parsed_url)
    preprocessed_url['having_path'] = has_path(parsed_url)
    preprocessed_url['path_length'] = get_path_length(parsed_url)
    preprocessed_url['having_query'] = has_query(parsed_url)
    preprocessed_url['having_fragment'] = has_fragment(parsed_url)
    preprocessed_url['having_anchor'] = has_anchor(parsed_url)
    preprocessed_url['entropy_of_url'] = get_entropy_of_url(url)
    preprocessed_url['entropy_of_domain'] = get_entropy_of_domain(parsed_url)

    return preprocessed_url
