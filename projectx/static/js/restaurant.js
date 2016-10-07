// /**
//  * Created by vikas on 10/5/16.
//  */
// var app = angular.module('MyApp', []);
//
// app.config(function ($resourceProvider) {
//     $resourceProvider.defaults.stripTrailingSlashes = false;
// });
//
// app.config(function($interpolateProvider){
//     $interpolateProvider.startSymbol("[[");
//     $interpolateProvider.startSymbol("]]");
// });
//
// app.controller('AppController', ['$scope', function ($scope) {
//     console.log("controller initialized");
//     $scope.menus = ['one', 'two'];
//     // $http.get("menuapi/").then(function (response) {
// //     //     console.log("hello");
// //     //     console.log(response);
// //     //     //$scope.menus = response.data;
// //     //
// //     // });
//  }]);
//

var myApp = angular.module('myApp', []);

myApp.controller('appController', ['$scope', '$http', '$sce', function ($scope, $http, $sce) {
    var ctrl = this;
    ctrl.showdata = false;
    ctrl.showmenu = false;
    ctrl.getMenu = function () {
        ctrl.showdata = ctrl.showdata ? false : true;
        $http.get("getmenu/").then(function (response) {
            ctrl.htmldata = $sce.trustAsHtml(response.data);
        });
    };
    ctrl.createMenu = function () {
        ctrl.showmenu = ctrl.showmenu ? false : true;
        $http.get("createmenu/").then(function (response) {
            ctrl.menuform = $sce.trustAsHtml(response.data);
        });
    }
}]);

myApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});