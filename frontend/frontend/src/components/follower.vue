<template>
  <div>
    <div class="phone">
      <div class="screen">
        <div class="pages">
          <div class="person_info">
            <div class="pic"></div>
            <div class="name_level">
              <div class="name">{{ user_name }}</div>
              <div class="level">等級:5</div>
            </div>
            <div class="follower" @click="go_to_follower">
              <div class="num">{{ follower_count }}</div>
              <div class="text">追蹤者</div>
            </div>
            <div class="following" @click="go_to_following">
              <div class="num">{{ following_count }}</div>
              <div class="text">追蹤中</div>
              <hr />
            </div>
          </div>
          <div class="search_bar"><img class="search_icon" src="" alt="" /></div>
          <div class="followings">
            <div class="following" v-for="follower in followers" :key="follower.id">
              <div class="pic"></div>
              <div class="name_level">
                <div class="name">{{ follower.name }}</div>
                <div class="level">等級:5</div>
              </div>
              <div class="follow_button" v-if="follower.followed">追蹤</div>
              <div class="followed_button" v-else>追蹤中</div>
            </div>

          </div>
        </div>
        <div class="nav">
          <img class="search" src="../assets/search.png" />
          <img class="more" src="../assets/more.png" />
          <img class="profile" src="../assets/profile_pressed.png" />
        </div>
      </div>
    </div>
    <h2 class="phonename">iphone14 pro</h2>
  </div>
</template>


<script>
import axios from 'axios';
export default {
  name: 'TastyExplorer_test',
  data() {
    return {
      user_name: "XXX美食家",
      user_id: 1,
      following_count: 0,
      follower_count: 0,
      comment_count: 0,    // comment = review
      diary_count: 0,
      list_count: 0,
      followers: [
        { id: 1, name: "胖胖", followed: true },
        { id: 2, name: "胖胖", followed: true },
        { id: 3, name: "胖胖", followed: true },
        { id: 4, name: "胖胖", followed: true },
        { id: 5, name: "胖胖", followed: true },
        { id: 6, name: "胖胖", followed: true },
        { id: 7, name: "胖胖", followed: true },
        { id: 8, name: "胖胖", followed: true },
        { id: 9, name: "胖胖", followed: true },
        { id: 10, name: "胖胖", followed: true },
        { id: 11, name: "胖胖", followed: true },
      ]
      //   isVisible: true,
    };
  },
  mounted() {

  },
  beforeUnmount() {

  },
  methods: {

  },
  created() {
    const path = "http://localhost:5000/follower";
    const user_id = this.user_id;
    console.log(user_id);

    axios
      .post(path, {user_id})
      .then((res) => {
        console.log(res);
        this.comment_count = res.data.comment_count;
        this.diary_count = res.data.diary_count;
        this.list_count = res.data.list_count;
        this.follower_count = res.data.follower_count;
        this.following_count = res.data.following_count;
        for (var i = 0; i < res.data.diary.length; i++) {
          this.followers.push({ id: res.data.followers[i].followers_id, name: res.data.followers[i].user_name, followed: true });
        }
        // console.log(res.data.diary)

      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>* {
  position: relative;
  font-family: "Noto Sans TC";
  vertical-align: top;
}

html,
body {
  width: 100%;
  height: 100%;
  margin: 0 auto;
  padding: 0 auto;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.phone {
  width: 395px;
  padding: 10px;
  background-color: #000;
  border-radius: 25px;
  transition: 0.5s;
  /* left: 100px; */
}

.screen {
  height: 852px;
  width: 393px;
  transition: 0.5s;
  border-radius: 25px;
  cursor: pointer;
  background-color: #fff;
}

.screen .pages {
  width: 100%;
  height: 786px;
  transition: 0.5s;
  left: 0px;
}

.screen .pages .person_info {
  left: 28px;
  top: 56px;
}

.screen .pages .person_info .pic {
  background-color: #ddd;
  border-radius: 100%;
  position: absolute;
  width: 60px;
  height: 60px;
}

.screen .pages .person_info .name_level .name {
  position: absolute;
  width: px;
  height: 24px;
  left: 79px;
  top: 6px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
}

.screen .pages .person_info .name_level .level {
  position: absolute;
  width: 44px;
  height: 15px;
  left: 79px;
  top: 32px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  color: #888888;
}

.screen .pages .person_info .follower {
  position: absolute;
  width: 49px;
  height: 38px;
  left: 203px;
  top: 5px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 22px;
  text-align: center;
  color: #BD0A0A;
}

.screen .pages .person_info .follower .text {
  font-size: 14px;
  color: #000;
}

.screen .pages .person_info .follower hr {
  width: 73px;
  left: -12px;
}

.screen .pages .person_info .following {
  position: absolute;
  width: 49px;
  height: 38px;
  left: 294px;
  top: 5px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 22px;
  text-align: center;
  color: #BD0A0A;
}

.screen .pages .person_info .following .text {
  font-size: 14px;
  color: #000;
}

.screen .pages .person_info .following hr {
  width: 73px;
  left: -12px;
}

.screen .pages .top_nav {
  left: 32px;
  top: 127px;
}

.screen .pages .top_nav .feedback_nav {
  width: 96px;
  height: 34px;
  left: 0px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 22px;
  text-align: center;
  color: #BD0A0A;
}

.screen .pages .top_nav .feedback_nav .text {
  font-size: 14px;
  color: #000;
}

.screen .pages .top_nav .diary_nav {
  position: absolute;
  width: 58px;
  height: 34px;
  left: 137px;
  top: 0px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 22px;
  text-align: center;
  color: #BD0A0A;
}

.screen .pages .top_nav .diary_nav .text {
  font-size: 14px;
  color: #000;
}

.screen .pages .top_nav .diary_nav hr {
  width: 96px;
  left: -21px;
}

.screen .pages .top_nav .list_nav {
  position: absolute;
  width: 58px;
  height: 34px;
  left: 256px;
  top: 0px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 22px;
  text-align: center;
  color: #BD0A0A;
}

.screen .pages .top_nav .list_nav .text {
  font-size: 14px;
  color: #000;
}

.screen .pages .top_nav .list_nav hr {
  width: 96px;
  left: -19px;
}

.screen .pages .search_bar {
  position: absolute;
  width: 338px;
  height: 31px;
  left: 27px;
  top: 137px;
  background: #FCE8E8;
  border-radius: 15px;
}

.screen .pages .followings .following {
  width: 337px;
  height: 60px;
  margin: 0 0 20px 0;
}

.screen .nav {
  background-color: #fff;
  width: 100%;
  height: 66px;
  border-radius: 0 0 25px 25px;
  border-top: 1px solid #DDDDDD;
}

.screen .nav .search {
  position: absolute;
  width: 36px;
  height: 36px;
  top: 15px;
  left: 39px;
}

.screen .nav .more {
  position: absolute;
  width: 36px;
  height: 36px;
  top: 15px;
  left: 178px;
}

.screen .nav .profile {
  position: absolute;
  width: 36px;
  height: 36px;
  top: 15px;
  left: 311px;
}

.status,
.phonename {
  color: #000;
  margin: 0;
}

.phonename {
  margin: 10px;
}

hr {
  border-top: 1pt solid black;
}

.followings::-webkit-scrollbar {
  width: 0;
}

.followings {
  position: absolute;
  margin-top: 10px;
  width: 337px;
  height: 591px;
  left: 28px;
  top: 185px;
  overflow: hidden;
  overflow-y: auto;
}

.followings .following .pic {
  background-color: rgba(101, 67, 33, 0.5);
  border-radius: 100%;
  position: absolute;
  width: 60px;
  height: 60px;
}

.followings .following .name_level .name {
  position: absolute;
  width: px;
  height: 24px;
  left: 79px;
  top: 6px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
}

.followings .following .name_level .level {
  position: absolute;
  width: 44px;
  height: 15px;
  left: 79px;
  top: 32px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  color: #888888;
}

.followings .following .follow_button {
  text-align: center;
  align-items: center;
  position: absolute;
  letter-spacing: 1.25px;
  font-weight: 500;
  font-size: 14px;
  line-height: 30px;
  width: 109px;
  height: 28px;
  left: 220px;
  top: 16px;
  background: #B82C30;
  border-radius: 5px;
  color: #fff;
  padding-bottom: 2px;
}

.followings .following .follow_button {
  text-align: center;
  align-items: center;
  position: absolute;
  letter-spacing: 1.25px;
  font-weight: 500;
  font-size: 14px;
  line-height: 30px;
  width: 109px;
  height: 28px;
  left: 220px;
  top: 16px;
  background: #B82C30;
  border-radius: 5px;
  color: #fff;
}
</style>