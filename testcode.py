from jsonschema import validate, validators
import json

from jsonschema.validators import Draft6Validator, Draft7Validator, Draft3Validator, Draft4Validator

json_schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "box": {
            "type": "string"
        },
        "polygon": {
            "type": "string"
        },
        "polyline": {
            "type": "string"
        },
        "points": {
            "type": "string"
        }
    },
    "allOf": [
        {
            "required": [
                "box"
            ]
        },  # 조건 1
        {
            "required": [
                "polygon"
            ]
        }
    ]
}
# oneOf : 각 조건마다 모두 맞아야 참 ( 조건이 하나가 맞더라도 나머지 조건이 맞지 않으면, 맞는 조건 외의 다른 조건은 오류 검출 )
# anyOf : 조건 중 하나 이상 맞으면 참 ( 조건이 하나 이상 맞으면, 맞지 않는 조건의 오류 검출 X )


member = json.loads('{"polyline":"zz"}')
v = Draft3Validator(json_schema)
for error in sorted(v.iter_errors(member), key=str):
    print(error.message)
