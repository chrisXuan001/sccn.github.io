import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=False, text=True)
    if result.returncode != 0:
        print(f"Command failed: {command}\nError: {result.stderr}")
    return result

def update_repo(repo, script, plugin_type='readme'):
    print(f"Updating {repo}...")
    current_dir = os.getcwd()
    repo_path = os.path.join(current_dir, 'github', repo)
    
    if os.path.exists(repo_path):
        os.chdir(repo_path)
        run_command('git pull')
    else:
        if plugin_type == "wiki":
            run_command(f'git clone https://github.com/sccn/{repo}.wiki.git {repo_path}')
        else:
            run_command(f'git clone https://github.com/sccn/{repo}.git {repo_path}')
        
    os.chdir(current_dir)
    run_command(f'python {script} {repo_path} {repo} {plugin_type}')

if __name__ == "__main__":
    # if 'github' not in current directory, create it
    if not os.path.exists('github'):
        os.makedirs('github')

    # wiki_plugins = ['SIFT', 'get_chanlocs', 'NFT', 'PACT', 'nsgportal', 'clean_rawdata']
    # for plugin in wiki_plugins:
    #     update_repo(plugin, "reformat_plugin.py", 'wiki')
    readme_plugins = ['ARfitStudio'] #, 'roiconnect', 'EEG-BIDS', 'trimOutlier', 'groupSIFT', 'nwbio', 'ICLabel', 'dipfit', 'eegstats', 'PowPowCAT', 'PACTools', 'zapline-plus', 'amica', 'fMRIb', 'relica', 'std_dipoleDensity', 'imat', 'viewprops', 'cleanline','NIMA', 'firfilt']
    for plugin in readme_plugins:
        update_repo(plugin, "reformat_plugin.py", "readme")
