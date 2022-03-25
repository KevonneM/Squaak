const APP_ID = 'e393edf6a2064a009f02a0dbd24284c5'
const CHANNEL = 'hello'
const TOKEN = '006e393edf6a2064a009f02a0dbd24284c5IACjKwgSUlkmgVe6Mv4GLA/drshjhtrozd14sAl/xXCpp4amEDYAAAAAEAAg4mLW3tM+YgEAAQDe0z5i'
let UID;

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks =  []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
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

joinAndDisplayLocalStream()