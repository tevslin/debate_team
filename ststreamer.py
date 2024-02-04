# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:01:01 2024

@author: tevsl
"""
from io import StringIO
import streamlit as st

class ObservableStringIO(StringIO):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_callback = None
        self.container=st.empty()
        self.text=""

    def write(self, s):
        # Call the original write method
        super().write(s)
        # Notify about the change
        self.text+=s
        self.container.markdown(
            body=self.text,
            unsafe_allow_html=False,
        )