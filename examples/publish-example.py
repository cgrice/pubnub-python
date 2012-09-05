from Pubnub import Pubnub

## Initiate Class
pubnub = Pubnub( 'pub-5c6ad54a-2ac8-4e5b-9671-3c5d10730ef8', 'sub-54010170-f5e2-11e1-826d-d91f52818550', None, False )

## Publish Example
info = pubnub.publish({
    'channel' : 'hello_world',
    'message' : {
        'some_text' : 'Hello my World'
    }
})
print(info)

