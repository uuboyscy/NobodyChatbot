'''
CarouselContainerJsonDict
For items on sale
'''

tmp = """
    {

        "type": "carousel",
        "contents": [ 
            {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "contents": [
                        {
                            "type": "text",
                            "text": "ＭＥＭＢＥＲ ＣＥＮＴＲＥ",
                            "size": "lg",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#000000"
                        }
                    ]
                },
                "hero": {
                    "type": "image",
                    "url": "%s",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "uri",
                        "label": "Action",
                        "uri": "https://linecorp.com"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                        "type": "uri",
                        "label": "Action",
                        "uri": "https://linecorp.com"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "text": "User ID",
                            "size": "lg",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "%s",
                            "size": "md"
                        },
                        {
                            "type": "text",
                            "text": "User Name",
                            "size": "lg",
                            "weight": "bold",
                            "color": "#000000",
                            "wrap": true
                        },
                        {
                            "type": "text",
                            "text": "%s",
                            "align": "start"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "spacer",
                            "size": "xxl"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "Modify",
                                "text": "[::text:]Modify"
                            },
                            "color": "#905C44",
                            "style": "primary"
                        }
                    ]
                }
            }
        ]
}"""
