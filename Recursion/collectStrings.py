def collectStrings(obj):
    str_arr = []
    for value in obj.values():
        if type(value) is str:
            str_arr.append(value)
        elif type(value) is dict:
            str_arr += collectStrings(value)
    return str_arr

print(collectStrings({"stuff": "foo",
                      "data":{
                          "val":{
                              "thing":{
                                  "info": "bar",
                                  "moreinfo":{
                                      "evenMoreInfo": {
                                          "weMadeIt": "baz"
                                                      }
                                             }
                                     }
                                }
                            }
                      })
    )