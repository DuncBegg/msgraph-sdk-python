from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class FreeBusyError(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value

    def __init__(self,) -> None:
        """
        Instantiates a new freeBusyError and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        self.odata_type = "#microsoft.graph.freeBusyError"
        # Describes the error.
        self._message: Optional[str] = None
        # The response code from querying for the availability of the user, distribution list, or resource.
        self._response_code: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FreeBusyError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FreeBusyError
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return FreeBusyError()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "response_code": lambda n : setattr(self, 'response_code', n.get_str_value()),
        }
        return fields

    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. Describes the error.
        Returns: Optional[str]
        """
        return self._message

    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. Describes the error.
        Args:
            value: Value to set for the message property.
        """
        self._message = value

    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type

    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value

    @property
    def response_code(self,) -> Optional[str]:
        """
        Gets the responseCode property value. The response code from querying for the availability of the user, distribution list, or resource.
        Returns: Optional[str]
        """
        return self._response_code

    @response_code.setter
    def response_code(self,value: Optional[str] = None) -> None:
        """
        Sets the responseCode property value. The response code from querying for the availability of the user, distribution list, or resource.
        Args:
            value: Value to set for the responseCode property.
        """
        self._response_code = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("responseCode", self.response_code)
        writer.write_additional_data_value(self.additional_data)


