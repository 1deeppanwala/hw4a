import requests
import json

def get_user_repositories(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = json.loads(response.text)
        return [repo["name"] for repo in repos]
    else:
        print("Error fetching repositories:", response.text)
        return []

def get_repo_commits(user_id, repo_name):
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = json.loads(response.text)
        return len(commits)
    else:
        print("Error fetching commits:", response.text)
        return 0

def get_user_repo_commits(user_id):
    repos = get_user_repositories(user_id)
    user_commits = []
    for repo in repos:
        commits = get_repo_commits(user_id, repo)
        user_commits.append((repo, commits))
    return user_commits

def main():
    user_id = input("Enter GitHub user ID: ")
    repo_commits = get_user_repo_commits(user_id)
    for repo, commits in repo_commits:
        print(f"Repo: {repo} Number of commits: {commits}")

if __name__ == "__main__":
    main()
