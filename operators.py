import bpy

from . import env


class demo_operator(bpy.types.Operator):
    """Tool Tip"""
    bl_idname = env.id + \
        ".offsetmirroreduvs"  # best to put plugin name then obperator name # must be all lowercase
    bl_label = "OffsetMirroredUVs"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        return demo_execute(self, context)


def demo_execute(self, context):
    return {'FINISHED'}


# REGISTRATION

classes = [demo_operator]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
