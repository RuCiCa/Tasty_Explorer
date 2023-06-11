<template>
  <div>

    <div class="phone">
      <div class="screen">
        <div class="pages">
          <div class="search_bar"></div>
          <div class="filter_type">類型 🔻</div>
          <div class="filter_location">地區 🔻</div>
          <div class="filter_open">營業中</div>
          <div class="recent_search_title">最近搜尋</div>
          <div class="restaurants">
            <div class="restaurant" v-for="restaurant in restaurants" :key="restaurant.id">
              <img class="rest_pic" src="https://img.ltn.com.tw/Upload/news/600/2021/04/12/phpG9MbVf.jpg" />
              <div class="rest_name">{{ restaurant.rest_name }}</div>
              <div class="location">{{ restaurant.location_dis }} | {{ restaurant.location_city }}</div>
              <div class="add_icon"></div>
              <div class="rating_title">評分</div>
              <div class="rating_number">| {{ restaurant.rating_number }} 人已評分</div>
              <div class="rating">{{ restaurant.rating }}</div>
              <div class="contact_title">聯絡資訊</div>
              <div class="contact_number">{{ restaurant.contact_number }}</div>
            </div>
          </div>
          <div class="nav">
            <img class="search" src="../assets/search_pressed.png" />
            <img class="more" src="../assets/more.png" />
            <img class="profile" src="../assets/profile.png" />
          </div>
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
      restaurants: [
        { id: 1, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 987, rating: "❤❤❤", contact_number: "02-2562-1270" },
        { id: 2, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 97, rating: "❤❤❤❤", contact_number: "02-2562-1270" },
        { id: 3, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 87, rating: "❤❤❤❤❤", contact_number: "02-2562-1270" },
        { id: 4, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 98, rating: "❤❤❤❤❤", contact_number: "02-2562-1270" },
        { id: 5, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 187, rating: "❤", contact_number: "02-2562-1270" },
        { id: 6, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 383, rating: "❤❤❤❤", contact_number: "02-2562-1270" },

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

.screen .pages .search_bar {
  position: absolute;
  width: 338px;
  height: 31px;
  left: 27px;
  top: 35px;
  border: 1px solid #DDDDDD;
  border-radius: 15px;
}

.screen .pages .filter_type {
  position: absolute;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  left: 37px;
  top: 82px;
  background: #FFFFFF;
  border: 1px solid #DDDDDD;
  border-radius: 15px;
  padding: 2px 20px 2px 26px;
}

.screen .pages .filter_location {
  position: absolute;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  left: 150px;
  top: 82px;
  background: #FFFFFF;
  border: 1px solid #DDDDDD;
  border-radius: 15px;
  padding: 2px 20px 2px 26px;
}

.screen .pages .filter_open {
  position: absolute;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  left: 263px;
  top: 82px;
  background: #FFFFFF;
  border: 1px solid #DDDDDD;
  border-radius: 15px;
  padding: 2px 28px;
}

.screen .pages .recent_search_title {
  position: absolute;
  width: 80px;
  height: 24px;
  left: 37px;
  top: 118px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
}

.screen .pages .restaurants {
  position: absolute;
  margin-top: 10px;
  width: 337px;
  height: 628px;
  left: 28px;
  top: 150px;
  overflow: hidden;
  overflow-y: auto;
}

.screen .pages .restaurants .restaurant {
  width: 337px;
  height: 123px;
  background: #F3E4E4;
  border-radius: 5px;
  margin-bottom: 20px;
}

.screen .pages .restaurants .restaurant .rest_pic {
  position: absolute;
  width: 122px;
  height: 94px;
  left: 12px;
  top: 14px;
  border-radius: 5px;
}

.screen .pages .restaurants .restaurant .rest_name {
  position: absolute;
  width: 84px;
  height: 17px;
  left: 148px;
  top: 14px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  /* identical to box height */
  text-align: center;
  color: #000000;
}

.screen .pages .restaurants .restaurant .location {
  position: absolute;
  width: 83px;
  height: 15px;
  left: 148px;
  top: 34px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  color: #888888;
}

.screen .pages .restaurants .restaurant .rating_title {
  position: absolute;
  width: 24px;
  height: 15px;
  left: 148px;
  top: 65px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 12px;
  line-height: 15px;
  text-align: center;
  color: #000000;
}

.screen .pages .restaurants .restaurant .rating_number {
  position: absolute;
  height: 10px;
  left: 175px;
  top: 67px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 10px;
  color: #888888;
}

.screen .pages .restaurants .restaurant .rating {
  position: absolute;
  height: 12px;
  left: 260px;
  top: 62px;
  font-size: 12px
}

.screen .pages .restaurants .restaurant .contact_title {
  position: absolute;
  width: 48px;
  height: 15px;
  left: 148px;
  top: 91px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 12px;
  line-height: 15px;
  text-align: center;
  color: #000000;
}

.screen .pages .restaurants .restaurant .contact_number {
  position: absolute;
  width: 82px;
  height: 15px;
  left: 255px;
  top: 91px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 15px;
  text-align: center;
  color: #000000;
}

.screen .pages .restaurants .feedback {
  width: 337px;
  height: 301px;
  background: #F3E4E4;
  border-radius: 5px;
  margin: 0 0 20px 0;
}

.nav {
  top: 788px;
  background-color: #fff;
  width: 100%;
  height: 66px;
  border-radius: 0 0 25px 25px;
  border-top: 1px solid #DDDDDD;
}

.nav .search {
  position: absolute;
  width: 36px;
  height: 36px;
  top: 15px;
  left: 39px;
}

.nav .more {
  position: absolute;
  width: 36px;
  height: 36px;
  top: 15px;
  left: 178px;
}

.nav .profile {
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

.restaurants::-webkit-scrollbar {
  width: 0;
}
</style>