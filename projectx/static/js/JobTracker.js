var myApp = angular.module('myApp', []);

myApp.controller('appController', ['$scope', '$http', '$sce', function ($scope, $http, $sce) {
    var ctrl = this;
    ctrl.show_add_form = false;
    ctrl.addJob = function () {
        $http.get(window.add_form_url).then(function (response) {
            ctrl.html_data = $sce.trustAsHtml(response.data);
        });
    }
    ctrl.getJobsList = function () {
        $http.get(window.get_jobs_list_url).then(function (response) {
            ctrl.html_data = $sce.trustAsHtml(response.data);
        });
    }
}]);

myApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});