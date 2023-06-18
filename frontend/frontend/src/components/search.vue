<template>
  <div>

    <div class="phone">
      <div class="screen">
        <div class="pages">
          <div class="overlay" v-if="showOverlay"></div>
          <div class="search_bar"></div>
          <div class="filter_type" :style="type" @click="choose_type">類型 🔻</div>
          <div class="filter_location" :style="location" @click="choose_location">地區 🔻</div>
          <div class="filter_open" :style="open" @click="choose_open">營業中</div>
          <div class="recent_search_title">搜尋結果</div>
          <div class="restaurants">
            <div class="restaurant" v-for="restaurant in restaurants" :key="restaurant.id">
              <img class="rest_pic" src="https://img.ltn.com.tw/Upload/news/600/2021/04/12/phpG9MbVf.jpg" />
              <div class="rest_name">{{ restaurant.rest_name }}</div>
              <div class="location">{{ restaurant.location }}</div>
              <div class="add_icon"></div>
              <div class="rating_title">評分</div>
              <div class="rating_number">| {{ restaurant.rating_number }} 人已評分</div>
              <div class="rating">{{ restaurant.rating }}</div>
              <div class="contact_title">聯絡資訊</div>
              <div class="contact_number">{{ restaurant.contact_number }}</div>
            </div>
          </div>
          <div class="filter_type_window" v-if="showFilter_type_window">
            <div class="title">類別</div>
            <div class="type1" :style="t1" @click="changeStyle_t1">中式</div>
            <div class="type2" :style="t2" @click="changeStyle_t2">美式</div>
            <div class="type3" :style="t3" @click="changeStyle_t3">日式</div>
            <div class="type4" :style="t4" @click="changeStyle_t4">韓式</div>
            <div class="type5" :style="t5" @click="changeStyle_t5">義式</div>
            <div class="type6" :style="t6" @click="changeStyle_t6">火鍋</div>
            <div class="type7" :style="t7" @click="changeStyle_t7">燒烤</div>
            <div class="type8" :style="t8" @click="changeStyle_t8">正餐</div>
            <div class="type9" :style="t9" @click="changeStyle_t9">點心</div>
            <div class="type10" :style="t10" @click="changeStyle_t10">酒吧</div>
            <div class="type11" :style="t11" @click="changeStyle_t11">飲品</div>
            <div class="type12" :style="t12" @click="changeStyle_t12">其他</div>
            <div class="clear_btn">清除</div>
            <div class="comfirm_btn" @click="comfirm_type">確認</div>
          </div>
          <div class="filter_type_window" v-if="showFilter_location_window">
            <div class="title">地區</div>
            <div class="type1" :style="l1" @click="changeStyle_l1">中正區</div>
            <div class="type2" :style="l2" @click="changeStyle_l2">大同區</div>
            <div class="type3" :style="l3" @click="changeStyle_l3">中山區</div>
            <div class="type4" :style="l4" @click="changeStyle_l4">松山區</div>
            <div class="type5" :style="l5" @click="changeStyle_l5">大安區</div>
            <div class="type6" :style="l6" @click="changeStyle_l6">萬華區</div>
            <div class="type7" :style="l7" @click="changeStyle_l7">信義區</div>
            <div class="type8" :style="l8" @click="changeStyle_l8">士林區</div>
            <div class="type9" :style="l9" @click="changeStyle_l9">北投區</div>
            <div class="type10" :style="l10" @click="changeStyle_l10">內湖區</div>
            <div class="type11" :style="l11" @click="changeStyle_l11">南港區</div>
            <div class="type12" :style="l12" @click="changeStyle_l12">文山區</div>
            <div class="clear_btn">清除</div>
            <div class="comfirm_btn" @click="comfirm_location">確認</div>
          </div>
          <div class="nav" v-if="!showOverlay">
            <img class="search" src="../assets/search_pressed.png" />
            <img class="more" src="../assets/more.png" @click="go_to_new_diary" />
            <img class="profile" src="../assets/profile.png" @click="go_to_diary" />
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
      search_content: "",
      type_list: [],
      place_list: [],
      restaurants: [
        // { id: 1, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 987, rating: "❤❤❤", contact_number: "02-2562-1270" },
        // { id: 2, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 97, rating: "❤❤❤❤", contact_number: "02-2562-1270" },
        // { id: 3, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 87, rating: "❤❤❤❤❤", contact_number: "02-2562-1270" },
        // { id: 4, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 98, rating: "❤❤❤❤❤", contact_number: "02-2562-1270" },
        // { id: 5, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 187, rating: "❤", contact_number: "02-2562-1270" },
        // { id: 6, rest_name: "鼎泰豐信義店", location_dis: "信義區", location_city: "台北市", rating_number: 383, rating: "❤❤❤❤", contact_number: "02-2562-1270" },

      ],
      showOverlay: false,
      type: {
        color: '#000000',
        background: "#FFFFFF",
        border: "1px solid #DDDDDD",
      },
      location: {
        color: '#000000',
        background: "#FFFFFF",
        border: "1px solid #DDDDDD",
      },

      open: {
        color: '#000000',
        background: "#FFFFFF",
        border: "1px solid #DDDDDD",
      },
      isOpen: false,
      // type
      showFilter_type_window: false,
      t1: {
        color: '#000000',
      },
      type1: false,
      t2: {
        color: '#000000',
      },
      type2: false,
      t3: {
        color: '#000000',
      },
      type3: false,
      t4: {
        color: '#000000',
      },
      type4: false,
      t5: {
        color: '#000000',
      },
      type5: false,
      t6: {
        color: '#000000',
      },
      type6: false,
      t7: {
        color: '#000000',
      },
      type7: false,
      t8: {
        color: '#000000',
      },
      type8: false,
      t9: {
        color: '#000000',
      },
      type9: false,
      t10: {
        color: '#000000',
      },
      type10: false,
      t11: {
        color: '#000000',
      },
      type11: false,
      t12: {
        color: '#000000',
      },
      type12: false,

      // location
      showFilter_location_window: false,
      l1: {
        color: '#000000',
      },
      location1: false,
      l2: {
        color: '#000000',
      },
      location2: false,
      l3: {
        color: '#000000',
      },
      location3: false,
      l4: {
        color: '#000000',
      },
      location4: false,
      l5: {
        color: '#000000',
      },
      location5: false,
      l6: {
        color: '#000000',
      },
      location6: false,
      l7: {
        color: '#000000',
      },
      location7: false,
      l8: {
        color: '#000000',
      },
      location8: false,
      l9: {
        color: '#000000',
      },
      location9: false,
      l10: {
        color: '#000000',
      },
      location10: false,
      l11: {
        color: '#000000',
      },
      location11: false,
      l12: {
        color: '#000000',
      },
      location12: false,

      //   isVisible: true,
    };
  },

  methods: {
    go_to_diary() {
      this.$router.push('/diary');
    },
    choose_type() {
      this.showFilter_type_window = !this.showFilter_type_window;
      this.showOverlay = !this.showOverlay;
    },
    go_to_new_diary() {
      this.$router.push('/new_diary');
    },
    choose_location() {
      this.showFilter_location_window = !this.showFilter_location_window;
      this.showOverlay = !this.showOverlay;
    },
    choose_open() {
      if (this.isOpen) {
        this.open.color = '#000000';
        this.open.background = "#FFFFFF";
        this.open.border = "1px solid #DDDDDD";
        this.isOpen = !this.isOpen;
      } else {
        this.open.color = '#BD0A0A';
        this.open.background = "#FCE8E8";
        this.open.border = "1px solid #DDDDDD";
        this.isOpen = !this.isOpen;
      }

    },

    comfirm_type() {
      this.showFilter_type_window = !this.showFilter_type_window;
      this.showOverlay = !this.showOverlay;
      this.type_list = [];
      if (this.type1) {
        this.type_list.push("中式");
      }
      if (this.type2) {
        this.type_list.push("美式");
      }
      if (this.type3) {
        this.type_list.push("日式");
      }
      if (this.type4) {
        this.type_list.push("韓式");
      }
      if (this.type5) {
        this.type_list.push("義式");
      }
      if (this.type6) {
        this.type_list.push("火鍋");
      }
      if (this.type7) {
        this.type_list.push("燒烤");
      }
      if (this.type8) {
        this.type_list.push("正餐");
      }
      if (this.type9) {
        this.type_list.push("點心");
      }
      if (this.type10) {
        this.type_list.push("酒吧");
      }
      if (this.type11) {
        this.type_list.push("飲品");
      }
      if (this.type12) {
        this.type_list.push("其他");
      }

      if (this.type_list.length > 0) {
        this.type.color = '#BD0A0A';
        this.type.background = "#FCE8E8";
        this.type.border = "1px solid #DDDDDD";

      } else {
        this.type.color = '#000000';
        this.type.background = "#FFFFFF";
        this.type.border = "1px solid #DDDDDD";
      }

      const path = "http://localhost:5000/search";

      this.restaurants = []
      axios
        .post(path, { "search_content": this.search_content, "place_list": this.place_list, "type_list": this.type_list })
        .then((res) => {
          console.log(res);

          for (var i = 0; i < res.data.items.length; i++) {
            this.restaurants.push({ id: res.data.items[i].id, rest_name: res.data.items[i].restaurant_name, location: res.data.items[i].address, rating_number: res.data.items[i].rating_num, rating: res.data.items[i].rating, contact_number: res.data.items[i].phone });
          }


        })
        .catch((error) => {
          console.log(error);
        });





    },
    comfirm_location() {
      this.showFilter_location_window = !this.showFilter_location_window;
      this.showOverlay = !this.showOverlay;
      this.place_list = [];
      if (this.location1) {
        this.place_list.push("中正區");
      }
      if (this.location2) {
        this.place_list.push("大同區");
      }
      if (this.location3) {
        this.place_list.push("中山區");
      }
      if (this.location4) {
        this.place_list.push("松山區");
      }
      if (this.location5) {
        this.place_list.push("大安區");
      }
      if (this.location6) {
        this.place_list.push("萬華區");
      }
      if (this.location7) {
        this.place_list.push("信義區");
      }
      if (this.location8) {
        this.place_list.push("士林區");
      }
      if (this.location9) {
        this.place_list.push("北投區");
      }
      if (this.location10) {
        this.place_list.push("內湖區");
      }
      if (this.location11) {
        this.place_list.push("南港區");
      }
      if (this.location12) {
        this.place_list.push("文山區");
      }

      if (this.place_list.length > 0) {
        this.location.color = '#BD0A0A';
        this.location.background = "#FCE8E8";
        this.location.border = "1px solid #DDDDDD";

      } else {
        this.location.color = '#000000';
        this.location.background = "#FFFFFF";
        this.location.border = "1px solid #DDDDDD";
      }

      const path = "http://localhost:5000/search";

      this.restaurants = []
      axios
        .post(path, { "search_content": this.search_content, "place_list": this.place_list, "type_list": this.type_list })
        .then((res) => {
          console.log(res);

          for (var i = 0; i < res.data.items.length; i++) {
            this.restaurants.push({ id: res.data.items[i].id, rest_name: res.data.items[i].restaurant_name, location: res.data.items[i].address, rating_number: res.data.items[i].rating_num, rating: res.data.items[i].rating, contact_number: res.data.items[i].phone });
          }


        })
        .catch((error) => {
          console.log(error);
        });

    },

    changeStyle_t1() {
      if (this.type1) {
        this.t1.color = '#000000';
        this.type1 = false;
        console.log(this.type1);
      } else {
        this.t1.color = '#FF0000';
        this.type1 = true;
        console.log(this.type1);
      }
    },
    changeStyle_t2() {
      if (this.type2) {
        this.t2.color = '#000000';
        this.type2 = false;
        console.log(this.type2);
      } else {
        this.t2.color = '#FF0000';
        this.type2 = true;
        console.log(this.type2);
      }
    },
    changeStyle_t3() {
      if (this.type3) {
        this.t3.color = '#000000';
        this.type3 = false;
        console.log(this.type3);
      } else {
        this.t3.color = '#FF0000';
        this.type3 = true;
        console.log(this.type3);
      }
    },
    changeStyle_t4() {
      if (this.type4) {
        this.t4.color = '#000000';
        this.type4 = false;
        console.log(this.type4);
      } else {
        this.t4.color = '#FF0000';
        this.type4 = true;
        console.log(this.type4);
      }
    },
    changeStyle_t5() {
      if (this.type5) {
        this.t5.color = '#000000';
        this.type5 = false;
        console.log(this.type5);
      } else {
        this.t5.color = '#FF0000';
        this.type5 = true;
        console.log(this.type5);
      }
    },
    changeStyle_t6() {
      if (this.type6) {
        this.t6.color = '#000000';
        this.type6 = false;
        console.log(this.type6);
      } else {
        this.t6.color = '#FF0000';
        this.type6 = true;
        console.log(this.type6);
      }
    },
    changeStyle_t7() {
      if (this.type7) {
        this.t7.color = '#000000';
        this.type7 = false;
        console.log(this.type7);
      } else {
        this.t7.color = '#FF0000';
        this.type7 = true;
        console.log(this.type7);
      }
    },
    changeStyle_t8() {
      if (this.type8) {
        this.t8.color = '#000000';
        this.type8 = false;
        console.log(this.type8);
      } else {
        this.t8.color = '#FF0000';
        this.type8 = true;
        console.log(this.type8);
      }
    },
    changeStyle_t9() {
      if (this.type9) {
        this.t9.color = '#000000';
        this.type9 = false;
        console.log(this.type9);
      } else {
        this.t9.color = '#FF0000';
        this.type9 = true;
        console.log(this.type9);
      }
    },
    changeStyle_t10() {
      if (this.type10) {
        this.t10.color = '#000000';
        this.type10 = false;
        console.log(this.type10);
      } else {
        this.t10.color = '#FF0000';
        this.type10 = true;
        console.log(this.type10);
      }
    },
    changeStyle_t11() {
      if (this.type11) {
        this.t11.color = '#000000';
        this.type11 = false;
        console.log(this.type11);
      } else {
        this.t11.color = '#FF0000';
        this.type11 = true;
        console.log(this.type11);
      }
    },
    changeStyle_t12() {
      if (this.type12) {
        this.t12.color = '#000000';
        this.type12 = false;
        console.log(this.type12);
      } else {
        this.t12.color = '#FF0000';
        this.type12 = true;
        console.log(this.type12);
      }
    },

    changeStyle_l1() {
      if (this.location1) {
        this.l1.color = '#000000';
        this.location1 = false;
        console.log(this.location1);
      } else {
        this.l1.color = '#FF0000';
        this.location1 = true;
        console.log(this.location1);
      }
    },
    changeStyle_l2() {
      if (this.location2) {
        this.l2.color = '#000000';
        this.location2 = false;
        console.log(this.location2);
      } else {
        this.l2.color = '#FF0000';
        this.location2 = true;
        console.log(this.location2);
      }
    },
    changeStyle_l3() {
      if (this.location3) {
        this.l3.color = '#000000';
        this.location3 = false;
        console.log(this.location3);
      } else {
        this.l3.color = '#FF0000';
        this.location3 = true;
        console.log(this.location3);
      }
    },
    changeStyle_l4() {
      if (this.location4) {
        this.l4.color = '#000000';
        this.location4 = false;
        console.log(this.location4);
      } else {
        this.l4.color = '#FF0000';
        this.location4 = true;
        console.log(this.location4);
      }
    },
    changeStyle_l5() {
      if (this.location5) {
        this.l5.color = '#000000';
        this.location5 = false;
        console.log(this.location5);
      } else {
        this.l5.color = '#FF0000';
        this.location5 = true;
        console.log(this.location5);
      }
    },
    changeStyle_l6() {
      if (this.location6) {
        this.l6.color = '#000000';
        this.location6 = false;
        console.log(this.location6);
      } else {
        this.l6.color = '#FF0000';
        this.location6 = true;
        console.log(this.location6);
      }
    },
    changeStyle_l7() {
      if (this.location7) {
        this.l7.color = '#000000';
        this.location7 = false;
        console.log(this.location7);
      } else {
        this.l7.color = '#FF0000';
        this.location7 = true;
        console.log(this.location7);
      }
    },
    changeStyle_l8() {
      if (this.location8) {
        this.l8.color = '#000000';
        this.location8 = false;
        console.log(this.location8);
      } else {
        this.l8.color = '#FF0000';
        this.location8 = true;
        console.log(this.location8);
      }
    },
    changeStyle_l9() {
      if (this.location9) {
        this.l9.color = '#000000';
        this.location9 = false;
        console.log(this.location9);
      } else {
        this.l9.color = '#FF0000';
        this.location9 = true;
        console.log(this.location9);
      }
    },
    changeStyle_l10() {
      if (this.location10) {
        this.l10.color = '#000000';
        this.location10 = false;
        console.log(this.location10);
      } else {
        this.l10.color = '#FF0000';
        this.location10 = true;
        console.log(this.location10);
      }
    },
    changeStyle_l11() {
      if (this.location11) {
        this.l11.color = '#000000';
        this.location11 = false;
        console.log(this.location11);
      } else {
        this.l11.color = '#FF0000';
        this.location11 = true;
        console.log(this.location11);
      }
    },
    changeStyle_l12() {
      if (this.location12) {
        this.l12.color = '#000000';
        this.location12 = false;
        console.log(this.location12);
      } else {
        this.l12.color = '#FF0000';
        this.location12 = true;
        console.log(this.location12);
      }
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

.overlay {
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: rgba(59, 56, 56, 0.5);
  z-index: 5;
}


.filter_type_window {
  position: absolute;
  z-index: 10;
  width: 393px;
  height: 302px;
  top: 553px;
  background: #FFFFFF;
  /* background: #ddd; */
  border-radius: 10px 10px 25px 25px;
}

.filter_type_window .title {
  position: absolute;
  width: 40px;
  height: 24px;
  left: 28px;
  top: 25px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
}

.filter_type_window .type1 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 82px;
  top: 99px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type2 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 144px;
  top: 99px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type3 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 206px;
  top: 99px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type4 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 268px;
  top: 99px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}


.filter_type_window .type5 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 82px;
  top: 132px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type6 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 144px;
  top: 132px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type7 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 206px;
  top: 132px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type8 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 268px;
  top: 132px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type9 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 82px;
  top: 165px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type10 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 144px;
  top: 165px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type11 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 206px;
  top: 165px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}

.filter_type_window .type12 {
  position: absolute;
  /* width: 28px; */
  height: 17px;
  left: 268px;
  top: 165px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  /* color: #000000; */
}


.filter_type_window .clear_btn {
  position: absolute;
  left: 80px;
  top: 246px;
  background: #555555;
  border-radius: 5px;
  padding: 9px 40px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  color: #FFFFFF;
}

.filter_type_window .comfirm_btn {
  position: absolute;
  right: 80px;
  top: 246px;
  background: #BD0A0A;
  border-radius: 5px;
  padding: 9px 40px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 17px;
  text-align: center;
  color: #FFFFFF;
}
</style>