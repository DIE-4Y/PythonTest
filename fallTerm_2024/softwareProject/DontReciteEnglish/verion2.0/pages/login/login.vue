<template>
	<view class="content">
		<image class="top" src="https://img.js.design/assets/img/670f0ac148e0a84364903058.png#229f0ccc05fb055d575bae5a7397b95e"></image>
		<image class="top2" src="https://img.js.design/assets/img/670f0ac148e0a84364903058.png#229f0ccc05fb055d575bae5a7397b95e"></image>
		<view class="main" >
			<view class="emailBox">
				邮箱
				<input type="text" class="emailInput" v-model="myEmail">
			</view>
			<view class="emailBox" v-if="isPassword">
				密码
				<input type="text" v-if="showPassword" class="emailInput" v-model="myPassword">
				<input type="password" v-if="!showPassword" class="emailInput" v-model="myPassword">
				<image class="eyeButton" src="../../static/yanjing.png" @click="changePassword"></image>
			</view>
			<view class="warningBox" v-if="isPassword">
				<image class="warnImg" src="../../static/vuesax_linear_warning-2.png" mode=""></image>
				<span>密码为8-20个字母、数字或ascii字符</span>
			</view>
			
			<view class="emailBox" v-if="!isPassword">
				<view class="specal">
				验证
				<br />
				码	
				</view>
				<input type="text"  class="emailInput" v-model="myCode">
				<view class="codeButton" >
					<span v-if="isCode"@click="getCode">获得验证码</span>
					<span v-if="!isCode">{{itTime}}s后重新发送</span>
				</view>
				
			</view>
			
			
			<view class="functionBox">
				
				<span @click="toEnroll">注册新账号</span>
				<span @click="toForget">忘记密码</span>
			</view>
			<view class="loginButton" @click="toindex">
				登录
			</view>
			<view class="changeLogin" >
				<span v-if="isPassword"@click="changeLogin"> 验证码登录</span>
				<span v-if="!isPassword" @click="changeLogin">密码登录</span>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				myPassword:'',
				myEmail: '',
				showPassword: false,
				isPassword:true,
				isCode:true,
				itTime:60,
				myCode:'',
			}
		},
		onLoad() {

		},
		methods: {
			changePassword() {
				this.showPassword = !this.showPassword
				console.log(this.showPassword)
			}
			,
			toEnroll(){
				
				uni.navigateTo({
					url: 'enroll'
				});

			},
			toindex(){
				
				uni.reLaunch({
					url: '../index/study'
				});
			
			},
			toForget(){
				uni.navigateTo({
					url: 'forgetPassword1'
				});
			}
			,changeLogin()
			{
				this.isPassword = !this.isPassword
			},getCode(){
				this.isCode = !this.isCode
					if (!this.isCode) {
						const a = setInterval(() => {
							this.itTime--;
							if (this.itTime == 0) {
								this.isCode = true;
								this.itTime = 60
								clearInterval(a)
							}
						}, 1000)
					}
			
			}
		}
	}
</script>

<style>
	.codeButton{
		position: absolute;
		width: 200rpx;
		text-align: center;
		height: 4vh;
		right: 120rpx;
		margin-top: 10rpx;
		line-height: 4vh;
		border-radius: 30rpx;
		z-index: 100;
		background-color: rgba(169, 212, 198, 1);
		font-size: 28rpx;
	}
	.specal{
		line-height: 2.5vh;
		text-align: center;
	}
	.changeLogin{
		font-size: 40rpx;
		margin-top: 2vh;
		color:rgba(237, 174, 141, 1);
		
		
	}	
	.loginButton{
		background: rgba(123, 180, 178, 1);
		width: 360rpx;
		height: 80rpx;
		border-radius: 40rpx;
		font-size: 40rpx;
		text-align: center;
		line-height: 80rpx;
	}
	.functionBox{
		margin:2vh 0;
		width: 600rpx;
		height: 4vh;
		line-height: 4vh;
		color:rgba(237, 174, 141, 1);
		display: flex;
		justify-content: space-between;
	}
	.warnImg{
		width: 30rpx;
		height: 30rpx;
		margin-right: 20rpx ;
	}
	.warningBox{
		width: 600rpx;
		height: 2vh;
		line-height: 2vh;
		font-size: 23rpx;
		display: flex;
		color: rgba(80,80,80,0.7);
	}
	.emailInput {
		background-color: white;
		width: 450rpx;
		border: 4rpx solid rgba(243, 215, 185, 1);
		height: 4.7vh;
		margin-left: 30rpx;
		border-radius: 50rpx;
		padding-left: 20rpx;
	}

	.eyeButton {
		position: absolute;
		width: 50rpx;
		height: 50rpx;
		right: 120rpx;
		margin-top: 15rpx;
		z-index: 100;
	}

	.passwordBox {
		width: 600rpx;
		height: 5vh;
		line-height: 5vh;
		font-size: 36rpx;
		display: flex;
		position: relative;
	}

	.emailBox {
		width: 600rpx;
		height: 5vh;
		line-height: 5vh;
		font-size: 36rpx;
		margin: 2vh 0;
		display: flex;
	}

	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.top {
		height: 23vh;
		width: 750rpx;
		position: absolute;
		top: 0;
	}

	.top2 {
		height: 23vh;
		width: 750rpx;
		position: absolute;
		top: 23vh;
		opacity: 0.5;
		-moz-transform: scaleY(-1);
		-webkit-transform: scaleY(-1);
		-o-transform: scaleY(-1);
		transform: scaleY(-1);
		z-index: -1;
	}

	.main {
		margin-top: 36vh;
		background-color: rgba(251, 249, 236, 1);
		;
		width: 750rpx;
		height: 64vh;
		border-radius: 100rpx;

		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 3vh;
	}
</style>