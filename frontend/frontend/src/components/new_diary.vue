<template>
  <div>

    <div class="phone">
      <div class="screen"> </div><img class="close" src="https://i.postimg.cc/fb8jgLWs/close.png" alt="" />
      <div class="title">新日記</div>
      <div class="add_rest">
        <div class="rest_title">餐廳</div>
        <input type="text" placeholder="" v-model="restaurant" /><img class="rest_icon"
          src="https://i.postimg.cc/zv7g32Lr/location.png" alt="" />
        <source />
      </div>
      <div class="add_date">
        <div class="date_title">用餐日期</div>
        <input type="date" placeholder="" v-model="date" />
      </div>
      <div class="add_pic">
        <div class="pic_title">新增照片</div>
        <div class="border"></div>
        <label class="custom-file-upload" for="file-upload"><img class="rest_icon"
            src="https://i.postimg.cc/QdwX8xDK/plus-icon.png" alt="" /></label>
        <input id="file-upload" type="file" accept="image/*" />
      </div>
      <div class="add_text">
        <div class="text_title">新增文字</div>
        <input type="text" placeholder="" v-model="text" />
      </div>
      <div class="post_btn" @click="post_diary">發布</div>
    </div>
    <h2 class="phonename">iphone14 pro</h2>

  </div>
</template>



<script>
export default {
  name: 'TastyExplorer_test',
  data() {
    return {
      restaurant: "",
      date: "",
      text: "",



      //   isVisible: true,
    };
  },
  mounted() {

  },
  beforeUnmount() {

  },
  methods: {
    post_diary() {
      const diary_info = { user_id: 1, photo: "test4.jpg", content: this.text, restaurant_name: this.restaurant, post_time: this.date };
      const path = "http://localhost:5000/diary_post";
      axios
        // post 過去的東西要包大括號 {}
        .post(path, diary_info)
        .then((res) => {
          console.log(res.data);
          this.success = res.data.status;
          // console.log(res.data.diary);
          this.$router.go(-1);

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

.close {
  position: absolute;
  width: 37.55px;
  height: 37.55px;
  left: 21px;
  top: 15px;
}

.title {
  position: absolute;
  width: 88px;
  height: 29px;
  left: 76px;
  top: 20px;
  font-family: "Inter";
  font-style: normal;
  font-weight: 700;
  font-size: 24px;
  line-height: 29px;
  color: #000000;
}

.add_rest {
  position: absolute;
  width: 304px;
  height: 55px;
  left: 40px;
  top: 78px;
}

.add_rest .rest_title {
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
}

.add_rest input {
  position: absolute;
  width: 234px;
  height: 55px;
  top: 39px;
  border: 1px solid #C7C2C2;
  border-radius: 14px;
  padding-left: 70px;
}

.add_rest .rest_icon {
  position: absolute;
  top: 52px;
  left: 20px;
}

.add_date {
  position: absolute;
  width: 304px;
  height: 55px;
  left: 40px;
  top: 187px;
}

.add_date .date_title {
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
}

.add_date input {
  position: absolute;
  width: 264px;
  height: 55px;
  top: 39px;
  border: 1px solid #C7C2C2;
  border-radius: 14px;
  padding: 0 20px;
}

.add_pic {
  position: absolute;
  width: 304px;
  height: 240px;
  left: 44px;
  top: 296px;
}

.add_pic .pic_title {
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
}

.add_pic .border {
  position: absolute;
  width: 304px;
  height: 201px;
  top: 39px;
  background: #FFFFFF;
  border: 1px solid #C7C2C2;
  border-radius: 14px;
}

.add_pic input {
  position: absolute;
  width: 304px;
  height: 201px;
  top: 39px;
  opacity: 0;
}

.add_pic .custom-file-upload {
  position: absolute;
  top: 90px;
  left: 92px;
  display: inline-block;
  padding: 10px 20px;
  cursor: pointer;
  color: #333;
  border-radius: 4px;
}

.add_text {
  position: absolute;
  width: 304px;
  height: 55px;
  left: 40px;
  top: 551px;
}

.add_text .text_title {
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
}

.add_text input {
  position: absolute;
  width: 264px;
  height: 181px;
  top: 39px;
  border: 1px solid #C7C2C2;
  border-radius: 14px;
  padding: 0 20px;
}

.post_btn {
  position: absolute;
  width: 214px;
  height: 35px;
  left: 90px;
  top: 784px;
  background: #B82C30;
  border-radius: 5px;
  font-family: "Noto Sans TC";
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 180%;
  align-items: center;
  text-align: center;
  letter-spacing: 1.25px;
  padding-top: 10px;
  color: #FFFFFF;
}
</style>