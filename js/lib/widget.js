// Copyright (c) Alex Lewandowski
// Distributed under the terms of the Modified BSD License.

"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.URLView = exports.URLModel = void 0;
const base_1 = require("@jupyter-widgets/base");
const version_1 = require("./version");

// Import the CSS
require("../css/widget.css");
class URLModel extends base_1.DOMWidgetModel {
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()),
            { _model_name: URLModel.model_name,
            _model_module: URLModel.model_module,
            _model_module_version: URLModel.model_module_version,
            _view_name: URLModel.view_name, _view_module: URLModel.view_module,
            _view_module_version: URLModel.view_module_version, value: '' });
    }
}
exports.URLModel = URLModel;
URLModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
URLModel.model_name = 'URLModel';
URLModel.model_module = version_1.MODULE_NAME;
URLModel.model_module_version = version_1.MODULE_VERSION;
URLModel.view_name = 'URLView'; // Set to null if no view
URLModel.view_module = version_1.MODULE_NAME; // Set to null if no view
URLModel.view_module_version = version_1.MODULE_VERSION;
class URLView extends base_1.DOMWidgetView {
    render() {
        this.el.classList.add('url-widget');
        this.model.set('value', document.URL);
        this.model.save_changes();
        this.value_changed();
        this.model.on('change:value', this.value_changed, this);
    }
    value_changed() {
        this.el.textContent = this.model.get('value');
    }
}
exports.URLView = URLView;
exports.URLModel = URLModel;
