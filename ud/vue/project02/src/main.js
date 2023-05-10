import { createApp } from 'vue'
import App from './App.vue'
import FriendContact from './components/friend_contact.vue'

const app = createApp(App);

app.component('friend-contact', FriendContact);

app.mount('#app');
