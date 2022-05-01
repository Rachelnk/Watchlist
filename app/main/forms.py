from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Inputrequired
class ReviewForm(FlaskForm):

    # title = StringField('Review title',validators=[Required()])
    # review = TextAreaField('Movie review', validators=[Required()])
    title = StringField('Review title')
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')