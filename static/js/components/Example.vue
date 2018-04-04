<template>
  <div id="">
      <table class="table">
            <thead>
                <th>Title</th>
                <th>Platform</th>
            </thead>
            <tbody>
                <tr v-for="(game, index) in list" :key=index>
                    <td>{{ game.fields.title }}</td>
                    <td>{{ game.fields.platform }}</td>
                </tr>
            </tbody>
        </table>
  </div>
</template>

<script>
export default {
    data(){
        return {
            list: []
        }
    },
    mounted(){
        this.$http.get("/homepage/games").then( (res) => this.list = res.data )
    }
}
</script>

<style>

</style>
