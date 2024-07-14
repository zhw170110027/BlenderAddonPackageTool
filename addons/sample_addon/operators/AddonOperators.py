import bpy
import json

from addons.sample_addon.config import __addon_name__
from addons.sample_addon.preference.AddonPreferences import ExampleAddonPreferences


# This Example Operator will scale up the selected object
class ExampleOperator(bpy.types.Operator):
    '''ExampleAddon'''
    bl_idname = "object.example_ops"
    bl_label = "ExampleOperator"

    # 确保在操作之前备份数据，用户撤销操作时可以恢复
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)
        # use operator
        # bpy.ops.transform.resize(value=(2, 2, 2))

        # manipulate the scale directly
        context.active_object.scale *= addon_prefs.number

        objects =bpy.data.objects

        # 创建一个字典列表，其中每个字典表示一个对象的基本信息
        objects_info = [{'name': obj.name, 'type': type(obj).__name__} for obj in bpy.data.objects]

        # 将字典列表转换为JSON字符串
        objects_str = json.dumps(objects_info, indent=4)
        print(objects_str)
        # for 循环
        # for index, point in enumerate(full_path):
        #     print(f"点 {index + 1}: 经度: {point[0]}, 纬度: {point[1]}, 海拔: {point[2]}")

        return {'FINISHED'}
