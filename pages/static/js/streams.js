const APP_ID = 'e393edf6a2064a009f02a0dbd24284c5'
const CHANNEL = 'users'
const TOKEN = '006e393edf6a2064a009f02a0dbd24284c5IADh6YUCSH5RIThnL0aYOcXr5ZxLaMz62laTMiWntIYVX+mlgxQAAAAAEABg4SwUzAJMYgEAAQDMAkxi'
let UID;

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks =  []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    client.on('user-published', handleUserJoined)
    client.on('user-left', handleUserLeft)
    
    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `<div class="video-container" id="user-container-${UID}">
                    <div class="username-wrapper"><span class="user-name">My name</span></div>
                    <div class="video-player" id="user-${UID}"></div>
                </div>`
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

    localTracks[1].play(`user-${UID}`)

    await client.publish([localTracks[0], localTracks[1]])
}

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    if(mediaType === 'video'){
        let player = document.getElementById(`user-container-${user.uid}`)
        if (player != null){
            player.remove()
        }

        player = `<div class="video-container" id="user-container-${user.uid}}">
                <div class="username-wrapper"><span class="user-name">My name</span></div>
                <div class="video-player" id="user-${user.uid}"></div>
            </div>`
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
        user.videoTrack.play(`user-${user.uid}`)
    }

    if(mediaType === 'audio'){
        user.audioTrack.play()
    }
}

let handleUserLeft = async (user) => {
        delete remoteUsers[user,uid]
        document.getElementById(`user-container-${user.uid}`).remove()
    }
joinAndDisplayLocalStream()