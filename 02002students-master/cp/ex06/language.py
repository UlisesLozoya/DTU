"""Exercise 6.5: Languages."""

def get_people_by_language(language: str, name_languages: dict)-> list:
    """Return the names of people who speak a specific language.
    
    :param language: A string containing the desired language.
    :param name_languages: A dictionary containing the names of people along with their spoken languages
    :return: The names of people that speak the desired language.
    """
    # TODO: Code has been removed from here. 
if __name__ == "__main__":
    name_languages = {
    'Peter': ['Danish', 'English'],
    'Alice': ['English', 'French'],
    'John': ['Spanish', 'English'],
    'Maria': ['Danish', 'Spanish'],
    'Anna': ['German', 'English']
    }
    print(get_people_by_language('English', name_languages))
