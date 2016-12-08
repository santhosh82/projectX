$(document).ready(function () {
    $('#get_jobs_list_btn').click();
});



var myApp = angular.module('myApp', ['angular-bind-html-compile']);

myApp.controller('appController', ['$scope', '$http', '$sce', '$compile', '$location', '$window',
    function ($scope, $http, $sce, $compile, $location, $window) {
    var ctrl = this;
    ctrl.show_add_form = false;

   var add_form_url = '/JobTracker/addjob/';
    var get_jobs_list_url = '/JobTracker/getjobslist/';
    var about_url = '/JobTracker/about/';
    var edit_job_url = '/JobTracker/editjob/';
    var delete_job_url = '/JobTracker/deletejob/';




    ctrl.addJob = function () {
        $http.get('/jobtracker/addjob/').then(function (response) {
            ctrl.html_data = $sce.trustAsHtml(response.data);
        });
    };
    ctrl.getJobsList = function () {
        $http.get('/jobtracker/getjobslist/').then(function (response) {
          //  temp_data = $sce.trustAsHtml(response.data);
            //ctrl.html_data = $compile(temp_data)($scope);
            ctrl.html_data = response.data;
        });
    }

    ctrl.getJobsSharedList =  function()
    {
        $http.get("/jobtracker/getsharedlist/").then(function (response) {
            ctrl.html_data = response.data;
        });
    }

    ctrl.about = function () {
        $http.get('/jobtracker/about/').then(function (response) {
            ctrl.html_data = $sce.trustAsHtml(response.data);
            // $window.location.href = "/jobtracker/index/";
            // ctrl.html_data = $sce.trustAsHtml(response.data);
        });
        // $window.location.href = "/jobtracker/about/";
    };


    ctrl.edit = function (jobId) {
      console.log("editing job id is ",jobId);
        $http.get('/jobtracker/editjob/'+jobId).then(function (response) {
            console.log("data in edit function is "+response.data);
           ctrl.html_data = response.data;
        });
    };

    ctrl.delete = function(jobId)
    {
        console.log("delete job id is ",jobId);

        $http.get('/jobtracker/deletejob/'+jobId).then(function (response) {
            ctrl.html_data = response.data

        })
    }

    ctrl.share = function(jobId)
    {
        console.log("share job id is ",jobId);
        //$location.path("/jobtracker/sharejob/"+jobId);

        $window.location.href = "/jobtracker/sharejob/"+jobId;

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
