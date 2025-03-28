from django.contrib import admin
from django.urls import path
from soothestore.views import *

using_nginx = True

if using_nginx:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', HomePage),
        path('serverdestination/FindProduct/', SearchPage),
        path('serverdestination/Buy/<int:product_id>/', Buy),
        path('serverdestination/FAQ/', FAQ),
        path('serverdestination/Cart/', Cart),
        path('serverdestination/VerifyCart/', CheckCart.as_view()),
        path('serverdestination/GetCompanyContact/', companyContactPoint.as_view()),
        path('serverdestination/RecordReview/<int:chair_id>/', ChairReviewCreateAPIView.as_view()),
        path('serverdestination/DeleteReview/<int:review_id>/', RemoveReview.as_view()),
        path('serverdestination/RecordInquiry/', SaveCustomerQuestion.as_view()),
        path('serverdestination/GetReview/<int:product_id>/', ProductReviewsEndpoint.as_view()),
        path('serverdestination/RecordUserReaction/<int:review_id>/', UserReactionCreateView.as_view()),
        path('serverdestination/GetProduct/<int:product_ID>/', MassageChairDetailView.as_view()),
        path('serverdestination/payment/', initiatePayment),
        path('serverdestination/initiate_checkout/', InitiateCheckoutSession),
        path('serverdestination/HomePageData/', FetchHomePage.as_view()),
        path('serverdestination/RegisterCustomer/', RegisterCustomer),
        path('serverdestination/customer_orders/', customer_orders),
        path('serverdestination/customer_orders/<str:order_number>/', order_check),
        path('serverdestination/order_details/<str:order_number>/', order_details),
        path('serverdestination/AdminDetails/', CompletedPaymentSessionsView.as_view()),
        path('serverdestination/SaveProduct/', SaveProduct.as_view()),
        path('serverdestination/GetProducts/', GetProducts.as_view()),
        path('serverdestination/UpdateProduct/<int:product_id>/', UpdateProduct.as_view()),
        path('serverdestination/GetBrands/', GetBrands.as_view()),
        path('serverdestination/UpdateBrand/<int:brand_id>/', UpdateBrand.as_view()),
        path('serverdestination/CreateBrand/', CreateBrand.as_view()),
        path('serverdestination/GetDiscounts/', GetDiscounts.as_view()),
        path('serverdestination/CreateDiscount/', CreateDiscount.as_view()),
        path('serverdestination/UpdateDiscount/<int:discount_id>/', UpdateDiscount.as_view()),
        path('serverdestination/GetOrders/', GetOrders.as_view()),
        path('serverdestination/UpdateShipping/<int:data_id>/', UpdateShippingData.as_view()),
        path('serverdestination/UpdateOrder/<int:data_id>/', UpdateOrder.as_view()),
        path('serverdestination/UpdateCompanyContactInfo/', UpdateContact.as_view()),
        path('serverdestination/GetCompanyContactInfo/', GetCompanyContactData.as_view()),
        path('serverdestination/GetOrderTrackings/', GetOrderTracking.as_view()),
        path('serverdestination/UpdateTrackingData/', UpdateTrackingData.as_view()),
        path('serverdestination/AuthenticateAdmin/', AuthenticateAdmin.as_view()),
        path('serverdestination/VerifyIfAdmin/', CheckIfAdmin.as_view()),
        path('serverdestination/GetReviews/', AllReviews.as_view()),
        path('serverdestination/GetQuestions/', GetCustomerInquiries.as_view()),
        path('serverdestination/UpdateInquiryStatus/', UpdateInquiryStatus.as_view()),
        path('serverdestination/GetAllFAQs/', GetFAQs.as_view()),
        path('serverdestination/UpdateFAQ/<int:FAQ_id>/', UpdateFAQ.as_view()),
        path('serverdestination/CreateFAQ/', CreateFAQ.as_view()),
        path('serverdestination/SwapFAQ/<int:FAQ_id>/', SwapFAQs.as_view()),
        path('serverdestination/RemoveFAQ/<int:FAQ_id>/', RemoveFAQ.as_view()),
        path('serverdestination/SwapEach/<int:FAQ_id>/<int:FAQ_at_priority>/', SwapEach.as_view()),
        path('serverdestination/reindex-product/<int:product_id>/', IndexProductView.as_view()),
        path('serverdestination/Product_Meta/<int:product_id>/', Product_Meta.as_view()),
        path('serverdestination/AdjustPrice/', PriceAdjustmentPoint.as_view()),
        path('serverdestination/SpecialEvent/', PromotionDetails.as_view()),
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', HomePage),
        path('FindProduct/', SearchPage),
        path('Buy/<int:product_id>/', Buy),
        path('FAQ/', FAQ),
        path('Cart/', Cart),
        path('VerifyCart/', CheckCart.as_view()),
        path('RecordReview/<int:chair_id>/', ChairReviewCreateAPIView.as_view()),
        path('GetReview/<int:product_id>/', ProductReviewsEndpoint.as_view()),
        path('RecordUserReaction/<int:review_id>/', UserReactionCreateView.as_view()),
        path('GetProduct/<int:product_ID>/', MassageChairDetailView.as_view()),
        path('payment/', initiatePayment),
        path('initiate_checkout/', InitiateCheckoutSession),
        path('HomePageData/', FetchHomePage.as_view()),
        path('RegisterCustomer/', RegisterCustomer),
    ]