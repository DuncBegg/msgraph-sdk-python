from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class Ceiling_MathPostRequestBody(AdditionalDataHolder, Parsable):
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
        Instantiates a new ceiling_MathPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The mode property
        self._mode: Optional[json.Json] = None
        # The number property
        self._number: Optional[json.Json] = None
        # The significance property
        self._significance: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Ceiling_MathPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Ceiling_MathPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Ceiling_MathPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "mode": lambda n : setattr(self, 'mode', n.get_object_value(json.Json)),
            "number": lambda n : setattr(self, 'number', n.get_object_value(json.Json)),
            "significance": lambda n : setattr(self, 'significance', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def mode(self,) -> Optional[json.Json]:
        """
        Gets the mode property value. The mode property
        Returns: Optional[json.Json]
        """
        return self._mode
    
    @mode.setter
    def mode(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the mode property value. The mode property
        Args:
            value: Value to set for the mode property.
        """
        self._mode = value
    
    @property
    def number(self,) -> Optional[json.Json]:
        """
        Gets the number property value. The number property
        Returns: Optional[json.Json]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("mode", self.mode)
        writer.write_object_value("number", self.number)
        writer.write_object_value("significance", self.significance)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def significance(self,) -> Optional[json.Json]:
        """
        Gets the significance property value. The significance property
        Returns: Optional[json.Json]
        """
        return self._significance
    
    @significance.setter
    def significance(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the significance property value. The significance property
        Args:
            value: Value to set for the significance property.
        """
        self._significance = value
    
