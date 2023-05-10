const app = Vue.createApp({
  data() {
    return { 
      inputGoal : "",
      goals: [] 
    };
  },
  methods : {
    addGoal(){
      console.log("goal added : " + this.inputGoal);
      this.goals.push(this.inputGoal);
    },
    removeGoal(index){
      console.log("goal removed : " + this.goals[index]);
      this.goals.splice(index, 1);
    },
    showGoalsHeader(){
      if(this.goals.length === 0 ){
        return "No goals have been added yet - please start adding some!";
      }else{
        return ""
      }
    },
    showGoals(){
      if(this.goals.length === 0 ){
        return "No goals have been added yet - please start adding some!";
      }else{
        return this.goals
      }
    }
  }
});

app.mount('#user-goals');
