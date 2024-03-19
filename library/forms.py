
from django import forms
from library.models import Book

class BookForm(forms.Form):
    name = forms.CharField(label='Book Title' , max_length=100)
    price = forms.IntegerField(label="Price")
    no_ofpages = forms.IntegerField(label="no. of Pages")
    author = forms.CharField(label='Author' , max_length=100)
    image = forms.ImageField(label='Image')

    # def clean_email(self):
    #     email= self.cleaned_data['email']
    #     # check if email exists before ? return to page --> display form errors

    #     if Student.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email already exists")

    #     return email


    # def clean_name(self):
    #     name= self.cleaned_data['name']
    #     if len(name) < 2:
    #          raise forms.ValidationError("Name must be at least 2 characters ")
    #     return name


## generate form based on the model
### model form ?

# class StudentModelForm(forms.ModelForm):
#     class Meta:
#         model= Student
#         # fields = ['name', 'age', 'email', 'image']
#         fields='__all__'


#     def clean_email(self):
#         """ when you raise error
#         if the email already exists in another instance not in current instance

#         self ==> modelform
#         in case of create instance--> email ==> null

#         if case of edit instance --> already created instance.email != email


#         """
#         email= self.cleaned_data['email']

#         if (Student.objects.filter(email=email).exists()
#                 and self.instance.email!=email):
#             raise forms.ValidationError("Email already exists")

#         return email


#     def clean_name(self):
#         name= self.cleaned_data['name']
#         if len(name) < 2:
#              raise forms.ValidationError("Name must be at least 2 characters ")
#         return name

    ## override save function
    # def save(self, commit=True):
    #     pass