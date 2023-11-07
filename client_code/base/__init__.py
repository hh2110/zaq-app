from ._anvil_designer import baseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

from ..home import home
from ..add_data import add_data

class base(baseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.change_sign_in_text()
    self.content_panel.add_component(home())
    self.toggle_content_panel_visiblity()

  def toggle_content_panel_visiblity(self):
    self.content_panel.visible = anvil.users.get_user() is not None

  def go_to_page(self, target):
    self.content_panel.clear()
    self.content_panel.add_component(target)

  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      self.sign_in.text = user["email"]
    else:
      self.sign_in.text = "Sign In"

  def add_data_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_page(target=add_data())

  def dashboard_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_page(target=home())

  def view_data_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_page(target=home())

  def reports_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_page(target=home())

  def title_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_page(target=home())

  def sign_in_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user:
      logout = confirm("Would you like to logout?")
      if logout:
        anvil.users.logout()
        self.go_to_page(target=home())
    else:
      anvil.users.login_with_form()
    
    self.change_sign_in_text()
    self.toggle_content_panel_visiblity()
