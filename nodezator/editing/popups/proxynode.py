
### local imports

from config import APP_REFS

from menu.main import MenuManager

from editing.popups.constants import GeneralPopupCommands


class ProxyNodePopupMenu(GeneralPopupCommands):

    def __init__(self):

        super().__init__()

        redirect_node_menu_list = [

          {
             'label': "Move this node",
             'command': self.move_obj,
          },

          {
             'label': "Duplicate this node",
             'command': self.duplicate_obj,
          },

          {
             'label'   : "Delete this node",
             'command' : self.delete_obj,
          },

        ]

        self.redirect_node_only_popup = (

          MenuManager(

            redirect_node_menu_list,

            is_menubar  = False,
            use_outline = True,
            keep_focus_when_unhovered=True,

          )

        )

        ###

        data_node_menu_list = redirect_node_menu_list.copy()

        data_node_menu_list.insert(

          0,

          {
            'label'   : "Edit this node's title",
            'command' : self.edit_node_title,
          },

        )

        self.data_node_only_popup = (

          MenuManager(

            data_node_menu_list,

            is_menubar  = False,
            use_outline = True,
            keep_focus_when_unhovered=True,

          )

        )

        ###

        redirect_node_menu_list.extend(
          self.GENERAL_COLLECTIVE_COMMANDS
        )

        self.redirect_node_and_selected_popup = (

          MenuManager(

            redirect_node_menu_list,

            is_menubar  = False,
            use_outline = True,
            keep_focus_when_unhovered=True,

          )

        )

        ###

        data_node_menu_list.extend(
          self.GENERAL_COLLECTIVE_COMMANDS
        )

        self.data_node_and_selected_popup = (

          MenuManager(

            data_node_menu_list,

            is_menubar  = False,
            use_outline = True,
            keep_focus_when_unhovered=True,

          )

        )

    def show(self, proxy_node, mouse_pos):

        self.obj_under_mouse = proxy_node

        if proxy_node in APP_REFS.ea.selected_objs:

            if hasattr(proxy_node.proxy_socket, 'parent'):

                (
                  self
                  .redirect_node_and_selected_popup
                  .focus_if_within_boundaries(mouse_pos) 
                )

            else:

                (
                  self
                  .data_node_and_selected_popup
                  .focus_if_within_boundaries(mouse_pos) 
                )

        else:

            if hasattr(proxy_node.proxy_socket, 'parent'):

                (
                  self
                  .redirect_node_only_popup
                  .focus_if_within_boundaries(mouse_pos) 
                )

            else:

                (
                  self
                  .data_node_only_popup
                  .focus_if_within_boundaries(mouse_pos) 
                )

    def edit_node_title(self):
        pass