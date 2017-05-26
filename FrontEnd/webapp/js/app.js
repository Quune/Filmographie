/**
 * Created by Quentinounet on 26/05/2017.
 */
var filmographie = angular.module('filmographie ', ['ngRoute', 'ngResource']);

filmographie.config($routeProvider, $interpolateProvider, $httpProvider, $resourceProvider),
    function () {

        $httpProvider.interceptors.push = 'httpInterceptor';
        $httpProvider.defaults.headers.common['X-CSRFToken'] = $.cookie('csrftoken');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $interpolateProvider.startSymbol =  '~{';
        $interpolateProvider.endSymbol = '}~';

        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

        $resourceProvider.defaults.stripTrailingSlashes = false;

        $routeProvider

            .otherwise({redirectTo: '/home'});


    };



