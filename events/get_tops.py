""" Get tops API """
from datetime import datetime
from collections import Counter
from pymongo import MongoClient

# Mongo Credentials
URI = 'mongodb://nds_user:Nearshor3.@ds151207.mlab.com:51207/news-sentiments'
CLIENT = MongoClient(URI,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)
DATABASE = CLIENT.get_default_database()

def search_tops_author(author, from_txt, to_txt):
    """ Searches tops for author

    Checks in the database for the top information found in the
    news of an author

    Args:
        author(string):    Name of the author
        from_txt(string):  Start date
        to_txt(string):    End date

    Returns:
        string: Top Entities found
        string: Top Keywords found
        string: Top Concepts found
    """
    if from_txt and to_txt is not None:
        from_date, to_date = correct_format(from_txt, to_txt)

        data = list(DATABASE.news.find({"$and":
                                            [{"analysis.metadata.authors.name": author},
                                             {"date": {"$gte": from_date, "$lt": to_date}}]}))
    else:
        data = list(DATABASE.news.find({"analysis.metadata.authors.name": author}))

    return search_data(data)

def search_tops_newspaper_subject(subject, newspaper, from_txt, to_txt):
    """ Searches tops for subject in a newspaper

    Checks in the database for the top information found in the
    news of a newspaper which contains a subject

    Args:
        subject(string):   Subject in the news
        newspaper(string): Name of the newspaper
        from_txt(string):  Start date
        to_txt(string):    End date

    Returns:
        string: Top Entities found
        string: Top Keywords found
        string: Top Concepts found
    """
    subject = subject.lower()

    if from_txt and to_txt is not None:
        from_date, to_date = correct_format(from_txt, to_txt)

        data = list(DATABASE.news.find({"$and":
                                            [{"subject": subject},
                                             {"newspaper": newspaper},
                                             {"date": {"$gte": from_date, "$lt": to_date}}]}))
    else:
        data = list(DATABASE.news.find({"$and":
                                            [{"subject": subject},
                                             {"newspaper": newspaper}]}))
    return search_data(data)

def search_tops_newspaper(newspaper, from_txt, to_txt):
    """ Searches tops for a newspaper

    Checks in the database for the top information found in the
    news of a newspaper

    Args:
        Newspaper(string): Name of the newspaper
        from_txt(string):  Start date
        to_txt(string):    End date

    Returns:
        string: Top Entities found
        string: Top Keywords found
        string: Top Concepts found
    """
    if from_txt and to_txt is not None:
        from_date, to_date = correct_format(from_txt, to_txt)

        data = list(DATABASE.news.find({"$and":
                                            [{"newspaper": newspaper},
                                             {"date": {"$gte": from_date, "$lt": to_date}}]}))
    else:
        data = list(DATABASE.news.find({"newspaper": newspaper}))

    return search_data(data)

def search_tops(from_txt, to_txt):
    """ Searches tops in the database

    Checks in the database for the top information found in all the
    news

    Args:
        from_txt(string):  Start date
        to_txt(string):    End date

    Returns:
        string: Top Entities found
        string: Top Keywords found
        string: Top Concepts found
    """
    if from_txt and to_txt is not None:
        from_date, to_date = correct_format(from_txt, to_txt)
        data = list(DATABASE.news.find({"date": {"$gte": from_date, "$lt": to_date}}))
    else:
        data = list(DATABASE.news.find())

    return search_data(data)

def search_tops_subject(subject, from_txt, to_txt):
    """ Searches tops for a subject

    Checks in the database for the top information found in the
    news of a subject

    Args:
        subject(string):  subject to be searched for
        from_txt(string): Start date
        to_txt(string):   End date

    Returns:
        string: Top Entities found
        string: Top Keywords found
        string: Top Concepts found
    """
    subject = subject.lower()

    if from_txt and to_txt is not None:
        from_date, to_date = correct_format(from_txt, to_txt)

        data = list(DATABASE.news.find({"$and":
                                            [{"subject": subject},
                                             {"date": {"$gte": from_date, "$lt": to_date}}]}))
    else:
        data = list(DATABASE.news.find({"subject": subject}))

    return search_data(data)

def search_tops_entity(entity, from_txt, to_txt):
    """ Searches tops for an entity

    Checks in the database for the top information found in the
    news of an entity

    Args:
        entity(string):   entity to be searched for
        from_txt(string): Start date
        to_txt(string):   End date

    Returns:
        string: Top Entities found
        string: Top Keywords found
        string: Top Concepts found
    """
    if from_txt and to_txt is not None:
        from_date, to_date = correct_format(from_txt, to_txt)
        data = list(DATABASE.news.find({"$and":
                                            [{"analysis.entities.text": entity},
                                             {"date": {"$gte": from_date, "$lt": to_date}}]}))
    else:
        data = list(DATABASE.news.find({"analysis.entities.text": entity}))

    return search_data(data)


def search_tops_concept(concept, from_txt, to_txt):
    """ Searches tops for concept

    Checks in the database for the top information found in the
    news of a concept

    Args:
        concept(string):  concept to be searched for
        from_txt(string): Start date
        to_txt(string):   End date

    Returns:
        string: Top Entities found
        string: Top Keywords found
        string: Top Concepts found
    """
    if from_txt and to_txt is not None:
        from_date, to_date = correct_format(from_txt, to_txt)
        data = list(DATABASE.news.find({"$and":
                                            [{"analysis.concepts.text": concept},
                                             {"date": {"$gte": from_date, "$lt": to_date}}]}))
    else:
        data = list(DATABASE.news.find({"analysis.concepts.text": concept}))

    return search_data(data)

def correct_format(from_txt, to_txt):
    """ Get the correct format for the date

    Corrects the string format of the date to get a fittable one for
    using it when searching in the database.

    Args:
        from_txt(string): Start date to be transformed
        to_txt(string):   End date to be transformed

    Returns:
        string: Transformed start date
        string: Transformed end date
    """
    from_date = datetime.strptime(from_txt + ' 0:00', '%Y-%m-%d %H:%M')
    to_date = datetime.strptime(to_txt +' 0:00', '%Y-%m-%d %H:%M')

    return from_date, to_date

def search_data(data):
    """ Get the important data (keywords, concepts and entities)

    Shortens the database answer to only return what was asked
    (keywords, concepts and entities)

    Args:
        data(list): Database returned values

    Returns:
        list: entities list
        list: keywords list
        list: concepts list
    """

    # Whole values returned
    entities = []
    keywords = []
    concepts = []

    for element in data:
        try:
            for entity in element["analysis"]["entities"]:
                entities.append(entity["text"])
        except KeyError as key_error:
            print(key_error)

        try:
            for keyword in element["analysis"]["keywords"]:
                keywords.append(keyword["text"])
        except KeyError as key_error:
            print(key_error)

        try:
            for concept in element["analysis"]["concepts"]:
                concepts.append(concept["text"])
        except KeyError as key_error:
            print(key_error)

    top_entities = get_common(entities)
    top_keywords = get_common(entities)
    top_concepts = get_common(entities)

    return top_entities, top_concepts, top_keywords


def get_common(data):
    """ Get the top common words

    Add to a list the top 20 common words of the entered
    data

    Args:
        data(list): words to be ordered

    Returns:
        list: list with the top 20 words
    """
    common_data = []
    common_counter = Counter(data)

    for data_element in common_counter.most_common()[:20]:
        common_data.append({
            "category": data_element[0],
            "total":    data_element[1]
        })

    return common_data
