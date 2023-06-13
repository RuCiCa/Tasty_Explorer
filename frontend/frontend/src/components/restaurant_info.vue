<template>
  <div>

    <div class="phone">
      <div class="screen">
        <div class="pages">
          <img class="back_icon" src="../assets/back.png" />
          <div class="rest_name">{{ rest_name }}</div>
          <div class="route_btn">路線</div>
          <div class="reserve_btn">預約</div>
          <div class="phone_btn">電話</div>
          <img class="rest_pic" src="../assets/rest_pic1.jpg" />
          <div class="rest_info">
            <img class="loc_icon" src="../assets/location.png" />
            <div class="loc">{{ address }}</div>
            <img class="open_icon" src="../assets/time.png" />
            <div class="is_open">已打烊 </div>
            <div class="open_time">開始營業時間：週四11:30</div>
            <img class="price_icon" src="../assets/price.png" />
            <div class="price">$400~600</div>
            <img class="website_icon" src="../assets/website.png" />
            <div class="website">{{ website }}</div>
          </div>
        </div>
        <div class="nav">
          <img class="search" src="../assets/menu.png" />
          <img class="more" src="../assets/feedback.png" />
          <img class="profile" src="../assets/about.png" />
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
      address: "中山區 | 台北市",
      id: 1,
      phone: "02-2562-1270",
      rest_name: "魚心日本料理",
      website: "https://www.facebook.com/%E9%AD%9A%E5%BF%83%E6%97%A5%E6%9C%AC%E6%96%99%E7%90%86-234781849865585/"
      
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
    const path = "http://localhost:5000/following";
    const restaurant_id = this.restaurant_id;
    console.log(user_id);

    axios
      .post(path, {restaurant_id})
      .then((res) => {
        console.log(res);
        this.address = res.data.restaurant[i].address;
        this.rest_name = res.data.restaurant[i].restaurant_name;
        this.phone = res.data.restaurant[i].phone;
        this.website = res.data.restaurant[i].website;
        // console.log(res.data.diary)

      })
      .catch((error) => {
        console.log(error);
      });
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

.screen .pages .back_icon {
  position: absolute;
  width: 30px;
  height: 30px;
  left: 5px;
  top: 28px;
}

.screen .pages .rest_name {
  position: absolute;
  width: 320px;
  height: 74px;
  left: calc(50% - 320px/2);
  top: 82px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 44px;
  text-align: center;
  color: #000000;
}

.screen .pages .route_btn {
  position: absolute;
  width: 40px;
  height: 24px;
  left: 28px;
  top: 156px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  text-align: center;
  color: #000000;
  padding: 8px 25px;
  background: #F3E4E4;
  border-radius: 8px;
}

.screen .pages .reserve_btn {
  position: absolute;
  width: 40px;
  height: 24px;
  left: 154px;
  top: 156px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  text-align: center;
  color: #000000;
  padding: 8px 25px;
  background: #F3E4E4;
  border-radius: 8px;
}

.screen .pages .phone_btn {
  position: absolute;
  width: 40px;
  height: 24px;
  left: 278px;
  top: 156px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  text-align: center;
  color: #000000;
  padding: 8px 25px;
  background: #F3E4E4;
  border-radius: 8px;
}

.screen .pages .rest_pic {
  position: absolute;
  width: 311px;
  height: 258px;
  left: 43px;
  top: 234px;
  border-radius: 8px;
}

.screen .pages .rest_info {
  position: absolute;
  width: 393px;
  height: 60px;
  left: 0px;
  top: 530px;
  background: #FFFFFF;
  border-top: 1px solid #000000;
}

.screen .pages .rest_info .loc_icon {
  position: absolute;
  width: 30px;
  height: 30px;
  left: 9px;
  top: 15px;
}

.screen .pages .rest_info .loc {
  position: absolute;
  width: 315px;
  height: 30px;
  left: calc(50% - 315px/2 + 14px);
  top: 20px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  text-align: center;
  color: #000000;
}

.screen .pages .rest_info .open_icon {
  position: absolute;
  width: 30px;
  height: 30px;
  left: 9px;
  top: 75px;
}

.screen .pages .rest_info .is_open {
  position: absolute;
  width: 65px;
  height: 30px;
  left: 68.5px;
  top: 75px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  text-align: center;
  color: #FF0000;
}

.screen .pages .rest_info .open_time {
  position: absolute;
  width: 307px;
  height: 30px;
  left: 138.66px;
  top: 75px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
}

.screen .pages .rest_info .price_icon {
  position: absolute;
  width: 30px;
  height: 30px;
  left: 9px;
  top: 135px;
}

.screen .pages .rest_info .price {
  position: absolute;
  width: 315px;
  height: 30px;
  left: 50%;
  top: 140px;
  transform: translate(-50%, 0%);
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  text-align: center;
  color: #000000;
}

.screen .pages .rest_info .website_icon {
  position: absolute;
  width: 30px;
  height: 30px;
  left: 9px;
  top: 195px;
}

.screen .pages .rest_info .website {
  position: absolute;
  height: 30px;
  left: 50%;
  top: 192px;
  transform: translate(-50%, 0%);
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  display: flex;
  align-items: center;
  text-align: center;
  -webkit-text-decoration-line: underline;
  text-decoration-line: underline;
  color: #000000;
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
}
</style>