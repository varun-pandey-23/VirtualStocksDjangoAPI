from django.urls import path
from . import views

urlpatterns = [
    path('stock/<str:name>', views.stock, name='stock'),
    path('stocks', views.stocks, name='stocks'),
    path('gainers', views.gainers, name='gainers'),
    path('losers', views.losers, name='losers'),
    path('', views.apiHome, name='home'),
    path('register-user', views.registerUser, name='register-user'),
    path('list-users', views.listUsers, name='list-users'),
    path('delete-user', views.deleteUser, name='delete-user'),
    path('populate-stocks/<str:op>',
         views.populateStocksTable, name='populate-stocks'),
    path('add-watchlist/<str:code>', views.addToWatchlist, name='add-watchlist'),
    path('delete-watchlist/<str:code>',
         views.deleteFromWatchlist, name='delete-watchlist'),
    path('view-watchlist', views.viewWatchlist, name='view-watchlist'),
    path('buy-stock/<str:code>/<int:quantity>',
         views.buyStock, name='buy-stock'),
    path('sell-stock/<str:code>/<int:quantity>',
         views.sellStock, name='sell-stock')
]
