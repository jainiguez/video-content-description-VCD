"""
VCD (Video Content Description) library v5.0.1

Project website: http://vcd.vicomtech.org

Copyright (C) 2021, Vicomtech (http://www.vicomtech.es/),
(Spain) all rights reserved.

VCD is a Python library to create and manage VCD content version 5.0.1.
VCD is distributed under MIT License. See LICENSE.

"""

######################################
# Fully manually writing the schema
######################################
from builtins import type

openlabel_schema_version = "1.0.0"
openlabel_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "openlabel": {"$ref": "#/definitions/openlabel"}
    },
    "definitions": {
        "action": {
            "additionalProperties": False,
            "description": "An action is a type of element intended to describe temporal situations with semantic load as a certain activity happening in real life, such as crossing-zebra-cross, standing-still, playing-guitar. As such, actions are defined by their type, the frame intervals in which the action happens, and any additional action data, for example, numbers, booleans, text as attributes of the actions.",
            "properties": {
                "action_data": {
                    "$ref": "#/definitions/action_data"
                },
                "action_data_pointers": {
                    "$ref": "#/definitions/element_data_pointers"
                },
                "frame_intervals": {
                    "description": "The array of frame intervals where this action exists or is defined.",
                    "items": {
                        "$ref": "#/definitions/frame_interval"
                    },
                    "type": "array"
                },
                "name": {
                    "description": "Name of the action. It is a friendly name and not used for indexing.",
                    "type": "string"
                },
                "ontology_uid": {
                    "description": "This is the UID of the ontology where the type of this action is defined.",
                    "type": "string"
                },
                "resource_uid": {
                    "$ref": "#/definitions/resource_uid"
                },
                "type": {
                    "description": "The type of an action defines the class the action corresponds to.",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "type"
            ],
            "type": "object"
        },
        "action_data": {
            "additionalProperties": False,
            "description": "Additional data to describe attributes of the action.",
            "properties": {
                "boolean": {
                    "description": "List of \"boolean\" that describe this action.",
                    "items": {
                        "$ref": "#/definitions/boolean"
                    },
                    "type": "array"
                },
                "num": {
                    "description": "List of \"num\" that describe this action.",
                    "items": {
                        "$ref": "#/definitions/num"
                    },
                    "type": "array"
                },
                "text": {
                    "description": "List of \"text\" that describe this action.",
                    "items": {
                        "$ref": "#/definitions/text"
                    },
                    "type": "array"
                },
                "vec": {
                    "description": "List of \"vec\" that describe this action.",
                    "items": {
                        "$ref": "#/definitions/vec"
                    },
                    "type": "array"
                }
            },
            "type": "object"
        },
        "area_reference": {
            "additionalProperties": True,
            "description": "An area reference is a JSON object which defines the area of a set of 3D line segments by means of defining the indexes of all lines which outline the area. Note that coplanar 3D lines are assumed.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "reference_type": {
                    "description": "This is the type of the reference as a string with the name of the element data (e.g. line_reference)",
                    "type": "string"
                },
                "val": {
                    "description": "The array of indexes of the references of type reference_type.",
                    "items": {
                        "type": "number"
                    },
                    "type": "array"
                }
            },
            "type": "object"
        },
        "attributes": {
            "additionalProperties": False,
            "description": "Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes.",
            "properties": {
                "boolean": {
                    "items": {
                        "$ref": "#/definitions/boolean"
                    },
                    "type": "array"
                },
                "num": {
                    "items": {
                        "$ref": "#/definitions/num"
                    },
                    "type": "array"
                },
                "text": {
                    "items": {
                        "$ref": "#/definitions/text"
                    },
                    "type": "array"
                },
                "vec": {
                    "items": {
                        "$ref": "#/definitions/vec"
                    },
                    "type": "array"
                }
            },
            "type": "object"
        },
        "bbox": {
            "additionalProperties": True,
            "description": "A 2D bounding box is defined as a 4-dimensional vector [x, y, w, h], where [x, y] is the center of the bounding box and [w, h] represent the width (horizontal, x-coordinate dimension) and height (vertical, y-coordinate dimension), respectively.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "The array of 4 values that define the [x, y, w, h] values of the bbox.",
                    "items": {
                        "type": "number"
                    },
                    "maxItems": 4,
                    "minItems": 4,
                    "type": "array"
                }
            },
            "required": [
                "name",
                "val"
            ],
            "type": "object"
        },
        "binary": {
            "additionalProperties": True,
            "description": "A binary payload.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "data_type": {
                    "description": "This is a string that declares the type of the values of the binary object.",
                    "type": "string"
                },
                "encoding": {
                    "description": "This is a string that declares the encoding type of the bytes for this binary payload, for example, \"base64\".",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "A string with the encoded bytes of this binary payload.",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "val",
                "encoding",
                "data_type"
            ],
            "type": "object"
        },
        "boolean": {
            "additionalProperties": True,
            "description": "A boolean.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "type": {
                    "description": "This attribute specifies how the boolean shall be considered. In this schema the only possible option is as a value.",
                    "enum": [
                        "value"
                    ],
                    "type": "string"
                },
                "val": {
                    "description": "The boolean value.",
                    "type": "boolean"
                }
            },
            "required": [
                "val"
            ],
            "type": "object"
        },
        "context": {
            "additionalProperties": False,
            "description": "A context is a type of element which defines any nonspatial or temporal annotation. Contexts can be used to add richness to the contextual information of a scene, including location, weather, application-related information.",
            "properties": {
                "context_data": {
                    "$ref": "#/definitions/context_data"
                },
                "context_data_pointers": {
                    "$ref": "#/definitions/element_data_pointers"
                },
                "frame_intervals": {
                    "description": "The array of frame intervals where this context exists or is defined.",
                    "items": {
                        "$ref": "#/definitions/frame_interval"
                    },
                    "type": "array"
                },
                "name": {
                    "description": "Name of the context. It is a friendly name and not used for indexing.",
                    "type": "string"
                },
                "ontology_uid": {
                    "description": "This is the UID of the ontology where the type of this context is defined.",
                    "type": "string"
                },
                "resource_uid": {
                    "$ref": "#/definitions/resource_uid"
                },
                "type": {
                    "description": "The type of a context defines the class the context corresponds to.",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "type"
            ],
            "type": "object"
        },
        "context_data": {
            "additionalProperties": False,
            "description": "Additional data to describe attributes of the context.",
            "properties": {
                "boolean": {
                    "description": "List of \"boolean\" that describe this context.",
                    "items": {
                        "$ref": "#/definitions/boolean"
                    },
                    "type": "array"
                },
                "num": {
                    "description": "List of \"num\" that describe this context.",
                    "items": {
                        "$ref": "#/definitions/num"
                    },
                    "type": "array"
                },
                "text": {
                    "description": "List of \"text\" that describe this context.",
                    "items": {
                        "$ref": "#/definitions/text"
                    },
                    "type": "array"
                },
                "vec": {
                    "description": "List of \"vec\" that describe this context.",
                    "items": {
                        "$ref": "#/definitions/vec"
                    },
                    "type": "array"
                }
            },
            "type": "object"
        },
        "coordinate_system": {
            "additionalProperties": True,
            "description": "A coordinate system is a 3D reference frame. Spatial information on objects and their properties can be defined with respect to coordinate systems.",
            "properties": {
                "children": {
                    "description": "List of children of this coordinate system.",
                    "items": {
                        "description": "This is the string UID of this child coordinate system.",
                        "type": "string"
                    },
                    "type": "array"
                },
                "parent": {
                    "description": "This is the string UID of the parent coordinate system this coordinate system is referring to.",
                    "type": "string"
                },
                "pose_wrt_parent": {
                    "$ref": "#/definitions/transform_data"
                },
                "type": {
                    "description": "This is a string that describes the type of the coordinate system, for example, \"local\", \"geo\").",
                    "type": "string"
                }
            },
            "required": [
                "type",
                "parent"
            ]
        },
        "coordinate_systems": {
            "additionalProperties": False,
            "description": "This is a JSON object which contains OpenLABEL coordinate systems. Coordinate system keys can be any string, for example, a friendly coordinate system name.",
            "patternProperties": {
                "^": {
                    "$ref": "#/definitions/coordinate_system"
                }
            },
            "type": "object"
        },
        "cuboid": {
            "additionalProperties": True,
            "description": "A cuboid or 3D bounding box. It is defined by the position of its center, the rotation in 3D, and its dimensions.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "List of values encoding the position, rotation and dimensions. Two options are supported, using 9 or 10 values. If 9 values are used, the format is (x, y, z, rx, ry, rz, sx, sy, sz), where (x, y, z) encodes the position, (rx, ry, rz) encodes the Euler angles that encode the rotation, and (sx, sy, sz) are the dimensions of the cuboid in its object coordinate system. If 10 values are used, then the format is (x, y, z, qx, qy, qz, qw, sx, sy, sz) with the only difference of the rotation values which are the 4 values of a quaternion.",
                    "oneOf": [
                        {
                            "items": {
                                "type": "number"
                            },
                            "maxItems": 10,
                            "minItems": 9,
                            "type": "array"
                        },
                        {
                            "type": "null"
                        }
                    ]
                }
            },
            "required": [
                "name",
                "val"
            ],
            "type": "object"
        },
        "element_data_pointer": {
            "description": "This item contains pointers to element data of elements, indexed by \"name\", and containing information about the element data type, for example, bounding box, cuboid, and the frame intervals in which this element_data exists within an element. That means, these pointers can be used to explore element data dynamic information within the JSON content.",
            "properties": {
                "attribute_pointers": {
                    "description": "This is a JSON object which contains pointers to the attributes of the element data pointed by this pointer. The attributes pointer keys shall be the \"name\" of the attribute of the element data this pointer points to.",
                    "patternProperties": {
                        "^": {
                            "description": "The attribute pointer values are strings which define the type of the attribute.",
                            "enum": [
                                "num",
                                "text",
                                "boolean",
                                "vec"
                            ],
                            "type": "string"
                        }
                    },
                    "type": "object"
                },
                "frame_intervals": {
                    "description": "List of frame intervals of the element data pointed by this pointer.",
                    "items": {
                        "$ref": "#/definitions/frame_interval"
                    },
                    "type": "array"
                },
                "type": {
                    "description": "Type of the element data pointed by this pointer.",
                    "enum": [
                        "bbox",
                        "rbbox",
                        "num",
                        "text",
                        "boolean",
                        "poly2d",
                        "poly3d",
                        "cuboid",
                        "image",
                        "mat",
                        "binary",
                        "point2d",
                        "point3d",
                        "vec",
                        "line_reference",
                        "area_reference",
                        "mesh"
                    ],
                    "type": "string"
                }
            },
            "required": [
                "frame_intervals"
            ],
            "type": "object"
        },
        "element_data_pointers": {
            "additionalProperties": False,
            "description": "This is a JSON object which contains OpenLABEL element data pointers. Element data pointer keys shall be the \"name\" of the element data this pointer points to.",
            "patternProperties": {
                "^": {
                    "$ref": "#/definitions/element_data_pointer"
                }
            },
            "type": "object"
        },
        "event": {
            "additionalProperties": False,
            "description": "An event is an instantaneous situation that happens without a temporal interval. Events complement actions providing a mechanism to specify triggers or to connect actions and objects with causality relations.",
            "properties": {
                "event_data": {
                    "$ref": "#/definitions/event_data"
                },
                "event_data_pointers": {
                    "$ref": "#/definitions/element_data_pointers"
                },
                "frame_intervals": {
                    "description": "The array of frame intervals where this event exists or is defined. Note that events are thought to be instantaneous. That means, they are defined for a single frame interval where the starting and ending frames are the same.",
                    "items": {
                        "$ref": "#/definitions/frame_interval"
                    },
                    "type": "array"
                },
                "name": {
                    "description": "Name of the event. It is a friendly name and not used for indexing.",
                    "type": "string"
                },
                "ontology_uid": {
                    "description": "This is the UID of the ontology where the type of this event is defined.",
                    "type": "string"
                },
                "resource_uid": {
                    "$ref": "#/definitions/resource_uid"
                },
                "type": {
                    "description": "The type of an event defines the class the event corresponds to.",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "type"
            ],
            "type": "object"
        },
        "event_data": {
            "additionalProperties": False,
            "description": "Additional data to describe attributes of the event.",
            "properties": {
                "boolean": {
                    "description": "List of \"boolean\" that describe this event.",
                    "items": {
                        "$ref": "#/definitions/boolean"
                    },
                    "type": "array"
                },
                "num": {
                    "description": "List of \"num\" that describe this event.",
                    "items": {
                        "$ref": "#/definitions/num"
                    },
                    "type": "array"
                },
                "text": {
                    "description": "List of \"text\" that describe this event.",
                    "items": {
                        "$ref": "#/definitions/text"
                    },
                    "type": "array"
                },
                "vec": {
                    "description": "List of \"vec\" that describe this event.",
                    "items": {
                        "$ref": "#/definitions/vec"
                    },
                    "type": "array"
                }
            },
            "type": "object"
        },
        "frame": {
            "additionalProperties": False,
            "description": "A frame is a container of dynamic, timewise, information.",
            "properties": {
                "actions": {
                    "additionalProperties": False,
                    "description": "This is a JSON object that contains dynamic information on OpenLABEL actions. Action keys are strings containing numerical UIDs or 32 bytes UUIDs. Action values may contain an \"action_data\" JSON object.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "additionalProperties": False,
                            "properties": {
                                "action_data": {
                                    "$ref": "#/definitions/action_data"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "type": "object"
                },
                "contexts": {
                    "additionalProperties": False,
                    "description": "This is a JSON object that contains dynamic information on OpenLABEL contexts. Context keys are strings containing numerical UIDs or 32 bytes UUIDs. Context values may contain a \"context_data\" JSON object.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "additionalProperties": False,
                            "properties": {
                                "context_data": {
                                    "$ref": "#/definitions/context_data"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "type": "object"
                },
                "events": {
                    "additionalProperties": False,
                    "description": "This is a JSON object that contains dynamic information on OpenLABEL events. Event keys are strings containing numerical UIDs or 32 bytes UUIDs. Event values may contain an \"event_data\" JSON object.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "additionalProperties": False,
                            "properties": {
                                "event_data": {
                                    "$ref": "#/definitions/event_data"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "type": "object"
                },
                "frame_properties": {
                    "additionalProperties": True,
                    "description": "This is a JSON object which contains information about this frame.",
                    "properties": {
                        "streams": {
                            "additionalProperties": False,
                            "description": "Streams is a JSON object which contains OpenLABEL streams with specific information for this frame. Stream keys can be any string, for example, a friendly stream name.",
                            "patternProperties": {
                                "^": {
                                    "$ref": "#/definitions/stream"
                                }
                            },
                            "type": "object"
                        },
                        "timestamp": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "number"
                                }
                            ],
                            "description": "The timestamp indicates a time instant as a string or numerical value to describe this frame."
                        },
                        "transforms": {
                            "additionalProperties": False,
                            "description": "Transforms is a JSON object which contains OpenLABEL transforms specific for this frame. Transform keys can be any string, for example, a friendly name of a transform.",
                            "patternProperties": {
                                "^": {
                                    "$ref": "#/definitions/transform"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "type": "object"
                },
                "objects": {
                    "additionalProperties": False,
                    "description": "This is a JSON object that contains dynamic information on OpenLABEL objects. Object keys are strings containing numerical UIDs or 32 bytes UUIDs. Object values may contain an \"object_data\" JSON object.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "additionalProperties": False,
                            "properties": {
                                "object_data": {
                                    "$ref": "#/definitions/object_data"
                                }
                            },
                            "type": "object"
                        }
                    },
                    "type": "object"
                },
                "relations": {
                    "additionalProperties": False,
                    "description": "This is a JSON object that contains dynamic information of OpenLABEL relations. Relation keys are strings containing numerical UIDs or 32 bytes UUIDs. Relation values are empty. The presence of a key-value relation pair indicates the specified relation exists in this frame.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {}
                    },
                    "type": "object"
                }
            },
            "type": "object"
        },
        "frame_interval": {
            "additionalProperties": False,
            "description": "A frame interval defines a starting and ending frame number as a closed interval. That means the interval includes the limit frame numbers.",
            "properties": {
                "frame_end": {
                    "description": "Ending frame number of the interval.",
                    "type": "integer"
                },
                "frame_start": {
                    "description": "Initial frame number of the interval.",
                    "type": "integer"
                }
            },
            "type": "object"
        },
        "image": {
            "additionalProperties": True,
            "description": "An image.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "encoding": {
                    "description": "This is a string that declares the encoding type of the bytes for this image, for example, \"base64\".",
                    "type": "string"
                },
                "mime_type": {
                    "description": "This is a string that declares the MIME (multipurpose internet mail extensions) of the image, for example, \"image/gif\".",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "A string with the encoded bytes of this image.",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "val",
                "mime_type",
                "encoding"
            ],
            "type": "object"
        },
        "line_reference": {
            "additionalProperties": True,
            "description": "A line reference is a JSON object which defines a 3D line segment by means of defining the indexes of its two extreme points.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "reference_type": {
                    "description": "This is the type of the reference as a string with the name of the element data (e.g. point3d)",
                    "type": "string"
                },
                "val": {
                    "description": "The array of indexes of the references of type reference_type.",
                    "items": {
                        "type": "number"
                    },
                    "maxItems": 2,
                    "minItems": 2,
                    "type": "array"
                }
            },
            "type": "object"
        },
        "mat": {
            "additionalProperties": True,
            "description": "A matrix.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "channels": {
                    "description": "Number of channels of the matrix.",
                    "type": "number"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "data_type": {
                    "description": "This is a string that declares the type of the numerical values of the matrix, for example, \"float\".",
                    "type": "string"
                },
                "height": {
                    "description": "Height of the matrix. Expressed in number of rows.",
                    "type": "number"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "Flattened list of values of the matrix.",
                    "items": {
                        "type": "number"
                    },
                    "type": "array"
                },
                "width": {
                    "description": "Width of the matrix. Expressed in number of columns.",
                    "type": "number"
                }
            },
            "required": [
                "name",
                "val",
                "channels",
                "width",
                "height",
                "data_type"
            ],
            "type": "object"
        },
        "mesh": {
            "additionalProperties": True,
            "description": "A mesh encodes a point-line-area structure. It is intended to represent flat 3D meshes, such as several connected parking lots, where points, lines and areas composing the mesh are interrelated and can have their own properties.",
            "properties": {
                "area_reference": {
                    "additionalProperties": False,
                    "description": "This is the JSON object for the areas defined for this mesh. Area keys are strings containing numerical UIDs.",
                    "patternProperties": {
                        "^[0-9]+$": {
                            "$ref": "#/definitions/area_reference"
                        }
                    },
                    "type": "object"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "line_reference": {
                    "additionalProperties": False,
                    "description": "This is the JSON object for the 3D lines defined for this mesh. Line reference keys are strings containing numerical UIDs.",
                    "patternProperties": {
                        "^[0-9]+$": {
                            "$ref": "#/definitions/line_reference"
                        }
                    },
                    "type": "object"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "point3d": {
                    "additionalProperties": False,
                    "description": "This is the JSON object for the 3D points defined for this mesh. Point3d keys are strings containing numerical UIDs.",
                    "patternProperties": {
                        "^[0-9]+$": {
                            "$ref": "#/definitions/point3d"
                        }
                    },
                    "type": "object"
                }
            },
            "type": "object"
        },
        "metadata": {
            "additionalProperties": True,
            "description": "This JSON object contains information, that is, metadata, about the annotation file itself.",
            "properties": {
                "annotator": {
                    "description": "Name or description of the annotator that created the annotations.",
                    "type": "string"
                },
                "comment": {
                    "description": "Additional information or description about the annotation content.",
                    "type": "string"
                },
                "file_version": {
                    "description": "Version number of the OpenLABEL annotation content.",
                    "type": "string"
                },
                "name": {
                    "description": "Name of the OpenLABEL annotation content.",
                    "type": "string"
                },
                "schema_version": {
                    "description": "Version number of the OpenLABEL schema this annotation JSON object follows.",
                    "enum": [
                        "1.0.0"
                    ],
                    "type": "string"
                },
                "tagged_file": {
                    "description": "File name or URI of the data file being tagged.",
                    "type": "string"
                }
            },
            "required": [
                "schema_version"
            ],
            "type": "object"
        },
        "num": {
            "additionalProperties": True,
            "description": "A number.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "type": {
                    "description": "This attribute specifies whether the number shall be considered as a value, a minimum, or a maximum in its context.",
                    "enum": [
                        "value",
                        "min",
                        "max"
                    ],
                    "type": "string"
                },
                "val": {
                    "description": "The numerical value of the number.",
                    "type": "number"
                }
            },
            "required": [
                "val"
            ],
            "type": "object"
        },
        "object": {
            "additionalProperties": False,
            "description": "An object is the main type of annotation element. Object is designed to represent spatiotemporal entities, such as physical objects in the real world. Objects shall have a name and type. Objects may have static and dynamic data. Objects are the only type of elements that may have geometric data, such as bounding boxes, cuboids, polylines, images, etc.",
            "properties": {
                "coordinate_system": {
                    "description": "This is the string key of the coordinate system this object is referenced with respect to.",
                    "type": "string"
                },
                "frame_intervals": {
                    "description": "The array of frame intervals where this object exists or is defined.",
                    "items": {
                        "$ref": "#/definitions/frame_interval"
                    },
                    "type": "array"
                },
                "name": {
                    "description": "Name of the object. It is a friendly name and not used for indexing.",
                    "type": "string"
                },
                "object_data": {
                    "$ref": "#/definitions/object_data"
                },
                "object_data_pointers": {
                    "$ref": "#/definitions/element_data_pointers"
                },
                "ontology_uid": {
                    "description": "This is the UID of the ontology where the type of this object is defined.",
                    "type": "string"
                },
                "resource_uid": {
                    "$ref": "#/definitions/resource_uid"
                },
                "type": {
                    "description": "The type of an object defines the class the object corresponds to.",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "type"
            ],
            "type": "object"
        },
        "object_data": {
            "additionalProperties": False,
            "description": "Additional data to describe attributes of the object.",
            "properties": {
                "area_reference": {
                    "description": "List of \"area_reference\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/area_reference"
                    },
                    "type": "array"
                },
                "bbox": {
                    "description": "List of \"bbox\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/bbox"
                    },
                    "type": "array"
                },
                "binary": {
                    "description": "List of \"binary\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/binary"
                    },
                    "type": "array"
                },
                "boolean": {
                    "description": "List of \"boolean\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/boolean"
                    },
                    "type": "array"
                },
                "cuboid": {
                    "description": "List of \"cuboid\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/cuboid"
                    },
                    "type": "array"
                },
                "image": {
                    "description": "List of \"image\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/image"
                    },
                    "type": "array"
                },
                "line_reference": {
                    "description": "List of \"line_reference\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/line_reference"
                    },
                    "type": "array"
                },
                "mat": {
                    "description": "List of \"mat\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/mat"
                    },
                    "type": "array"
                },
                "mesh": {
                    "description": "List of \"mesh\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/mesh"
                    },
                    "type": "array"
                },
                "num": {
                    "description": "List of \"num\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/num"
                    },
                    "type": "array"
                },
                "point2d": {
                    "description": "List of \"point2d\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/point2d"
                    },
                    "type": "array"
                },
                "point3d": {
                    "description": "List of \"point3d\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/point3d"
                    },
                    "type": "array"
                },
                "poly2d": {
                    "description": "List of \"poly2d\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/poly2d"
                    },
                    "type": "array"
                },
                "poly3d": {
                    "description": "List of \"poly3d\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/poly3d"
                    },
                    "type": "array"
                },
                "rbbox": {
                    "description": "List of \"rbbox\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/rbbox"
                    },
                    "type": "array"
                },
                "text": {
                    "description": "List of \"text\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/text"
                    },
                    "type": "array"
                },
                "vec": {
                    "description": "List of \"vec\" that describe this object.",
                    "items": {
                        "$ref": "#/definitions/vec"
                    },
                    "type": "array"
                }
            },
            "type": "object"
        },
        "ontologies": {
            "additionalProperties": False,
            "description": "This is the JSON object of OpenLABEL ontologies. Ontology keys are strings containing numerical UIDs or 32 bytes UUIDs. Ontology values may be strings, for example, encoding a URI. JSON objects containing a URI string and optional lists of included and excluded terms.",
            "patternProperties": {
                "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                    "oneOf": [
                        {
                            "type": "string"
                        },
                        {
                            "additionalProperties": True,
                            "dependencies": {
                                "boundary_list": {
                                    "required": [
                                        "boundary_mode"
                                    ]
                                }
                            },
                            "properties": {
                                "boundary_list": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "type": "array"
                                },
                                "boundary_mode": {
                                    "enum": [
                                        "include",
                                        "exclude"
                                    ],
                                    "type": "string"
                                },
                                "uri": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "uri"
                            ],
                            "type": "object"
                        }
                    ]
                }
            },
            "type": "object"
        },
        "openlabel": {
            "additionalProperties": False,
            "description": "The OpenLABEL root JSON object, which contains all other JSON objects.",
            "properties": {
                "actions": {
                    "additionalProperties": False,
                    "description": "This is the JSON object of OpenLABEL actions. Action keys are strings containing numerical UIDs or 32 bytes UUIDs.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "$ref": "#/definitions/action"
                        }
                    },
                    "type": "object"
                },
                "contexts": {
                    "additionalProperties": False,
                    "description": "This is the JSON object of OpenLABEL contexts. Context keys are strings containing numerical UIDs or 32 bytes UUIDs.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "$ref": "#/definitions/context"
                        }
                    },
                    "type": "object"
                },
                "coordinate_systems": {
                    "$ref": "#/definitions/coordinate_systems"
                },
                "events": {
                    "additionalProperties": False,
                    "description": "This is the JSON object of OpenLABEL events. Event keys are strings containing numerical UIDs or 32 bytes UUIDs.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "$ref": "#/definitions/event"
                        }
                    },
                    "type": "object"
                },
                "frame_intervals": {
                    "description": "This is an array of frame intervals.",
                    "item": {
                        "$ref": "#/definitions/frame_interval"
                    },
                    "type": "array"
                },
                "frames": {
                    "additionalProperties": False,
                    "description": "This is the JSON object of frames that contain the dynamic, timewise, annotations. Keys are strings containing numerical frame identifiers, which are denoted as master frame numbers.",
                    "patternProperties": {
                        "^[0-9]+$": {
                            "$ref": "#/definitions/frame"
                        }
                    },
                    "type": "object"
                },
                "metadata": {
                    "$ref": "#/definitions/metadata"
                },
                "objects": {
                    "additionalProperties": False,
                    "description": "This is the JSON object of OpenLABEL objects. Object keys are strings containing numerical UIDs or 32 bytes UUIDs.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "$ref": "#/definitions/object"
                        }
                    },
                    "type": "object"
                },
                "ontologies": {
                    "$ref": "#/definitions/ontologies"
                },
                "relations": {
                    "additionalProperties": False,
                    "description": "This is the JSON object of OpenLABEL relations. Relation keys are strings containing numerical UIDs or 32 bytes UUIDs.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "$ref": "#/definitions/relation"
                        }
                    },
                    "type": "object"
                },
                "resources": {
                    "$ref": "#/definitions/resources"
                },
                "streams": {
                    "$ref": "#/definitions/streams"
                },
                "tags": {
                    "additionalProperties": False,
                    "description": "This is the JSON object of tags. Tag keys are strings containing numerical UIDs or 32 bytes UUIDs.",
                    "patternProperties": {
                        "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                            "$ref": "#/definitions/tag"
                        }
                    },
                    "type": "object"
                }
            },
            "required": [
                "metadata"
            ],
            "type": "object"
        },
        "point2d": {
            "additionalProperties": True,
            "description": "A 2D point.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "id": {
                    "description": "This is an integer identifier of the point in the context of a set of points.",
                    "type": "integer"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "List of two coordinates to define the point, for example, x, y.",
                    "items": {
                        "type": "number"
                    },
                    "maxItems": 2,
                    "minItems": 2,
                    "type": "array"
                }
            },
            "required": [
                "name",
                "val"
            ],
            "type": "object"
        },
        "point3d": {
            "additionalProperties": True,
            "description": "A 3D point.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "id": {
                    "description": "This is an integer identifier of the point in the context of a set of points.",
                    "type": "integer"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "List of three coordinates to define the point, for example, x, y, z.",
                    "items": {
                        "type": "number"
                    },
                    "maxItems": 3,
                    "minItems": 3,
                    "type": "array"
                }
            },
            "required": [
                "name",
                "val"
            ],
            "type": "object"
        },
        "poly2d": {
            "additionalProperties": True,
            "description": "A 2D polyline defined as a sequence of 2D points.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "closed": {
                    "description": "A boolean that defines whether the polyline is closed or not. In case it is closed, it is assumed that the last point of the sequence is connected with the first one.",
                    "type": "boolean"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "hierarchy": {
                    "description": "Hierarchy of the 2D polyline in the context of a set of 2D polylines.",
                    "items": {
                        "type": "integer"
                    },
                    "maxItems": 4,
                    "minItems": 4,
                    "type": "array"
                },
                "mode": {
                    "description": "Mode of the polyline list of values: \"MODE_POLY2D_ABSOLUTE\" determines that the poly2d list contains the sequence of (x, y) values of all points of the polyline. \"MODE_POLY2D_RELATIVE\" specifies that only the first point of the sequence is defined with its (x, y) values, while all the rest are defined relative to it. \"MODE_POLY2D_SRF6DCC\" specifies that SRF6DCC chain code method is used. \"MODE_POLY2D_RS6FCC\" specifies that the RS6FCC method is used.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "List of numerical values of the polyline, according to its mode.",
                    "anyOf": [
                        {
                            "items": {
                                "type": "string"
                            },
                            "type": "array"
                        },
                        {
                            "items": {
                                "type": "number"
                            },
                            "type": "array"
                        }
                    ]
                }
            },
            "required": [
                "name",
                "val",
                "mode",
                "closed"
            ],
            "type": "object"
        },
        "poly3d": {
            "additionalProperties": True,
            "description": "A 3D polyline defined as a sequence of 3D points.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "closed": {
                    "type": "boolean",
                    "description": "A boolean that defines whether the polyline is closed or not. In case it is closed, it is assumed that the last point of the sequence is connected with the first one."
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "List of numerical values of the polyline, according to its mode.",
                    "items": {
                        "type": "number"
                    },
                    "type": "array"
                }
            },
            "required": [
                "name",
                "val",
                "closed"
            ],
            "type": "object"
        },
        "rbbox": {
            "additionalProperties": True,
            "description": "A 2D rotated bounding box is defined as a 5-dimensional vector [x, y, w, h, alpha], where [x, y] is the center of the bounding box and [w, h] represent the width (horizontal, x-coordinate dimension) and height (vertical, y-coordinate dimension), respectively. The angle alpha, in radians, represents the rotation of the rotated bounding box, and is defined as a right-handed rotation, that is, positive from x to y axes, and with the origin of rotation placed at the center of the bounding box (that is, [x, y]).",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "val": {
                    "description": "The array of 5 values that define the [x, y, w, h, alpha] values of the bbox.",
                    "items": {
                        "type": "number"
                    },
                    "maxItems": 5,
                    "minItems": 5,
                    "type": "array"
                }
            },
            "required": [
                "name",
                "val"
            ],
            "type": "object"
        },
        "rdf_agent": {
            "description": "An RDF agent is either an RDF semantic object or subject.",
            "properties": {
                "type": {
                    "description": "The OpenLABEL type of element.",
                    "enum": [
                        "object",
                        "action",
                        "event",
                        "context"
                    ],
                    "type": "string"
                },
                "uid": {
                    "description": "The element UID this RDF agent refers to.",
                    "type": "string"
                }
            },
            "type": "object"
        },
        "relation": {
            "additionalProperties": False,
            "description": "A relation is a type of element which connects two or more other elements, for example, objects, actions, contexts, or events. RDF triples are used to structure the connection with one or more subjects, a predicate, and one or more semantic objects.",
            "properties": {
                "frame_intervals": {
                    "description": "The array of frame intervals where this relation exists or is defined.",
                    "items": {
                        "$ref": "#/definitions/frame_interval"
                    },
                    "type": "array"
                },
                "name": {
                    "description": "Name of the relation. It is a friendly name and not used for indexing.",
                    "type": "string"
                },
                "ontology_uid": {
                    "description": "This is the UID of the ontology where the type of this relation is defined.",
                    "type": "string"
                },
                "rdf_objects": {
                    "description": "This is the list of RDF semantic objects of this relation.",
                    "items": {
                        "$ref": "#/definitions/rdf_agent"
                    },
                    "type": "array"
                },
                "rdf_subjects": {
                    "description": "This is the list of RDF semantic subjects of this relation.",
                    "items": {
                        "$ref": "#/definitions/rdf_agent"
                    },
                    "type": "array"
                },
                "resource_uid": {
                    "$ref": "#/definitions/resource_uid"
                },
                "type": {
                    "description": "The type of a relation defines the class the predicated of the relation corresponds to.",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "type",
                "rdf_objects",
                "rdf_subjects"
            ],
            "type": "object"
        },
        "resource_uid": {
            "description": "This is a JSON object that contains links to external resources. Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource_uid values are strings describing the identifier of the element in the external resource.",
            "patternProperties": {
                "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                    "type": "string"
                }
            },
            "type": "object"
        },
        "resources": {
            "additionalProperties": False,
            "description": "This is the JSON object of OpenLABEL resources. Resource keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource values are strings that describe an external resource, for example, file name, URLs, that may be used to link data of the OpenLABEL annotation content with external existing content.",
            "patternProperties": {
                "^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$": {
                    "type": "string"
                }
            },
            "type": "object"
        },
        "stream": {
            "additionalProperties": False,
            "description": "A stream describes the source of a data sequence, usually a sensor.",
            "properties": {
                "description": {
                    "description": "Description of the stream.",
                    "type": "string"
                },
                "stream_properties": {
                    "$ref": "#/definitions/stream_properties"
                },
                "type": {
                    "description": "A string encoding the type of the stream.",
                    "enum": [
                        "camera",
                        "lidar",
                        "radar",
                        "gps_imu",
                        "other"
                    ],
                    "type": "string"
                },
                "uri": {
                    "description": "A string encoding the URI, for example, a URL, or file name, for example, a video file name, the stream corresponds to.",
                    "type": "string"
                }
            },
            "type": "object"
        },
        "stream_properties": {
            "additionalProperties": True,
            "description": "Additional properties of the stream.",
            "oneOf": [
                {
                    "intrinsics_custom": {
                        "description": "This is a JSON object completely customizable for other types of camera models.",
                        "type": "object"
                    },
                    "intrinsics_fisheye": {
                        "additionalProperties": True,
                        "description": "This JSON object defines an instance of the intrinsic parameters of a fisheye camera.",
                        "properties": {
                            "center_x_px": {
								"description": "x-coordinate (horizontal) of the principal point of projection.",
                                "type": [
                                    "number",
                                    "null"
                                ]
                            },
                            "center_y_px": {
								"description": "y-coordinate (vertical) of the principal point of projection.",
                                "type": [
                                    "number",
                                    "null"
                                ]
                            },
                            "focal_length_x": {
								"description": "Horizontal focal length (x-axis) in pixels.",
                                "type": [
                                    "number",
                                    "null"
                                ]
                            },
                            "focal_length_y": {
								"description": "Vertical focal length (y-axis) in pixels.",
                                "type": [
                                    "number",
                                    "null"
                                ]
                            },
                            "height_px": {
								"description": "Height of the image frame in pixels.",
                                "type": "integer"
                            },
                            "lens_coeffs": {
                                "description": "This is the list of N values for the lens coefficients.",
                                "items": {
                                    "type": "number"
                                },
                                "maxItems": 5,
                                "minItems": 4,
                                "type": "array"
                            },
                            "width_px": {
								"description": "Width of the image frame in pixels.",
                                "type": "integer"
                            }
                        },
                        "type": "object"
                    },
                    "intrinsics_pinhole": {
                        "additionalProperties": True,
                        "description": "This JSON object defines an instance of the intrinsic parameters of a pinhole camera.",
                        "properties": {
                            "camera_matrix": {
                                "description": "This is a 3x4 camera matrix which projects 3D homogeneous points (4x1) from a camera coordinate system into the image plane (3x1). This is the usual K matrix for camera projection as in OpenCV. It is extended from 3x3 to 3x4 to enable its direct utilisation to project 4x1 homogeneous 3D points. The matrix is defined to follow the camera model: x-to-right, y-down, z-forward. The following equation applies: x_img = camera_matrix * X_ccs.",
                                "items": {
                                    "type": "number"
                                },
                                "maxItems": 12,
                                "minItems": 12,
                                "type": "array"
                            },
                            "distortion_coeffs": {
                                "description": "This is the array 1xN radial and tangential distortion coefficients.",
                                "items": {
                                    "type": "number"
                                },
                                "maxItems": 14,
                                "minItems": 5,
                                "type": "array"
                            },
                            "height_px": {
                                "type": "integer"
                            },
                            "width_px": {
                                "type": "integer"
                            }
                        },
                        "type": "object"
                    }
                }
            ],
            "sync": {
                "description": "This is the sync information for this stream.",
                "oneOf": [
                    {
                        "properties": {
                            "frame_stream": {
                                "description": "This is the internal frame number inside the stream this OpenLABEL frame corresponds to.",
                                "type": "integer"
                            },
                            "timestamp": {
                                "anyOf": [
                                    {
                                        "type": "string"
                                    },
                                    {
                                        "type": "number"
                                    }
                                ],
                                "description": "The timestamp indicates a time instant as a string or numerical value to describe this frame."
                            }
                        }
                    },
                    {
                        "properties": {
                            "frame_shift": {
                                "description": "Fixed shift or difference between the OpenLABEL master frame count and this stream's internal frame count.",
                                "type": "integer"
                            }
                        }
                    }
                ],
                "type": "object"
            },
            "type": "object"
        },
        "streams": {
            "additionalProperties": False,
            "description": "This is a JSON object which contains OpenLABEL streams. Stream keys can be any string, for example, a friendly stream name.",
            "patternProperties": {
                "^": {
                    "$ref": "#/definitions/stream"
                }
            },
            "type": "object"
        },
        "tag": {
            "additionalProperties": True,
            "description": "A tag is a special type of label that can be attached to any type of content, such as images, data containers, folders. In ASAM OpenLABEL the main purpose of a tag is to allow adding metadata to scenario descriptions.",
            "properties": {
                "ontology_uid": {
                    "description": "This is the UID of the ontology where the type of this tag is defined.",
                    "type": "string"
                },
                "resource_uid": {
                    "$ref": "#/definitions/resource_uid"
                },
                "tag_data": {
                    "$ref": "#/definitions/tag_data"
                },
                "type": {
                    "description": "The type of a tag defines the class the tag corresponds to.",
                    "type": "string"
                }
            },
            "required": [
                "type"
            ],
            "type": "object"
        },
        "tag_data": {
            "description": "Tag data can be a JSON object or a string which contains additional information about this tag.",
            "oneOf": [
                {
                    "additionalProperties": False,
                    "properties": {
                        "boolean": {
                            "description": "List of \"boolean\" that describe this tag.",
                            "items": {
                                "$ref": "#/definitions/boolean"
                            },
                            "type": "array"
                        },
                        "num": {
                            "description": "List of \"num\" that describe this tag.",
                            "items": {
                                "$ref": "#/definitions/num"
                            },
                            "type": "array"
                        },
                        "text": {
                            "description": "List of \"text\" that describe this tag.",
                            "items": {
                                "$ref": "#/definitions/text"
                            },
                            "type": "array"
                        },
                        "vec": {
                            "description": "List of \"vec\" that describe this tag.",
                            "items": {
                                "$ref": "#/definitions/vec"
                            },
                            "type": "array"
                        }
                    },
                    "type": "object"
                },
                {
                    "type": "string"
                }
            ]
        },
        "text": {
            "additionalProperties": True,
            "description": "A text.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "type": {
                    "description": "This attribute specifies how the text shall be considered. The only possible option is as a value.",
                    "enum": [
                        "value"
                    ],
                    "type": "string"
                },
                "val": {
                    "description": "The characters of the text.",
                    "type": "string"
                }
            },
            "required": [
                "val"
            ],
            "type": "object"
        },
        "transform": {
            "additionalProperties": True,
            "description": "This is a JSON object with information about this transform.",
            "properties": {
                "dst": {
                    "description": "The string UID, that is, the name, of the destination coordinate system for geometric data converted with this transform.",
                    "type": "string"
                },
                "src": {
                    "description": "The string UID, that is, the name, of the source coordinate system of geometrical data this transform converts.",
                    "type": "string"
                },
                "transform_src_to_dst": {
                    "$ref": "#/definitions/transform_data"
                }
            },
            "required": [
                "src",
                "dst",
                "transform_src_to_dst"
            ],
            "type": "object"
        },
        "transform_data": {
            "description": "JSON object containing the transform data.",
            "oneOf": [
                {
                    "additionalProperties": False,
                    "properties": {
                        "matrix4x4": {
                            "description": "Flattened list of 16 entries encoding a 4x4 homogeneous matrix to enable transform 3D column homogeneous vectors 4x1 using right-multiplication of matrices: X_dst = matrix_4x4 * X_src.",
                            "items": {
                                "type": "number"
                            },
                            "type": "array"
                        }
                    },
                    "required": [
                        "matrix4x4"
                    ],
                    "type": "object"
                },
                {
                    "additionalProperties": False,
                    "description": "A transform can be defined with a quaternion to encode the rotation of a coordinate system with respect to another, and a translation.",
                    "properties": {
                        "quaternion": {
                            "description": "List of 4 values encoding a quaternion (x, y, z, w).",
                            "items": {
                                "type": "number"
                            },
                            "maxItems": 4,
                            "minItems": 4,
                            "type": "array"
                        },
                        "translation": {
                            "description": "List of 3 values encoding the translation vector (x, y, z)",
                            "items": {
                                "type": "number"
                            },
                            "maxItems": 3,
                            "minItems": 3,
                            "type": "array"
                        }
                    },
                    "required": [
                        "quaternion",
                        "translation"
                    ],
                    "type": "object"
                },
                {
                    "additionalProperties": False,
                    "description": "A transform can be defined with a sequence of Euler angles to encode the rotation of a coordinate system with respect to another and a translation.",
                    "properties": {
                        "euler_angles": {
                            "description": "List of 3 values encoding Euler angle values.",
                            "items": {
                                "type": "number"
                            },
                            "maxItems": 3,
                            "minItems": 3,
                            "type": "array"
                        },
                        "sequence": {
                            "description": "The sequence as a string of 3 characters defining the axis of the Euler angles and their order of application, for example, \"ZYX\". The default is \"ZYX\".",
                            "type": "string"
                        },
                        "translation": {
                            "description": "List of 3 values encoding the translation vector (x, y, z)",
                            "items": {
                                "type": "number"
                            },
                            "maxItems": 3,
                            "minItems": 3,
                            "type": "array"
                        }
                    },
                    "required": [
                        "euler_angles",
                        "translation"
                    ],
                    "type": "object"
                }
            ]
        },
        "vec": {
            "additionalProperties": True,
            "description": "A vector (list) of numbers or strings.",
            "properties": {
                "attributes": {
                    "$ref": "#/definitions/attributes"
                },
                "coordinate_system": {
                    "description": "Name of the coordinate system in respect of which this object data is expressed.",
                    "type": "string"
                },
                "name": {
                    "description": "This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers.",
                    "type": "string"
                },
                "type": {
                    "description": "This attribute specifies whether the vector shall be considered as a descriptor of individual values or as a definition of a range.",
                    "enum": [
                        "values",
                        "range"
                    ],
                    "type": "string"
                },
                "val": {
                    "description": "The numerical values of the vector (list) of numbers.",
                    "items": {
                        "oneOf": [
                            {
                                "type": "number"
                            },
                            {
                                "type": "string"
                            }
                        ]
                    },
                    "type": "array"
                }
            },
            "required": [
                "val"
            ],
            "type": "object"
        }
    },
    "required": ["openlabel"],
    "additionalProperties": False
}