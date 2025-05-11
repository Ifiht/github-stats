import requests
import argparse
import sys

def get_repo_languages(owner, repo, token=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Query GitHub repo languages.")
    parser.add_argument("owner", help="GitHub username or organization")
    parser.add_argument("repo", help="Repository name")
    parser.add_argument("--token", help="GitHub personal access token (optional)")

    args = parser.parse_args()

    languages = get_repo_languages(args.owner, args.repo, args.token)
    if languages:
        print("Languages used in the repo:")
        for lang, bytes_of_code in languages.items():
            print(f"{lang}: {bytes_of_code} bytes")

if __name__ == "__main__":
    main()
