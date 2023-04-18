# Layout of code is from zenbbq

import bpy
from bpy.types import PropertyGroup
from bpy.props import BoolProperty, FloatProperty, IntProperty, StringProperty, PointerProperty, EnumProperty


class SunysEasyBaker_SceneProps(PropertyGroup):
    lowPrefix: StringProperty(
        name="low prefix",
        description="",
        default="_low")

    highPrefix: StringProperty(
        name="high prefix",
        description="",
        default="_high")


def register():

    # register scene props
    bpy.utils.register_class(SunysEasyBaker_SceneProps)
    bpy.types.Scene.SunysEasyBaker = PointerProperty(
        type=SunysEasyBaker_SceneProps)


def unregister():

    # unregister scene props
    bpy.utils.unregister_class(SunysEasyBaker_SceneProps)
    del bpy.types.Scene.SunysEasyBaker


def getSceneProps():
    return bpy.context.scene.SunysEasyBaker

# userConfig = bpy.context.scene.ZBBQ_PreviewRenderUserConfig
# ZBBQ_PreviewRenderConfigForSaving
