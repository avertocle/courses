<template>
  <li>
    <h2>{{ name }}</h2>
    <button @click="toggleDetails">
      {{ detailsVisible ? "Hide Details" : "Show Details" }}
    </button>
    <ul v-if="detailsVisible">
      <li><strong>Phone : </strong>{{ phoneNumber }}</li>
      <li><strong>Email : </strong>{{ emailAdd }}</li>
    </ul>
  </li>
</template>

<script>
export default {
  props:[
    'id',
    'name',
    'phoneNumber',
    'emailAdd'
  ],
  data() {
    return {
      detailsVisible: false,
    };
  },
  methods: {
    toggleDetails() {
      this.detailsVisible = !this.detailsVisible;
      console.log("details = " + this.detailsVisible);
    },
  },
};
</script>
