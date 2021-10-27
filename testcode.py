from jsonschema import validate
import json

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
    "oneOf": [
        {
            "required": [
                "box"
            ]
        },  # 조건 1
        {
            "required": [
                "polygon"
            ]
        },  # 조건 2
        {
            "required": [
                "box",
                "polygon"
            ]
        }  # 조건 3

    ]
}
# oneOf : 각 조건마다 모두 맞아야 참 ( 조건이 하나가 맞더라도 나머지 조건이 맞지 않으면, 맞는 조건 외의 다른 조건은 오류 검출 )
# anyOf : 조건 중 하나 이상 맞으면 참 ( 조건이 하나 이상 맞으면, 맞지 않는 조건의 오류 검출 X )


member = json.loads('{"box":"asdf","polygon":"aaa"}')
print(member)
validate(instance=member, schema=json_schema)
