const app = angular.module("guitarApp", ['ngRoute']);

angular.module('guitarApp').config(['$routeProvider', 
        function config($routeProvider){
            $routeProvider.
            when('/home', {
                templateUrl: '/public/views/home.html'
            }).
            when('/history', {
                templateUrl: '/public/views/history.html'
            }).
            when('/plans', {
                templateUrl: '/public/views/plans.html'
            }).
            when('/teachers', {
                templateUrl: '/public/views/teachers.html'
            }).
            when('/contact', {
                templateUrl: '/public/views/contact.html'
            }).
            when('/lore', {
                templateUrl: '/public/views/lore.html'
            }).
            when('/luigi_sings', {
                templateUrl: '/public/views/luigi_sings.html'
            }).
            otherwise('/home')
        }
    ]);
