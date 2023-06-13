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

            </div>
            <div class="list_nav" @click="go_to_lists">
              <div class="num">{{ list_count }}</div>
              <div class="text">份清單</div>
              <hr />
            </div>
          </div>
          <div class="order_title">排序</div>
          <div class="by_created_date">依創建日期</div>
          <div class="by_edited_date">依修改日期</div>
          <div class="by_rest_num">依餐廳數量</div>
          <div class="lists">
            <div class="list" v-for="list in lists" :key="list.id" @click="to_diary_one(list.id)">
              <div class="list_name">{{ list.list_name }}</div>
              <div class="info">{{ list.info_isPublic }} | {{ list.info_rest_num }} 家餐廳</div>
              <div class="tag_icon"></div>
              <div class="info_icon"></div>
            </div>
          </div>
        </div>
        <div class="nav">
          <img class="search" src="../assets/search.png" @click="go_to_search" />
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
      lists: []
      //   isVisible: true,
    };
  },
  mounted() {
    const path = "http://localhost:5000/list";
    const user_id = this.user_id;

    axios
      // post 過去的東西要包大括號 {}
      .post(path, { user_id })
      .then((res) => {
        console.log(res.data);
        this.comment_count = res.data.comment_count;
        this.diary_count = res.data.diary_count;
        this.list_count = res.data.list_count;
        this.follower_count = res.data.follower_count;
        this.following_count = res.data.following_count;
        this.user_name = res.data.info[0].user_name;
        for (var i = 0; i < res.data.list.length; i++) {
          this.lists.push({ id: res.data.list[i].id, list_name: res.data.list[i].list_name, info_rest_num: res.data.list[i].res_num });
        }
        // console.log(res.data.diary);



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
    go_to_list(id) {
      this.$router.push({ name: 'list', params: { list_id: id } });
    }

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

.order_title {
  position: absolute;
  width: 32px;
  height: 19px;
  left: 34px;
  top: 195px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 19px;
  text-align: center;
  color: #000000;
}

.by_created_date {
  position: absolute;
  width: 69px;
  height: 11px;
  left: 79px;
  top: 193px;
  font-family: "Noto Sans TC";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 180%;
  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: 1.25px;
  color: #000000;
  border: 1px solid #DDDDDD;
  border-radius: 10px;
  padding: 5.5px 11px;
}

.by_edited_date {
  position: absolute;
  width: 69px;
  height: 11px;
  left: 176px;
  top: 193px;
  font-family: "Noto Sans TC";
  font-style: normal;
  font-size: 12px;
  line-height: 180%;
  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: 1.25px;
  font-weight: 600;
  color: #BD0A0A;
  border: 1px solid #DDDDDD;
  border-radius: 10px;
  padding: 5.5px 11px;
  background: #FCE8E8;
}

.by_rest_num {
  position: absolute;
  width: 69px;
  height: 11px;
  left: 272px;
  top: 193px;
  font-family: "Noto Sans TC";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 180%;
  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: 1.25px;
  color: #000000;
  border: 1px solid #DDDDDD;
  border-radius: 10px;
  padding: 5.5px 11px;
}

.lists::-webkit-scrollbar {
  width: 0;
}

.lists {
  top: 220px;
  height: 566px;
  position: absolute;
  margin-top: 10px;
  width: 337px;
  left: 28px;
  overflow: hidden;
  overflow-y: auto;
}

.lists .list {
  width: 337px;
  height: 57px;
  background: #F3E4E4;
  border-radius: 5px;
  margin: 0 0 20px 0;
}

.lists .list .list_name {
  position: absolute;
  height: 17px;
  left: 17px;
  top: 11px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 17px;
  text-align: center;
  color: #000000;
}

.lists .list .info {
  position: absolute;
  height: 15px;
  left: 17px;
  top: 33px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  color: #888888;
}
</style>