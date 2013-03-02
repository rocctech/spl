define([
  'models/base/model'
], function(Model) {
  "use strict";

  var Supplier = Model.extend({

    urlRoot: '/api/suppliers/',

    defaults: {
      phone: '',
      email: ''
    },

    initialize: function(attributes, options) {
      Model.prototype.initialize.apply(this, arguments);
      if (options && options.loadDetails) {
        this.initDeferred();
        this.fetch();
      }
    }

  });

  return Supplier;

});
// vim:sw=2
