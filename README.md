# AI4AR Radiomics

AI4AR Prostate Cancer data visualization and radiomics analyses


## Project

This project structure is explained in: https://www.youtube.com/watch?v=seKOq-VMJgY&list=PLr752TWTU4tu-aq_rH5KuYrnvPuueW0Wy


## Requirements

Python 3.7.15 (pyradiomics)
 https://visualstudio.microsoft.com/visual-cpp-build-tools/

 
## Usage

### Creating an env

To create a Python virtual environment with the name ```ai4ar-radiomics-env```, you can use the following instructions:

Make sure that you have the ```virtualenv``` package installed on your system. You can install it using ```pip install virtualenv```.

Open a terminal and navigate to the directory where you want to create the virtual environment.

Run the following command to create the virtual environment:
```bash
virtualenv ai4ar-radiomics-env
```

To activate the virtual environment, use the following command:

```bash
source ai4ar-radiomics-env/bin/activate
```

You should now see the name of your virtual environment in the terminal prompt, indicating that it is active.

To deactivate the virtual environment, use the following command:
```bash
deactivate
```

https://docs.python.org/3/library/venv.html

### Building the book

If you'd like to develop and/or build the AI4AR Radiomics book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. (Optional) Edit the books source files located in the `ai4ar-radiomics/` directory
4. Run `jupyter-book clean ai4ar-radiomics/` to remove any existing builds
5. Run `jupyter-book build ai4ar-radiomics/`

A fully-rendered HTML version of the book will be built in `ai4ar-radiomics/_build/html/`.

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/piotrsobecki/ai4ar-radiomics/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).



## Data (example for subset of the raw dataset)

### Data Source

https://ai4ar.opi.org.pl/baza-obrazow-mpmri/#


Follow the instructions on the site. Download the CONT data, unzip uzing 7zip, place into the data directory (ie. ./data/raw), unzip.

Place the metadata (.csv files) in the directory (ex. ./data/raw)

The directory structure should reflect following:

### (Example) Directory structure

./data/trial/AI4AR_cont\Anatomical_Labels\001
./data/trial/AI4AR_cont\Anatomical_Labels\003
./data/trial/AI4AR_cont\Anatomical_Labels\004
./data/trial/AI4AR_cont\Anatomical_Labels\005
./data/trial/AI4AR_cont\Data\001
./data/trial/AI4AR_cont\Data\003
./data/trial/AI4AR_cont\Data\004
./data/trial/AI4AR_cont\Data\005
./data/trial/AI4AR_cont\Lesion_Labels\001\lesion1\adc
./data/trial/AI4AR_cont\Lesion_Labels\001\lesion1\dce3
./data/trial/AI4AR_cont\Lesion_Labels\001\lesion1\hbv
./data/trial/AI4AR_cont\Lesion_Labels\001\lesion1\t2w
./data/trial/AI4AR_cont\Lesion_Labels\001\lesion1
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion1\adc
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion1\dce3
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion1\hbv
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion1\t2w
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion2\adc
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion2\dce3
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion2\hbv
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion2\t2w
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion1
./data/trial/AI4AR_cont\Lesion_Labels\003\lesion2
./data/trial/AI4AR_cont\Lesion_Labels\004\lesion1\adc
./data/trial/AI4AR_cont\Lesion_Labels\004\lesion1\dce3
./data/trial/AI4AR_cont\Lesion_Labels\004\lesion1\hbv
./data/trial/AI4AR_cont\Lesion_Labels\004\lesion1\t2w
./data/trial/AI4AR_cont\Lesion_Labels\004\lesion1
./data/trial/AI4AR_cont\Lesion_Labels\001
./data/trial/AI4AR_cont\Lesion_Labels\003
./data/trial/AI4AR_cont\Lesion_Labels\004
./data/trial/AI4AR_cont\Lesion_Labels\005
./data/trial/AI4AR_cont\Anatomical_Labels
./data/trial/AI4AR_cont\Data
./data/trial/AI4AR_cont\Lesion_Labels
./data/trial/AI4AR_cont

./data/trial/AI4A4_PCa_clinical.csv
./data/trial/AI4AR_PCa_radiological.csv


