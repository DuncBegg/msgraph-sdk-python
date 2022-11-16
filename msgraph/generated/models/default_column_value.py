from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

class DefaultColumnValue(AdditionalDataHolder, Parsable):
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
        Instantiates a new defaultColumnValue and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        self.odata_type = "#microsoft.graph.defaultColumnValue"
        # The formula used to compute the default value for this column.
        self._formula: Optional[str] = None
        # The direct value to use as the default value for this column.
        self._value: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DefaultColumnValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DefaultColumnValue
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return DefaultColumnValue()

    @property
    def formula(self,) -> Optional[str]:
        """
        Gets the formula property value. The formula used to compute the default value for this column.
        Returns: Optional[str]
        """
        return self._formula

    @formula.setter
    def formula(self,value: Optional[str] = None) -> None:
        """
        Sets the formula property value. The formula used to compute the default value for this column.
        Args:
            value: Value to set for the formula property.
        """
        self._formula = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "formula": lambda n : setattr(self, 'formula', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
        }
        return fields

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

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("formula", self.formula)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)

    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. The direct value to use as the default value for this column.
        Returns: Optional[str]
        """
        return self._value

    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. The direct value to use as the default value for this column.
        Args:
            value: Value to set for the value property.
        """
        self._value = value

