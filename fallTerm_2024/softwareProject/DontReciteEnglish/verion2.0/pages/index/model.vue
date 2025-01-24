<template>
	<view class="container">
		<view class="topBg">
			<image src="https://img.js.design/assets/img/671cffc990fc07a8da43ec7c.jpg#fc357197778f7760060b62a137b68ebb" mode=""></image>
		</view>
		<view class="bottomBg">
			<image src="https://img.js.design/assets/img/670f8ca1ed2df1560d409f09.png#25827d3ab0c051ba607ef846a376d359" mode=""></image>
		</view>
		<view class="sc">
			<image class="topImage" src="https://img.js.design/assets/img/6737405d18248c27bda31d13.png#208841e594dc87f74c5fba4bc690c1c4" mode=""></image>
			<image class="topImage" src="https://img.js.design/assets/img/65881b0fd0fb78b349b079e6.png#068f9e968604978090cbfb50354c5f4d" mode=""></image>
		</view>
		<view class="myBar">
			<view class="barBox" @click="to1">
				<image src="https://img.js.design/assets/img/6604e417f9f1cdd5be504e11.png#7a43d90be656d019e8e86c5acd2236b6" mode=""></image>
			</view>
			<view class="barBox" @click="to2">
				<image src="https://img.js.design/assets/img/673741058044d4311c67e4fe.png#a6d41878d07d093fbff6622f8d03b7ff" mode=""></image>
				
			</view>
			<view class="barBox" @click="to3">
				<image src="https://img.js.design/assets/img/6655b5faae88185aee885db4.png#57f61690b7bfd828e562b1e2ee5521cd" mode=""></image>
			</view>
		</view>
		
		
		<view class="main">
			
			
			
		</view>
	</view>
</template>

<script>
	export default {
		
		data(){
			return{
			
			}
		},
		
		methods:{
			to1(){
				uni.reLaunch({
					url: 'study'
				});
			}
			,
			to2(){
				uni.reLaunch({
					url: 'search'
				});
			}
			,
			to3(){
				uni.reLaunch({
					url: 'myself'
				});
			}
			
	}}
	
</script>

<style>
	
	.barBox{
		margin-top: 5rpx;
		height: 45rpx;
		width: 45rpx;
	}
	.barBox image{
		height: 45rpx;
		width: 45rpx;
	}
	.myBar{
		position: absolute;
		margin-left: 50rpx;
		width: 650rpx;
		height: 55rpx;
		display: flex;
		justify-content: space-between;
		bottom: 35rpx;
		z-index: 5;
	}
	.main{
		position: relative;
		margin-top: 330rpx;
		width: 750rpx;
		height: 1215rpx;
		border-radius: 80rpx;
		background-color: antiquewhite;
		z-index: 2;
		overflow: hidden;
	}
	.topImage{
		margin: 20rpx 30rpx;
		width: 50rpx;
		height: 50rpx;
		
	}
	.bottomBg image{
		margin-left: 40rpx;
		width: 680rpx;
		height: 130rpx;
		z-index: 1;
		transform: scale(1.2);
		
	}
	.bottomBg{
		width: 750rpx;
		height: 150rpx;
		position: absolute;
		bottom: 0rpx;
		z-index: 3;
		
	}
	.sc{
		position: absolute;
		width: 750rpx;
		height: 100rpx;
		z-index: 2;
		display: flex;
		justify-content: space-between;
	}
	.topBg{
		width: 750rpx;
		height: 900rpx;
		position: absolute;
		top: 0;
		z-index: 1;
	}
	.topBg image{
		width: 750rpx;
		height: 1100rpx;
		transform: translate(0rpx, -470rpx);
		z-index: 1;
	}
	.container{
		width: 750rpx;
		height: 1445rpx;
		position: relative;
		overflow: hidden;
		z-index: 1;
	}
</style>