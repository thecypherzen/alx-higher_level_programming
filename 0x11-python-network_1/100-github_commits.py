#!/usr/bin/python3
"""A script that lists 10 commits (from the most recent to oldest) of the
   repository “rails” by the user “rails.

   => must use the Github API
   => print commits like so: `<sha>: <author name>` (one per line)
"""
if __name__ == "__main__":
    import requests
    import sys

    _token = "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"
    _owner = sys.argv[2]
    _repo = sys.argv[1]
    url = f"https://api.github.com/repos/{_owner}/{_repo}/commits"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    params = {"per_page": 20}
    response = requests.get(url, headers=headers, params=params).json()
    try:
        response.sort(key=lambda entry: entry['commit']['author']['date'],
                      reverse=True)
        # id = response.get("id", None)
        for commit in response:
            sha = commit.get("sha", None)
            commit = commit.get("commit", None)
            if commit:
                # print(commit)
                author = commit.get("author")
                print(f"{sha}: {author['name']}")
                # break
    except Exception as e:
        print("Error: ", response)
