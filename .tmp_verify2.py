import sys

sys.path.insert(0, 'jarviscli')
from PluginManager import PluginManager

pm = PluginManager()
pm.add_directory('jarviscli/plugins')
plugins = pm.get_plugins()
print('TOP_LEVEL', sorted(plugins.keys()))

for name, plugin in plugins.items():
    print('PLUGIN', name, type(plugin).__name__)
    try:
        doc = plugin.get_doc()
        print('DOC_OK', name, len(doc))
    except Exception as e:
        print('DOC_FAIL', name, type(e).__name__, e)
