// Copyright (c) Alex Lewandowski
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import { MODULE_NAME, MODULE_VERSION } from './version';

// Import the CSS
import '../css/widget.css';

export class URLModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: URLModel.model_name,
      _model_module: URLModel.model_module,
      _model_module_version: URLModel.model_module_version,
      _view_name: URLModel.view_name,
      _view_module: URLModel.view_module,
      _view_module_version: URLModel.view_module_version,
      value: '',
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    // Add any extra serializers here
  };

  static model_name = 'URLModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'URLView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class URLView extends DOMWidgetView {
  render() {
    this.el.classList.add('url-widget');
    this.model.set('value', document.URL);
    this.model.save_changes();
    this.value_changed();
    // this.model.on('change:value', this.value_changed, this);
    // this.model.save_changes();
  }

  value_changed() {
    this.el.textContent = this.model.get('value');
  }
}
