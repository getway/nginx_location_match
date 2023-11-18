# -*- coding: utf-8 -*-
import re


def nginx_location_match(uri, locations):
    """
    Simulates Nginx's location block matching process with added safety checks for regex.

    Parameters:
    uri (str): The URI to be matched.
    locations (list): A list of Nginx location configurations.

    Returns:
    dict: Match results including exact, prefix, regex matches, the best match, and the reason.
    """
    exact_matches, prefix_matches, regex_matches = [], [], []
    best_match, reason = None, ""

    uri = uri.strip()  # Handling spaces in URI

    for location in locations:
        location_trimmed = location.strip()  # Handling spaces in location

        if location_trimmed.startswith('='):
            if uri == location_trimmed[1:]:
                exact_matches.append(location_trimmed)
                best_match, reason = location_trimmed, "Exact match"
                break
        elif location_trimmed.startswith('~'):
            try:
                if re.match(location_trimmed[1:], uri):
                    regex_matches.append(location_trimmed)
                    if not best_match:
                        best_match, reason = location_trimmed, "First regular expression match"
            except re.error:
                continue  # Skip invalid regex
        elif location_trimmed.startswith('~*'):
            try:
                if re.match(location_trimmed[2:], uri, re.IGNORECASE):
                    regex_matches.append(location_trimmed)
                    if not best_match:
                        best_match, reason = location_trimmed, "First regular expression match"
            except re.error:
                continue  # Skip invalid regex
        else:
            if uri.startswith(location_trimmed):
                prefix_matches.append(location_trimmed)
                if not best_match or len(location_trimmed) > len(best_match):
                    best_match, reason = location_trimmed, "Longest prefix match"

    return {
        "exact_matches": exact_matches,
        "prefix_matches": prefix_matches,
        "regex_matches": regex_matches,
        "best_match": best_match,
        "reason": reason
    }


if __name__ == '__main__':
    # Corrected example usage with valid regex patterns and safety checks
    uri = "/images/photo.jpg"
    locations = ["= /images/photo.jpg", "/images/", "~* \\.jpg$", "~ \\.png$"]
    nginx_match_data = nginx_location_match(uri, locations)
    print(nginx_match_data)
