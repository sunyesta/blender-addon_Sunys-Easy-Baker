from . import env
from . import sceneConfig
from . import operators
from . import ui


bl_info = {
    "name": env.name,
    "author": "Mary",
    "version": (1, 0, 1),
    "description": "Bake by name and export to substance painter",
    "blender": (3, 5, 0),
    "location": "View3D > Sidebar > Suny > Sunys Easy Baker",
    "warning": "",
    "category": "Mesh",
    "tracker_url": "",
    "wiki_url": ""
}

# ORDER IS IMPORTANT !
modules = [
    sceneConfig,
    operators,
    ui

]


def register():
    for m in modules:
        m.register()


def unregister():
    for m in reversed(modules):
        m.unregister()


if __name__ == "__main__":
    register()
