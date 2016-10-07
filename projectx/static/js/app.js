/**
 * Created by vikas on 10/7/16.
 */
var app = angular.module('JobApp', ['ui.router', 'restangular']);

app.config(function ($stateProvider, $urlRouteProvider, $RestangularProvider) {
    $urlRouteProvider.otherwise("/");
    $stateProvider.state('index2', {
        url: "/",
        templateUrl: "/templates/job/_job_list.html",
        controller: "JobList"
    })
        .state('new', {
            url: "/new",
            templateUrl: "templates/job/new.html",
            controller: "JobFormCtrl"
        })
});

app.controller("JobFormCtrl", ['$scope', 'Restangular', 'CbgenRestangular', '$q', function ($scope, Restangular, CbgenRestangular, $q) {
    JobFormCtrl.submitJob = function () {
        console.log("Making post request!")
        var post_update_data = create_resource($scope, CbgenRestangular);
        $q.when(post_update_data.then(
            function (object) {
                //Success
                //Write code to save to database
            },
            function (object) {
                //error
                console.log(object.data);
            }
        ))
    }
}]);

app.factory('CbgenRestangular', function (Restangular) {
    return Restangular.withConfig(function (RestangularConfigurer) {
        RestangularConfigurer.setBaseUrl('/api/v1');
    });
});

populate_scope_values = function ($scope) {
    return {companyName: $scope.companyName, appliedOn: $scope.appliedOn,
            source: $scope.source, jobId: $scope.jobId,
            jobDesc: $scope.jobDesc, statusLink: $scope.statusLink,
            result: $scope.result
    };
};

create_resource = function ($scope, CbgenRestangular) {
    var post_data = populate_scope_values($scope);
    return CbgenRestangular.all('tjob').post(post_data);
};