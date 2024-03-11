from setuptools import find_packages,setup

setup(
    name = 'quizgenerator',
    version= '0.0.1',
    author = 'Rakesh kanth',
    author_email = 'rakeshkanth77@gmail.com',
    install_requires = ['openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    packages = find_packages()
)