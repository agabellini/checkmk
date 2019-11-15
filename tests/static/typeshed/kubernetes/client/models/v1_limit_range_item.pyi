# Stubs for kubernetes.client.models.v1_limit_range_item (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1LimitRangeItem:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    default: Any = ...
    default_request: Any = ...
    max: Any = ...
    max_limit_request_ratio: Any = ...
    min: Any = ...
    type: Any = ...
    def __init__(self, default: Optional[Any] = ..., default_request: Optional[Any] = ..., max: Optional[Any] = ..., max_limit_request_ratio: Optional[Any] = ..., min: Optional[Any] = ..., type: Optional[Any] = ...) -> None: ...
    @property
    def default(self): ...
    @default.setter
    def default(self, default: Any) -> None: ...
    @property
    def default_request(self): ...
    @default_request.setter
    def default_request(self, default_request: Any) -> None: ...
    @property
    def max(self): ...
    @max.setter
    def max(self, max: Any) -> None: ...
    @property
    def max_limit_request_ratio(self): ...
    @max_limit_request_ratio.setter
    def max_limit_request_ratio(self, max_limit_request_ratio: Any) -> None: ...
    @property
    def min(self): ...
    @min.setter
    def min(self, min: Any) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...