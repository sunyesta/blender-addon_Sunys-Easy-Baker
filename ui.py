import bpy

from . import env
from . import operators
from . import sceneConfig


class objectPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = env.name
    bl_idname = env.id+"_object"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = env.bl_category  # the tab name
    bl_context = "objectmode"

    def draw(self, context):  # the stuff in the panel
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.operator(operators.demo_operator.bl_idname,
                     text="demo operator")

        row = layout.row()
        row.prop(sceneConfig.getSceneProps(), "lowPrefix")
        row.prop(sceneConfig.getSceneProps(), "highPrefix")


classes = [objectPanel]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
