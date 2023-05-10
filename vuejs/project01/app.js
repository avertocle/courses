const app = Vue.createApp({
  data() {
    return {
      detailsVisible : false,
      friends: [
        { id: "1", name: "Manuel Lorenz", phone: "01234 5678 991", pmail: "manuel@localhost.com" },
        { id: "2", name: "Julie Jones", phone: "09876 543 221", email: "julie@localhost.com" }
      ]
    }
  },
  methods:{
    toggleDetails(){
      this.detailsVisible = !this.detailsVisible
      console.log("details = " + this.detailsVisible)
    }
  }
});

app.component('friend-contact', {
  template: `
    <li v-for="f in friends" :key="f.id">
      <h2>{{f.name}}</h2>
      <button @click="toggleDetails">{{ detailsVisible ? "Hide Details" : "Show Details" }} </button>
      <ul v-if="detailsVisible">
        <li><strong>Phone:</strong>{{f.phone}}</li>
        <li><strong>Email:</strong>{{f.email}}</li>
      </ul>
    </li> 
  `,
  data() {
    return {
      detailsVisible : false,
      friends: [
        { id: "1", name: "Manuel Lorenz", phone: "01234 5678 991", pmail: "manuel@localhost.com" },
      ]

    }
  },
  methods:{
    toggleDetails(){
      this.detailsVisible = !this.detailsVisible
      console.log("details = " + this.detailsVisible)
    }
  }
})


app.mount("#app")


