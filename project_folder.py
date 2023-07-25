import os

def create_project_folder_template(role):
    if role not in ["data_analyst", "data_engineer", "data_scientist"]:
        print("Invalid role. Please choose from data_analyst, data_engineer, or data_scientist.")
        return
    
    project_folder = f"{role}_project/"
    
    # Directories for all roles
    directories = ["data_collection", "data_processing", "dashboards_and_reports", "deployment", "ui", "tests"]
    
    if role == "data_analyst":
        directories += ["analysis"]
    elif role == "data_engineer":
        directories += ["data_storage", "data_pipeline"]
    elif role == "data_scientist":
        directories += ["data_exploration", "model_training"]
    
    os.makedirs(project_folder)
    
    for directory in directories:
        os.makedirs(os.path.join(project_folder, directory))
    
    # Files for all roles
    files = ["kafka_config.yml", "data_collector.py", "data_processor.py", "dashboard_builder.py",
             "report_generator.py", "docker-compose.yml", "deploy_script.sh", "index.html", "style.css",
             "script.js", "test_data_collection.py", "test_data_processing.py", "requirements.txt",
             "README.md", "LICENSE", ".gitignore", ".env"]
    
    if role == "data_analyst":
        files += ["data_analyst_notebook.ipynb"]
    elif role == "data_engineer":
        files += ["data_engineer_script.py"]
    elif role == "data_scientist":
        files += ["data_scientist_notebook.ipynb"]
    
    for file in files:
        open(os.path.join(project_folder, file), 'w').close()

if __name__ == "__main__":
    roles = ["data_analyst", "data_engineer", "data_scientist"]
    
    for role in roles:
        create_project_folder_template(role)
