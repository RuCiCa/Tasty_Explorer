<template>
  <div>

    <div class="phone">
      <div class="screen">
        <div class="pages"><img class="arrow"
            src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQvIOHo-rHocRyC90IbCYaUTqrSvQVBXinULOIbFrgSM2NIxGzu" />
          <div class="list_info">
            <div class="name">{{list_name}}</div>
            <div class="info">公開 | {{ res_num }} 家餐廳 | {{ user_name }}</div><img class="add_icon" /><img class="more_info_icon" />
          </div>
          <div class="restaurants">
            <div class="restaurant" v-for="restaurant in restaurants" :key="restaurant.id">
              <img class="rest_pic" src="https://img.ltn.com.tw/Upload/news/600/2021/04/12/phpG9MbVf.jpg" />
              <div class="rest_name">{{ restaurant.rest_name }}</div>
              <div class="location">{{ restaurant.location_dis }}</div>
              <div class="add_icon"></div>
              <div class="rating_title">評分</div>
              <div class="rating_number">| {{ restaurant.rating_number }} 人已評分</div>
              <div class="rating">{{ restaurant.rating }}</div>
              <div class="contact_title">聯絡資訊</div>
              <div class="contact_number">{{ restaurant.contact_number }}</div>
            </div>
          </div>
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
      list_name: "就是要拉麵",
      list_id: 1,
      res_num: "35",
      user_name: "XXX美食家",
      restaurants: []
      //   isVisible: true,
    };
  },
  mounted() {
    const path = "http://localhost:5000/list_info";
    const list_id = this.list_id;

    axios
      // post 過去的東西要包大括號 {}
      .post(path, {list_id})
      .then((res) => {
        console.log(res.data);
        this.list_name = res.data.list_info[0].list_name;
        this.res_num = res.data.list_info[0].num_res;
        this.user_name = res.data.list_info[0].user_name;
        for (var i = 0; i < res.data.list_res.length; i++) {
          this.restaurants.push({ id: i+1, rest_name: res.data.list_res[i].restaurant_name, location_dis: res.data.list_res[i].address, rating_number: res.data.list_res[i].rating_num, rating: res.data.list_res[i].rating, contact_number: res.data.list_res[i].phone});
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

.screen .pages .arrow {
  position: absolute;
  width: 25px;
  left: 27px;
  top: 25px;
}

.screen .pages .list_info {
  left: 29px;
  top: 64px;
}

.screen .pages .list_info .name {
  position: absolute;
  width: 120px;
  height: 29px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  line-height: 29px;
  text-align: center;
  color: #000000;
}

.screen .pages .list_info .info {
  position: absolute;
  width: 265px;
  height: 24px;
  top: 38px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #888888;
}

.screen .pages .list_info .more_info_icon {
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

.screen .pages .restaurants {
  position: absolute;
  margin-top: 10px;
  width: 337px;
  height: 680px;
  left: 28px;
  top: 158px;
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
  /* width: 84px; */
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

.restaurants::-webkit-scrollbar {
  width: 0;
}
</style>