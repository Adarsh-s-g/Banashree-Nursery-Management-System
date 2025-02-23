from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login',views.loginUser,name='login'),
    path('register',views.regsiter,name='registere'),
    path('header', views.header, name="header"),
    path('sidebar', views.sidebar, name="sidebar"),
    path('system_settings', views.system_settings, name="system_settings"),
    path('footer', views.footer, name="footer"),
    path('add_pure_item', views.add_pure_item, name="add_pure_item"),
    path('add_pure_edit/<str:pk>/',views.add_pure_edit,name="add_pure_edit"),
    path('add_pure_delete/<str:id>/',views.add_pure_delete,name="add_pure_delete"),
    path('purchage_list_delete/<str:id>/',views.purchage_list_delete,name="purchage_list_delete"),
    path('purchage_list', views.purchage_list, name="purchage_list"),
    path('purchage_add', views.purchage_add, name="purchage_add"),
    path('customer_list', views.customer_list, name="customer_list"),
    path('customer_delete/<str:id>/',views.customer_delete,name='customer_delete'),
    path('customer_add', views.customer_add, name="customer_add"),
    path('nursery_add', views.nursery_add, name="nursery_add"),
    path('nursery_add_mul', views.nursery_add_mul, name="nursery_add_mul"),
    path('nursery_list', views.nursery_list, name="nursery_list"),
    path('nursery_delete/<str:id>/', views.nursery_delete, name="nursery_delete"),
    path('invoice_nursery/<str:pk>/', views.invoice_nursery, name="invoice_nursery"),
    path('nursery_ledger',views.nursery_ledger,name="nursery_ledger"),
    path('party_invoice/<str:pk>/',views.party_invoice,name="party_invoice"),
    path('partylist_delete',views.partylist_delete,name="partydelete"),
    path('partyfinal_invoice/<str:pk>/',views.partyfinal_invoice,name="partyfinal_invoice"),
    path('pb_customers',views.pb_customers,name="pb_customers"),
    path('pb_customer_add',views.pb_customer_add,name="pb_customer_add"),
    path('pb_customer_delete/<str:id>/',views.pbcustomer_delete,name="pb_customer_delete"),
    path('pb_ledger',views.pb_ledger,name="pb_ledger"),
    path('pb_sugarcane',views.pb_sugarcane,name="pb_sugarcane"),
    path('pb_sugarcane_delete/<str:id>/',views.pb_sugarcane_delete,name="pb_sugarcane_delete"),
    path('pb_sugarcane_add',views.pb_sugarcane_add,name="pb_sugarcane_add"),
    path('pb_invoice/<str:pk>/',views.pb_invoice,name="pb_invoice"),
    path('pb_invoice2/<str:pk>/',views.pb_invoice2,name="pb_invoice2"),
    path('sb_customer',views.sb_customer,name="sb_customer"),
    path('sb_customer_delete<str:id>',views.sb_customer_delete,name="sb_customer_delete"),
    path('sb_customer_add',views.sb_customer_add,name="sb_customer_add"),
    path('sb_sugar',views.sb_sugar,name="sb_sugar"),
    path('sb_sugar_add',views.sb_sugar_add,name="sb_sugar_add"),
    path('sb_sugarcane_delete/<str:id>/',views.sb_sugarcane_delete,name="sb_sugarcane_delete"),
    path('sugar_invoice<str:pk>',views.sugar_invoice,name="sugar_invoice"),
    path('sb_ledger',views.sb_ledger,name="sb_ledger"),
    path('labour',views.labour,name="labour"),
    path('labour_customer_delete<str:id>',views.labour_customer_delete,name="labour_customer_delete"),
    path('labour_add',views.labour_add,name="labour_add"),
    path('view_labour',views.view_labour,name="view_labour"),
    path('view_labour_delete<str:id>',views.view_labour_delete,name="view_labour_delete"),
    path('sc_labour_add',views.sc_labour_add,name="sc_labour_add"),
    path('view_ledger',views.view_ledger,name="view_ledger"),
    path('in_cust',views.in_cust,name="in_cust"),
    path('in_cust_add',views.in_cust_add,name="in_cust_add"),
    path('in_customer_delete/<str:id>/',views.in_cust_delete,name="in_customer_delete"),
    path('in_list',views.in_list,name="in_list"),
    path('in_list_add',views.in_list_add,name="in_list_add"),
    path('in_list_delete/<str:id>/',views.in_list_delete,name="in_list_delete"),
    

      path('ledger_invoice/<str:farmer_name>/',views.ledger_invoice,name="ledger_invoice"),








]