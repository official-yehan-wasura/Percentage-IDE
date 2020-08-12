# -*- coding: utf-8 -*-
 
import os
from percentage_ide import translations
from percentage_ide.tools import json_manager
from percentage_ide.core.template_registry.bundled_project_types import initial_page
from percentage_ide.core.template_registry.ntemplate_registry import BaseProjectType


SETUP_PY_FILE = """
# BEWARE: This is a minimal version you will most likely need to extend it
from setuptools import setup, find_packages

setup(
    name='%s',
    version='1.0',
    packages=find_packages(),

)
"""

BASIC_HELLO = """
# This is a sample yet useful program, for python 3


def hello_world():
    print("hello world, this is %s's main")

"""


class PythonProject(BaseProjectType):

    type_name = "Basic Python Project"
    layout_version = "0.1"
    category = "Python"
    encoding_string = {"py": "# -*- coding: %s -*-"}
    single_line_comment = {"py": "# "}
    description = "This wizard will create a basic Python project."

    def create_layout(self, wizard):
        """
        Create set of folders and files required for a basic python project
        """
        # Create project path
        project_path = os.path.join(self.path, self.name)
        self._create_path(project_path)
        # Create a single init file
        filepath = os.path.join(project_path, "__init__.py")
        with open(filepath, "w") as base_init:
            self.init_file(base_init, filepath)
        # Create a setup.py
        filepath = os.path.join(project_path, "setup.py")
        with open(filepath, "w") as base_setup:
            self.init_file(base_setup, filepath)
            base_setup.write(SETUP_PY_FILE % self.name)
        # Create a basic main file
        filepath = os.path.join(project_path, "main.py")
        with open(filepath, "w") as base_main:
            self.init_file(base_main, filepath)
            base_main.write(BASIC_HELLO % self.name)
        # Create .pect file
        project = {}
        project["name"] = self.name
        project["project-type"] = self.category
        project["mainFile"] = "main.py"
        project["description"] = wizard.field("description")
        json_manager.create_percentage_project(project_path, self.name, project)
        # Open project in Explorer
        self._open_project(project_path)

    @classmethod
    def wizard_pages(cls):
        return (InitialPage(),)


class InitialPage(initial_page.InitialPage):

    def __init__(self):
        super().__init__()
        self.setTitle(translations.TR_WIZARD_PYTHON_PROJECT_TITLE)
        self.setSubTitle(translations.TR_WIZARD_PYTHON_PROJECT_SUBTITLE)


PythonProject.register()
