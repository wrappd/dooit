from typing import List
from dooit.api.model import Model
from dooit.api.todo import Todo
from dooit.api.workspace import Workspace
from dooit.ui.events.events import SwitchTab
from dooit.ui.widgets.todo import TodoWidget
from .tree import Tree


class TodoTree(Tree):
    _empty = "todo"

    ModelType = Todo
    WidgetType = TodoWidget

    def __init__(self, model: Workspace):
        super().__init__(model, classes="right-dock")

    def get_children(self, parent: Model) -> List[ModelType]:
        return parent.todos

    async def switch_pane(self):
        self.post_message(SwitchTab())
