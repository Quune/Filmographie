/**
 * Created by Quentinounet on 26/05/2017.
 */
angular.module('filmographie', ['ui.router'])
    .config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/home');

    $stateProvider

        .state('home', {
            url: '/home',
            templateUrl: 'webapp/home.html'
        }

        );


    });



