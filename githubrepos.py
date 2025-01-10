
# Step 1: GitHub Integration - Fetching Public Repositories
# We'll use GitHub's REST API to get a list of repositories.

import requests
import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv()

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Use your GitHub token for authenticated requests.
if not GITHUB_TOKEN:
    raise ValueError("Please set the GITHUB_TOKEN environment variable with your GitHub personal access token.")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_repositories(query, per_page=5):
    """
    Fetch public repositories from GitHub based on a search query.
    :param query: Search query (e.g., "language:python stars:>1000").
    :param per_page: Number of repositories to fetch per request.
    :return: List of repositories.
    """
    url = f"{GITHUB_API_URL}/search/repositories?q={query}&per_page={per_page}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

# Example Usage
repositories = fetch_repositories("language:python stars:>1000")
for repo in repositories:
    print(f"Repository: {repo['full_name']} - Stars: {repo['stargazers_count']}")

# Step 2: Code Quality Analysis
# For analyzing the quality, we can use tools like Pylint, ESLint, or other linters for different languages.
import subprocess

def analyze_code(repo_url, local_dir):
    """
    Clone the repository and run code analysis tools like Pylint.
    :param repo_url: GitHub repository URL.
    :param local_dir: Local directory to clone the repository.
    """
    try:
        # Clone the repo
        subprocess.run(["git", "clone", repo_url, local_dir], check=True)
        
        # Run Pylint on Python code (as an example)
        result = subprocess.run(["pylint", local_dir], capture_output=True, text=True)
        print("Pylint Results:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while analyzing code: {e}")

# Example Usage
repo_url = repositories[0]['clone_url']
analyze_code(repo_url, "./cloned_repo")

# Step 3: Metrics and Evaluation
# You can expand the analysis based on:
# - Test Coverage (e.g., presence of tests, coverage percentage)
# - Documentation quality (e.g., README completeness)
# - Dependency updates, activity metrics, and best practices.

def evaluate_repo(repo):
    """
    Evaluate the repository based on certain criteria.
    :param repo: Repository details from GitHub API.
    :return: Evaluation score.
    """
    score = 0
    
    # Stars count as a metric of popularity
    score += repo['stargazers_count'] / 100
    
    # Has a README file?
    if 'README' in [file['name'] for file in requests.get(repo['url'] + '/contents', headers=headers).json()]:
        score += 5
    
    # Active repository (recent commits within the last 3 months)
    if repo['pushed_at']:
        from datetime import datetime, timedelta
        pushed_date = datetime.strptime(repo['pushed_at'], "%Y-%m-%dT%H:%M:%SZ")
        if pushed_date > datetime.now() - timedelta(days=90):
            score += 10
    
    # Presence of tests (e.g., files like test_*.py or directories named "tests")
    contents = requests.get(repo['url'] + '/contents', headers=headers).json()
    if any('test' in file['name'].lower() for file in contents):
        score += 10
    
    # Dependency management (e.g., presence of requirements.txt or package.json)
    if any(file['name'] in ['requirements.txt', 'package.json'] for file in contents):
        score += 5
    
    # Issue activity (e.g., open issues count)
    if repo['open_issues_count'] < 10:
        score += 5
    
    # Community engagement (e.g., number of forks, watchers)
    score += (repo['forks_count'] / 50) + (repo['watchers_count'] / 50)
    
    return score

# Example Usage
evaluated_score = evaluate_repo(repositories[0])
print(f"Evaluation Score: {evaluated_score}")

# Step 4: Extract Tech Stack and Provide Learning Resources
# Extract tech stack information and gather learning resources (could be done via tags or parsing code).

def extract_tech_stack(repo):
    """
    Extract the tech stack from the repository details or files.
    :param repo: Repository details from GitHub API.
    :return: List of technologies used in the repository.
    """
    tech_stack = []
    language = repo.get('language')
    if language:
        tech_stack.append(language)
    
    # Analyze files to extract more tech stack details (e.g., package.json for JavaScript, pom.xml for Java)
    contents = requests.get(repo['url'] + '/contents', headers=headers).json()
    for file in contents:
        if file['name'] == 'package.json':
            tech_stack.append('Node.js')
        elif file['name'] == 'pom.xml':
            tech_stack.append('Java')
    
    return tech_stack

# Example Usage
tech_stack = extract_tech_stack(repositories[0])
print(f"Tech Stack: {tech_stack}")

# Step 5: Learning Assistance
# Suggest learning resources based on the extracted tech stack.

def suggest_learning_resources(tech_stack):
    """
    Suggest learning resources for the given tech stack.
    :param tech_stack: List of technologies used in the repository.
    """
    resources = {
        "Python": ["https://docs.python.org/3/tutorial/", "https://www.learnpython.org/"],
        "JavaScript": ["https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide", "https://javascript.info/"],
        "Node.js": ["https://nodejs.org/en/docs/guides/", "https://www.freecodecamp.org/news/learn-node-js/"],
        "Java": ["https://docs.oracle.com/javase/tutorial/", "https://www.codecademy.com/learn/learn-java"]
    }
    
    for tech in tech_stack:
        if tech in resources:
            print(f"Learning Resources for {tech}:")
            for link in resources[tech]:
                print(f"- {link}")

# Example Usage
suggest_learning_resources(tech_stack)