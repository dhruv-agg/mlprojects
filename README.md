### Create a Git repo

### Create a Virtual Env
```sh
conda create -p venv python==3.8 -y
conda activate <path/to/folder>/venv
git init
git add README.md
git commit -m "first commit" 
git push -u origin main
```
### Create .gitignore 
```sh
git pull origin main
touch setup.py
touch requirements.txt
mkdir src
touch src/__init__.py
mkdir src/components
touch src/components/__init__.py
touch src/components/data_ingestion.py
touch src/components/data_validation.py
touch src/components/data_transformation.py
touch src/components/model_trainer.py      
mkdir src/pipeline  
touch src/pipeline/train_pipeline.py       
touch src/pipeline/predict_pipeline.py
touch src/pipeline/__init__.py        
touch src/logger.py           
touch src/exceptions.py
touch src/utils.py
```
