# Blender Add-on Development Framework and Packaging Tool

This project provides a lightweight, easy-to-use framework for developing and packaging Blender addons. The main
features include:

1. A single command to create a template add-on, facilitating quick development.
1. Support developing multiple addons in one project, which allows you to reuse functions across
   different addons, and helps you package only necessary modules into the zip file.
1. Allows you to run and test your add-on in Blender with a single command. Support hot swap
   for code updates. You can see the updates in Blender immediately after saving the code.
1. A single command to package the add-on into an installable addon package, making it easier for users to install. The
   packaging tool automatically detects and includes dependencies needed for the add-on within your project. (Not including 3rd party libraries)
1. Provide utility functions for basic development, like an auto-load utility for automatic class loading and an internationalization (i18n)
   tool, to help new developers creating high-quality addons.

You can check out an overview about this framework on YouTube: https://youtu.be/udPBrXJZT1g

The following external library will be installed automatically when you run the framework code, you can also install them
manually:

- https://github.com/nutti/fake-bpy-module
- https://github.com/gorakhargosh/watchdog

## Basic Framework

- [main.py](main.py): Configures the Blender path, add-on installation path, default add-on, package ignore files, and
  add-on release path, among other settings.
- [test.py](test.py): A testing tool to run and test add-ons.
- [create.py](create.py): A tool to create add-ons, allowing you to quickly create an add-on based on the `sample_addon`
  template.
- [release.py](release.py): A packaging tool that packages add-ons into an installable package.
- [addons](addons): A directory to store add-ons, with each add-on in its own sub-directory. Use `create.py` to quickly
  create a new add-on.
- [common](common): A directory to store shared utilities.

## Framework Development Guidelines

Blender Version >= 2.93

Each add-on, while adhering to the basic structure of a Blender add-on, should include a `config.py` file to configure
the add-on's package name, ensuring it doesn't conflict with other add-ons.
When importing dependencies, avoid using relative imports in __init__.py files, this file is copied to the root
directory so the path may change.

This project depends on the `addons` folder; do not rename this folder.

Do not define classes in the `__init__.py` file of an add-on. The `__init__.py` file is copied to the root directory of
the add-on when packaging the framework, which may result in classes being misused. To avoid this
issue, define classes in other files and import them in the `__init__.py` file as needed.

## Usage

1. Clone this repository.
1. Open this project in your IDE. Optional: Configure the IDE to use the same python interpreter as Blender.
1. Note: For PyCharm users, change the value idea.max.intellisense.filesize in idea.properties file ( Help | Edit Custom
   Properties.) to more than 2600 because some modules have the issue of being too big for intelliSense to work. You
   might also need to associate the __init__.pyi file as the python File Types
   in ![setting](https://i.ibb.co/QcYZytw/script.png) to get the auto code completion working.
1. Configure the name of the addon you want to create (ACTIVE_ADDON) in [main.py](main.py).
1. Run create.py to create a new addon in your IDE. The first time you run this, it will download dependencies,
   including
   watchdog and fake-bpy-module.
1. Develop your addon in the newly created addon directory.
1. Run test.py to test your addon in Blender.
1. Run release.py to package your addon into an installable package. The packaged addon path will appears in the
   terminal when packaged successfully.

## Features Provided by the Framework

1. You don't need to worry about register and unregister classes in Blender add-ons. The framework automatically loads
   and
   unloads classes in your add-ons. You just need to define your classes in the addon's folder.
1. You can use internationalization in your add-ons. Just add translations in the standard format to the `dictionary.py`
   file in the `i18n` folder of your add-on.
1. You can define RNA properties declaratively. Just follow the examples in the `__init__.py` file to add your RNA
   properties. The framework will automatically register and unregister your RNA properties.
1. You can use the `ExpandableUi` class in `common/types/framework.py` to easily extend Blender's native UI components,
   such as menus, panels, pie menus, and headers. Just inherit from this class and implement the `draw` method. You can
   specify the ID of the native UI component you want to extend using `target_id` and specify whether to append or
   prepend using `expand_mode`.

## Contributions

1. Framework Updates: If you are using this framework in your project and need to migrate to a newer version, you will
   need to manually replace the framework files to get the new features. We are looking for more user-friendly migration
   experience. In general, we aim to keep the framework lightweight and avoid making structural changes. Most future
   updates are expected to just adding new features rather than making major changes to the framework structure. So
   unless you personally made changes to the framework code locally, you will only need to replace the old files with
   the new ones in future updates.
1. Breakpoint Debugging: The framework currently does not support breakpoint debugging within the IDE. Implementing this
   feature requires some modifications to the framework code, which may increase the complexity of using the framework.
   We are looking for a lightweight solution to enable this feature. However, in general, breakpoint debugging is not
   necessary for developing add-ons. Breakpoint debugging is helpful for complex add-ons features, but logging is
   sufficient in most of the cases. For this framework, breakpoint debugging would be a nice-to-have feature, but not a
   must-have.

# Blender 插件开发框架及打包工具

本项目是一个轻量级的Blender插件开发框架和打包工具. 主要功能包括：

1. 一条命令创建模版插件，方便进行快速开发
1. 支持在一个项目中开发多个插件，可以让你在不同的插件之间复用函数功能，它可以自动检测功能模块之间的依赖关系，将相关联的模块打包到zip文件中，而不包含不必要的模块
1. 在IDE中可以通过一条命令在Blender上运行插件的测试, 支持代码热更新，保存代码后可以立即在Blender中看到变化
1. 一条命令将插件打包成一个安装包，方便用户安装，打包工具自动检测插件的依赖关系，自动打包插件所需的依赖文件(不包括引用的外部库)
1. 提供了常用的插件开发工具，比如自动加载类的auto_load工具，提供国际化翻译的i18n工具，方便新手开发者进行高水平插件开发

欢迎观看我们的中文视频教程：

- [B站](https://www.bilibili.com/video/BV1Gn4y1d7Bp)
- [YouTube](https://www.youtube.com/watch?v=Pjf7wg3IzDE&list=PLPkz3Ny42tJtxzw7xVUWvLI3FwEeETVOj&index=1&t=5s)

下外部库会在框架代码运行时自动安装，你也可以手动安装它们：

- https://github.com/nutti/fake-bpy-module
- https://github.com/gorakhargosh/watchdog

## 基础框架

[main.py](main.py): 可以配置Blender路径，插件安装路径，当前默认插件，打包ignore文件，插件发布路径等

[test.py](test.py): 测试工具，可以运行插件的测试

[create.py](create.py): 创建插件的工具，可以根据sample_addon模版快速创建一个插件

[release.py](release.py): 打包工具，可以将插件打包成一个安装包

[addons](addons): 存放插件的目录，每个插件一个目录，使用create.py可以快速创建一个插件

[common](common): 存放公共工具的目录

## 框架开发要求

Blender 版本 >= 2.93

每个插件在符合Blender插件的结构基础上，需要有一个config.py文件用于配置插件的包名，避免与其他插件冲突。
在导入依赖时需要书写完整包名，比如 `from addons.sample_addon.config import __addon_name__`
避免在__init__文件中使用相对路径导入，比如 `from .config import __addon_name__`，__init__文件在打包时会被复制到插件的根目录，会导致路径变换

注意项目依赖addons文件夹，请勿更改这个文件夹的名称。

请不要在插件的__init__.py文件中定义类，__init__.py文件在框架打包时会被复制到插件的根目录，可能会导致插件中包含重复的类导致意外情况。
为避免这个问题，请将插件的类定义到其他文件中，然后在需要时在__init__.py文件中导入这些类。

## 使用说明

1. 克隆此项目。
1. 在您的 IDE 中打开此项目。你可以将IDE使用的Python.exe配置成与Blender相同。
1. 对于PyCharm用户，请将idea.properties文件(点击 Help | Edit Custom Properties.)
   中的idea.max.intellisense.filesize的值更改为大于2600，因为某些模块的大小超过了intelliSense的工作范围。你可能需要将__init__
   .pyi文件关联到python File Types ![setting](https://i.ibb.co/QcYZytw/script.png) 以使自动代码补全正常工作。
1. 在 [main.py](main.py) 中配置 Blender 可执行文件路径（BLENDER_EXE_PATH）
1. 在 [main.py](main.py) 中配置您想要创建的插件名称（ACTIVE_ADDON）。
1. 运行 create.py 在您的 IDE 中创建一个新的插件。第一次运行时需要联网下载依赖库,包括watchdog和fake-bpy-module
1. 在新创建的插件目录中开发您的插件。
1. 运行 test.py 在 Blender 中测试您的插件。
1. 运行 release.py 将您的插件打包成可安装的包。成功打包后，终端中将显示打包插件的路径。

## 框架提供的功能

1. 你基本上无需关心Blender插件的类的加载和卸载，框架会自动加载和卸载你的插件中的类
1. 你可以在插件中使用国际化翻译，只需要在插件文件夹中的i18n中的dictionary.py文件中按标准格式添加翻译即可
1. 你可以使用声明式的方式定义RNA属性，只需要根据__init__.py中的注释示例添加你的RNA属性即可，框架会自动注册和卸载你的RNA属性
1. 你可以使用common/types/framework.py中的ExpandableUi类来方便的扩展Blender原生的菜单，面板，饼菜单，标题栏等UI组件,
   只需继承该类并实现draw方法，你可以通过target_id来指定需要扩展的原生UI组件的ID,
   通过expand_mode来指定向前还是向后扩展。

## 框架在以下方面可进一步完善，欢迎贡献意见和代码

1. 框架的更新：如果你已经在项目中使用了这个框架进行开发，当你需要迁移到更新的框架版本时，你需要手动替换框架代码文件来获取新的功能，
   我们希望探索一些更友好的方式来帮助更新框架代码，欢迎提供意见。但总的来说，我们希望框架保持轻量，不会在结构上有太大的变化。
   可以预计未来的大部分更新都是在增加新的功能，而不是对框架结构进行大的调整。除非你在本地对框架代码有所改动，未来的更新你只需要将新的文件替换旧的文件即可。
1. 断点调试：目前框架并不支持IDE内的断点调试，实现这个功能需要对框架代码进行一些修改，这也许会增加框架的使用难度，我们力求寻找尽量轻量级的解决方案。但总的来说，
   断点调试对应开发插件并不是必须的，大部分的插件功能并没有复杂到需要断点调试，打印日志也可以达到大部分的调试的目的。对于这个框架，如果我们力求寻找一个简单的方案来支持断点调试，但这不是必须的。


相关文档
https://docs.blender.org/api/4.1/info_quickstart.html