var myApp = angular.module('myApp', []);

myApp.controller('appController', ['$scope', '$http', '$sce', function ($scope, $http, $sce) {
    var ctrl = this;
    ctrl.show_add_form = false;
    ctrl.addJob = function () {
        ctrl.show_add_form = ctrl.show_add_form ? false : true;
        $http.get(window.add_form_url).then(function (response) {
            ctrl.add_form_html_data = $sce.trustAsHtml(response.data);
        });
    }
}]);

myApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});