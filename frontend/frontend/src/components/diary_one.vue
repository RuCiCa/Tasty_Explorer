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

            </div>
          </div>
          <div class="top_nav">
            <div class="feedback_nav" @click="go_to_review">
              <div class="num">{{ comment_count }}</div>
              <div class="text">則評分評論</div>

            </div>
            <div class="diary_nav" @click="go_to_diary">
              <div class="num">{{ diary_count }}</div>
              <div class="text">篇日記</div>
              <hr />
            </div>
            <div class="list_nav" @click="go_to_lists">
              <div class="num">{{ list_count }}</div>
              <div class="text">份清單</div>
            </div>
          </div>
          <div class="diarys">
            <div class="diary">
              <div class="time">{{ diary_time }} 於</div>
              <div class="rest_name">{{ rest_name }}</div><img class="rest_pic"
                src="https://img.ltn.com.tw/Upload/news/600/2021/04/12/phpG9MbVf.jpg" />
              <img class="delete_icon" src="../assets/delete.png" @click="delete_diary(diary_id)" />
              <img class="pic_choose_icon" src="../assets/edit.png" @click="to_edit_diary(diary_id)" />
              <div class="diary_text">
                {{ diary_text }}</div>
              <div class="back_to_diary" @click="go_to_diary">回到日記 -></div>
            </div>
          </div>
        </div>
        <div class="nav">
          <img class="search" src="../assets/search.png" @click="go_to_search" />
          <img class="more" src="../assets/more.png" @click="go_to_new_diary" />
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
  name: 'diary_one',
  data() {
    return {
      user_name: "XXX美食家",
      user_id: this.$route.params.user_id,
      following_count: 0,
      follower_count: 0,
      comment_count: 0,    // comment = review
      diary_count: 0,
      list_count: 0,
      diary_id: this.$route.params.diary_id,
      photo: "test.jpgg",
      diary_time: "",
      rest_name: "",
      diary_photo: "test.jpgg",
      diary_text: "",
      //   isVisible: true,
    };
  },
  mounted() {
    const path = "http://localhost:5000/diary_info";
    const user_id = this.user_id;
    const diary_id = this.diary_id;

    axios
      // post 過去的東西要包大括號 {}
      .post(path, { "user_id": user_id, "diary_id": diary_id })
      .then((res) => {
        console.log(diary_id);
        this.comment_count = res.data.comment_count;
        this.diary_count = res.data.diary_count;
        this.list_count = res.data.list_count;
        this.follower_count = res.data.follower_count;
        this.following_count = res.data.following_count;
        this.user_name = res.data.info[0].user_name;
        this.diary_time = res.data.diary[0].date_visited;
        this.rest_name = res.data.diary[0].restaurant_name;
        this.diary_text = res.data.diary[0].diary_content;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  beforeUnmount() {

  },
  methods: {

    go_to_follower() {
      this.$router.push('/follower');
    },
    go_to_lists() {
      this.$router.push('/lists');
    },
    go_to_following() {
      this.$router.push('/following');
    },
    go_to_diary() {
      this.$router.push('/diary');
    },
    go_to_review() {
      this.$router.push('/review');
    },

    to_edit_diary(diary_id) {
      this.$router.push({ name: 'edit_diary', params: { diary_id: diary_id } });
    },

    go_to_new_diary() {
      this.$router.push('/new_diary');
    },

    delete_diary(diary_id) {
      const path = "http://localhost:5000/diary_info";
      const user_id = this.user_id;


      axios
        // post 過去的東西要包大括號 {}s
        .post(path, { "user_id": user_id, "diary_id": diary_id, "isDelete": false })
        .then((res) => {
          this.$router.push('/diary');
        })
        .catch((error) => {
          console.log(error);
        });

    },


  },
  created() {

  },
};
</script>

<style scoped>
* {
  position: relative;
  font-family: "Noto Sans TC";
  vertical-align: top;
}

html,
body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
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
  left: 0;
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
  top: 186px;
  background: #FCE8E8;
  border-radius: 15px;
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
  width: 60px;
  height: 60px;
  top: 3px;
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

.diarys::-webkit-scrollbar {
  width: 0;
}

.diarys {
  position: absolute;
  margin-top: 10px;
  width: 337px;
  height: 591px;
  left: 28px;
  top: 190px;
}

.diarys .diary {
  width: 337px;
  height: 578px;
  background: #F3E4E4;
  border-radius: 5px;
  margin: 0 0 20px 0;
}

.diarys .diary .rest_name {
  position: absolute;
  height: 17px;
  left: 107px;
  top: 11px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  color: #000000;
}

.diarys .diary .back_to_diary {
  position: absolute;
  width: 74px;
  height: 17px;
  left: 252px;
  top: 558px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 17px;
  color: #888888;
}

.diarys .diary .time {
  position: absolute;
  height: 17px;
  left: 18px;
  top: 11px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 17px;
  color: #000000;
}

.diarys .diary .diary_text {
  position: absolute;
  width: 303px;
  height: 30px;
  left: 17px;
  top: 264px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  color: #000000;
}

.diarys .diary .rest_pic {
  position: absolute;
  width: 299px;
  height: 201px;
  left: 19px;
  top: 37px;
  border-radius: 5px;
}

.pic_choose_icon {
  position: absolute;
  width: 12px;
  height: 13px;
  left: 317px;
  top: 12px;
}

.delete_icon {
  position: absolute;
  height: 15px;
  width: 15px;
  left: 295px;
  top: 12px;
}
</style>