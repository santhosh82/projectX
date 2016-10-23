$(document).ready(function () {
    $('#get_jobs_list_btn').click();
});



var myApp = angular.module('myApp', ['angular-bind-html-compile']);

myApp.controller('appController', ['$scope', '$http', '$sce', '$compile', '$location', '$window',
    function ($scope, $http, $sce, $compile, $location, $window) {
    var ctrl = this;
    ctrl.show_add_form = false;

   




    ctrl.addJob = function () {
        $http.get(window.add_form_url).then(function (response) {
            ctrl.html_data = $sce.trustAsHtml(response.data);
        });
    };
    ctrl.getJobsList = function () {
        $http.get(window.get_jobs_list_url).then(function (response) {
          //  temp_data = $sce.trustAsHtml(response.data);
            //ctrl.html_data = $compile(temp_data)($scope);
            ctrl.html_data = response.data;
        });
    }

    ctrl.getJobsSharedList =  function()
    {
        $http.get("/JobTracker/getsharedlist/").then(function (response) {
            ctrl.html_data = response.data;
        });
    }

    ctrl.about = function () {
        $http.get('/JobTracker/about/').then(function (response) {
            ctrl.html_data = $sce.trustAsHtml(response.data);
        });
    };


    ctrl.edit = function (jobId) {
      console.log("job id is ",jobId);
        $http.get(window.edit_job_url+jobId).then(function (response) {
            console.log("data in edit function is "+response.data);
           ctrl.html_data = response.data;
        });
    };

    ctrl.delete = function(jobId)
    {
        console.log("job id is ",jobId);
        $http.get(window.delete_job_url+jobId).then(function (response) {
            ctrl.html_data = response.data

        })
    }

    ctrl.share = function(jobId)
    {
        console.log("share job id is ",jobId);
        //$location.path("/JobTracker/sharejob/"+jobId);

        $window.location.href = "/JobTracker/sharejob/"+jobId;

    }





}]);

myApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


(function (angular) {
    'use strict';

    var module = angular.module('angular-bind-html-compile', []);

    module.directive('bindHtmlCompile', ['$compile', function ($compile) {
        return {
            restrict: 'A',
            link: function (scope, element, attrs) {
                scope.$watch(function () {
                    return scope.$eval(attrs.bindHtmlCompile);
                }, function (value) {
                    // In case value is a TrustedValueHolderType, sometimes it
                    // needs to be explicitly called into a string in order to
                    // get the HTML string.
                    element.html(value && value.toString());
                    // If scope is provided use it, otherwise use parent scope
                    var compileScope = scope;
                    if (attrs.bindHtmlScope) {
                        compileScope = scope.$eval(attrs.bindHtmlScope);
                    }
                    $compile(element.contents())(compileScope);
                });
            }
        };
    }]);
}(window.angular));
