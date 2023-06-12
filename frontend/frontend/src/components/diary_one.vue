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
            <div class="follower">
              <div class="num">{{ follower_count }}</div>
              <div class="text">追蹤者</div>
            </div>
            <div class="following">
              <div class="num">{{ following_count }}</div>
              <div class="text">追蹤中</div>

            </div>
          </div>
          <div class="top_nav">
            <div class="feedback_nav">
              <div class="num">{{ comment_count }}</div>
              <div class="text">則評分評論</div>
              <hr />
            </div>
            <div class="diary_nav">
              <div class="num">{{ diary_count }}</div>
              <div class="text">篇日記</div>

            </div>
            <div class="list_nav">
              <div class="num">{{ list_count }}</div>
              <div class="text">份清單</div>
            </div>
          </div>
          <div class="diarys">
            <div class="diary">
              <div class="time">2023.04.15 於</div>
              <div class="rest_name">鼎泰豐信義店</div><img class="rest_pic"
                src="https://img.ltn.com.tw/Upload/news/600/2021/04/12/phpG9MbVf.jpg" /><img class="pic_choose_icon" />
              <div class="diary_text">
                當天天氣晴朗，我決定去鼎泰豐享受美食。一進門就被熱鬧的氣氛和美味的香氣所吸引。我點了一份小籠包和一份酸辣湯，兩者都是鼎泰豐的經典菜品。小籠包皮薄餡多，肉汁鮮美，每口都讓我感受到豐富的口感。酸辣湯酸甜開胃，辣度恰到好處，非常適合我的口味。除此之外，我還點了一些其他的菜品，如紅油炒手和蝦仁燒賣。紅油炒手口感細膩，香辣可口；蝦仁燒賣則是鮮美多汁，讓我一口接一口。在享受美食的同時，服務員也非常周到，讓我感到賓至如歸。整體來說，這次的鼎泰豐之旅是一次美食之旅，讓我非常滿足。我期待著下一次的品嚐，也推薦給想要嚐鮮的人。
                籠包皮薄餡多，肉汁鮮美，每口都讓我感受到豐富的口感。酸辣湯酸甜開胃，辣度恰到好處，非常適合我的口味。</div>
              <div class="back_to_diary">回到日記 -></div>
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
export default {
  name: 'TastyExplorer_test',
  data() {
    return {
      user_name: "XXX美食家",
      following_count: 0,
      follower_count: 0,
      comment_count: 0,    // comment = review
      diary_count: 0,
      list_count: 0,
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
</style>