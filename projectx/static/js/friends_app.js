/**
 * Created by santhosh on 10/21/2016.
 */


var friendsApp = angular.module('friendsApp',['ui.bootstrap']);

friendsApp.controller('myController',['$scope', '$http', '$window',function ($scope,$http,$window) {

    var ctrl = this;

     ctrl.selected = undefined;
     ctrl.states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Dakota', 'North Carolina', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'];

    ctrl.getUsers = function(val)
    {
        return $http.get('/jobtracker/api/getusers/'+val+"/").then(function(response)
        {
           return response.data.map(function (item) {
              return item.name;
           });

        });
    }

    ctrl.addFriend = function() {
        // Need to call a view to make friends in the database
        $http.get('/jobtracker/makefriends/',{params:{"name":ctrl.selected, "type":"pending"}}).then(function (response) {

            console.log(response.data)
        });

    }


    ctrl.shareJobFriend = function(friend,id)
    {
        // Need to call a view to make a row in sharedtable


        $http.get('/jobtracker/addjobshare/',{params:{"name" : friend, "id" : id }}).then(function (response) {
            console.log("in the share job friend with id ",friend + " "+id);
            $window.location.href = "/jobtracker/index";

        });
        
        
        
    }







}]);
friendsApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});