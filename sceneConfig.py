# Layout of code is from zenbbq

import bpy
from bpy.types import PropertyGroup
from bpy.props import BoolProperty, FloatProperty, IntProperty, StringProperty, PointerProperty, EnumProperty


class SunysEasyBaker_SceneProps(PropertyGroup):
    isSet: BoolProperty(
        name="Is set",
        description="Was it written at least once?",
        default=False)


def register():

    # register scene props
    bpy.utils.register_class(SunysEasyBaker_SceneProps)
    bpy.types.Scene.SunysEasyBaker = PointerProperty(
        type=SunysEasyBaker_SceneProps)


def unregister():

    # unregister scene props
    bpy.utils.unregister_class(SunysEasyBaker_SceneProps)
    del bpy.types.Scene.SunysEasyBaker


# userConfig = bpy.context.scene.ZBBQ_PreviewRenderUserConfig
# ZBBQ_PreviewRenderConfigForSaving
