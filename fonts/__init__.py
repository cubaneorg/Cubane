# coding=UTF-8
from __future__ import unicode_literals


# hook into resource pipeline and replace font references with actual
# css resources generated by the font cache.
def install_resource_manager(resource_manager):
    from cubane.fonts.extensions import ResourceManagerExtension
    return resource_manager.register_extension(ResourceManagerExtension)