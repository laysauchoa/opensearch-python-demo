"""
This file provides a formatting to easily read our results.
It is used as support when running the queries.

"""

from pprint import pprint


def log_titles(result):
    """
    Parses our search results to an easy
    read format containing animal's name and ID."""
    try:
        hits = result["hits"]["hits"]
        pprint(
            [
                "Name: "
                + res["_source"]["animal_name"]
                + " and Chip ID: "
                + res["_source"]["id_chip_number"]
                for res in hits
            ]
        )
    except Exception as e:
        print("Error has occurred: %s", e)
