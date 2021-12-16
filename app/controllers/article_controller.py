"""Article controller"""
from flask import render_template
from app.controllers.controller import ControllerBase


# pylint: disable=too-few-public-methods

class ArticleController(ControllerBase):
    """Article controller class"""

    @staticmethod
    def get_oop():
        """Returns to oop.html"""
        return render_template('oop.html')

    @staticmethod
    def get_oop_glossary():
        """Returns to glossary.html"""
        return render_template('glossary.html')

    @staticmethod
    def get_solid():
        """Returns to solid.html"""
        return render_template('solid.html')
