<template>
	<view class="content">
		<view >
			<image class="top" src="../../static/1730683558696.jpg" mode=""></image>
		</view>
		
		<view class="main">
			<view class="emailBox">
				邮箱
				<input type="text" class="emailInput" v-model="myEmail">
			</view>
			<view class="emailBox">
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
			<view class="emailBox">
				密码
				<input type="text" v-if="showPassword" class="emailInput" v-model="myPassword">
				<input type="password" v-if="!showPassword" class="emailInput" v-model="myPassword">
				<image class="eyeButton" src="../../static/yanjing.png" @click="changePassword"></image>
			</view>
			<view class="warningBox">
				<image class="warnImg" src="../../static/vuesax_linear_warning-2.png" mode=""></image>
				<span>密码为8-20个字母、数字或ascii字符</span>
			</view>
			<view class="emailBox">
				<view class="specal">
				确认
				<br />
				密码	
				</view>
				<input type="text" v-if="showPassword1" class="emailInput" v-model="myPassword1">
				<input type="password" v-if="!showPassword1" class="emailInput" v-model="myPassword1">
				<image class="eyeButton" src="../../static/yanjing.png" @click="changePassword1"></image>
			</view>
			
			<view class="loginButton">
				登录
			</view>
			<view class="changeLogin" @click="toLogin">
				已有帐号
			</view>
		</view>
	</view>
</template>


<script>
	export default {
		data(){
			return{
				myEmail:'',
				myCode:'',
				myPassword:'',
				showPassword:false,
				myPassword1:'',
				showPassword1:false,
				isCode:true,
				itTime:60
			}
		}
		
		,methods:{
			changePassword() {
				this.showPassword = !this.showPassword
			
			},
			changePassword1() {
				this.showPassword1 = !this.showPassword1
			
			},
			toLogin(){
				uni.navigateTo({
					url: 'login'
				});
			}
			,getCode(){
				this.isCode = !this.isCode
					if (!this.isCode) {
						const a = setInterval(() => {
							this.itTime--;
							if (this.itTime == 0) {
								this.isCode = false;
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
	.eyeButton {
		position: absolute;
		width: 50rpx;
		height: 50rpx;
		right: 120rpx;
		margin-top: 15rpx;
		z-index: 100;
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
	.main {
		background-color: rgba(251, 249, 236, 1);;
		width: 750rpx;
		height: 61vh;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 3vh;
	}
	.top{
		width: 750rpx;
		height: 36vh;
	}
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	
</style>