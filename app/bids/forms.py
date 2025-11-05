from django import forms
from .models import Bid

class BidForm(forms.ModelForm):
    """ 
    Form for placing a bid on a project.
    This form is tied to the Bid model and allows freelancers to
    input a bid amount and a message explaining their proposal.
    """

    class Meta:
        # Link this form to the Bid model
        model = Bid

        # Only include the following fields in the form
        fields = ['bid_amount', 'message']

        # Customize how each field is rendered in HTML
        widgets = {
            # Render bid_amount as a number input with decimal precision
            'bid_amount': forms.NumberInput(attrs={
                'step': '0.01',  # Allows decimals like 0.25, 1.50, etc.
                'min': '0.01',   # Prevents zero or negative bids
                'placeholder': 'Enter your bid amount'  # Placeholder text inside the input
            }),
            # Render message as a textarea with 5 rows
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Explain why you\'re the best fit for this project...'
            }),
        }

        # Define user-friendly labels for form fields
        labels = {
            'bid_amount': 'Your Bid Amount ($)',
            'message': 'Proposal Message',
        }

    def __init__(self, *args, **kwargs):
        """
        Customize field attributes (mainly CSS classes) after initialization.
        This ensures the fields match the app's design system or CSS framework.
        """
        # Call the parent constructor to initialize the form
        super().__init__(*args, **kwargs)

        # Add custom CSS classes and styles for the bid_amount field
        self.fields['bid_amount'].widget.attrs.update({
            'class': (
                'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden '
                'rounded-lg text-[#0d171b] dark:text-slate-50 focus:outline-0 focus:ring-0 '
                'border border-[#cfdfe7] dark:border-slate-700 bg-background-light '
                'dark:bg-background-dark focus:border-primary h-10 '
                'placeholder:text-[#6c757d] dark:placeholder:text-slate-400 '
                'px-[15px] text-sm font-normal leading-normal'
            )
        })

        # Add custom CSS classes and styles for the message field
        self.fields['message'].widget.attrs.update({
            'class': (
                'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden '
                'rounded-lg text-[#0d171b] dark:text-slate-50 focus:outline-0 focus:ring-0 '
                'border border-[#cfdfe7] dark:border-slate-700 bg-background-light '
                'dark:bg-background-dark focus:border-primary '
                'placeholder:text-[#6c757d] dark:placeholder:text-slate-400 '
                'px-[15px] py-2 text-sm font-normal leading-normal'
            )
        })
