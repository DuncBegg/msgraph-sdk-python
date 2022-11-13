from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from ..models import solutions_root
from ..models.o_data_errors import o_data_error
from .booking_businesses import booking_businesses_request_builder
from .booking_businesses.item import booking_business_item_request_builder
from .booking_currencies import booking_currencies_request_builder
from .booking_currencies.item import booking_currency_item_request_builder

class SolutionsRequestBuilder():
    """
    Provides operations to manage the solutionsRoot singleton.
    """
    def booking_businesses(self) -> booking_businesses_request_builder.BookingBusinessesRequestBuilder:
        """
        Provides operations to manage the bookingBusinesses property of the microsoft.graph.solutionsRoot entity.
        """
        return booking_businesses_request_builder.BookingBusinessesRequestBuilder(self.request_adapter, self.path_parameters)

    def booking_currencies(self) -> booking_currencies_request_builder.BookingCurrenciesRequestBuilder:
        """
        Provides operations to manage the bookingCurrencies property of the microsoft.graph.solutionsRoot entity.
        """
        return booking_currencies_request_builder.BookingCurrenciesRequestBuilder(self.request_adapter, self.path_parameters)

    def booking_businesses_by_id(self,id: str) -> booking_business_item_request_builder.BookingBusinessItemRequestBuilder:
        """
        Provides operations to manage the bookingBusinesses property of the microsoft.graph.solutionsRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: booking_business_item_request_builder.BookingBusinessItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingBusiness%2Did"] = id
        return booking_business_item_request_builder.BookingBusinessItemRequestBuilder(self.request_adapter, url_tpl_params)

    def booking_currencies_by_id(self,id: str) -> booking_currency_item_request_builder.BookingCurrencyItemRequestBuilder:
        """
        Provides operations to manage the bookingCurrencies property of the microsoft.graph.solutionsRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: booking_currency_item_request_builder.BookingCurrencyItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingCurrency%2Did"] = id
        return booking_currency_item_request_builder.BookingCurrencyItemRequestBuilder(self.request_adapter, url_tpl_params)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SolutionsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise Exception("path_parameters cannot be undefined")
        if not request_adapter:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/solutions{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_get_request_information(self,request_configuration: Optional[SolutionsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get solutions
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info

    def create_patch_request_information(self,body: Optional[solutions_root.SolutionsRoot] = None, request_configuration: Optional[SolutionsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update solutions
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    async def get(self,request_configuration: Optional[SolutionsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[solutions_root.SolutionsRoot]:
        """
        Get solutions
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[solutions_root.SolutionsRoot]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, solutions_root.SolutionsRoot, response_handler, error_mapping)

    async def patch(self,body: Optional[solutions_root.SolutionsRoot] = None, request_configuration: Optional[SolutionsRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[solutions_root.SolutionsRoot]:
        """
        Update solutions
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[solutions_root.SolutionsRoot]
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, solutions_root.SolutionsRoot, response_handler, error_mapping)

    @dataclass
    class SolutionsRequestBuilderGetQueryParameters():
        """
        Get solutions
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name

    
    @dataclass
    class SolutionsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SolutionsRequestBuilder.SolutionsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SolutionsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

