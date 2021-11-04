var plugin = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'url-widget:plugin',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'url-widget',
          version: plugin.version,
          exports: plugin
      });
  },
  autoStart: true
};

