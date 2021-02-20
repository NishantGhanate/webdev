
# ftl



## Indices

* [Ungrouped](#ungrouped)

  * [user_detail](#1-user_detail)
  * [user_list](#2-user_list)


--------


## Ungrouped



### 1. user_detail



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1:8000/v1/ftl/user_detail
```



***Query params:***

| Key | Value | Description |
| --- | ------|-------------|
| user_id | 1A |  |



***More example Requests/Responses:***


##### I. Example Request: user_detail



***Query:***

| Key | Value | Description |
| --- | ------|-------------|
| user_id | 1A |  |



##### I. Example Response: user_detail
```js
{
    "success": true,
    "status_code": 200,
    "message": "User activity found",
    "data": {
        "member": {
            "id": "1A",
            "real_name": "Rolling",
            "time_zone": "Asia/Kolkata",
            "activity": [
                {
                    "start_time": "Start",
                    "end_time": "End"
                },
                {
                    "start_time": "Start 1",
                    "end_time": "End - 2"
                },
                {
                    "start_time": "Start 3",
                    "end_time": "End 3"
                }
            ]
        }
    }
}
```


***Status Code:*** 200

<br>



### 2. user_list



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1:8000/v1/ftl/user_list
```



***More example Requests/Responses:***


##### I. Example Request: user_list



##### I. Example Response: user_list
```js
{
    "success": true,
    "status_code": 200,
    "message": "User activity found",
    "data": {
        "members": [
            {
                "id": "1A",
                "real_name": "Rolling",
                "tz": "Asia/Kolkata",
                "activity_periods": [
                    {
                        "start_time": "Start",
                        "end_time": "End"
                    },
                    {
                        "start_time": "Start 1",
                        "end_time": "End - 2"
                    },
                    {
                        "start_time": "Start 3",
                        "end_time": "End 3"
                    }
                ]
            },
            {
                "id": "1B",
                "real_name": "One BEEE",
                "tz": "Asia/Kolkata",
                "activity_periods": [
                    {
                        "start_time": "Start 1",
                        "end_time": "End 1"
                    },
                    {
                        "start_time": "Start 2",
                        "end_time": "End 2"
                    }
                ]
            },
            {
                "id": "1C",
                "real_name": "One SEE",
                "tz": "Asia/Kolkata",
                "activity_periods": [
                    {
                        "start_time": "Start 1",
                        "end_time": "End 1"
                    }
                ]
            }
        ]
    }
}
```


***Status Code:*** 200

<br>



---
[Back to top](#ftl)
> Made with &#9829; by [thedevsaddam](https://github.com/thedevsaddam) | Generated at: 2021-02-20 14:53:41 by [docgen](https://github.com/thedevsaddam/docgen)
