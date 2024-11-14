---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
创建计分板
trigger类型 ^cUlB1Cea

将计分板属性赋予玩家 ^p5ahn3rA

玩家达到计分板数值 ^lcKxsCqT

TP ^LWRNj2MQ

清除玩家计分板数值 ^xohwt5cf

execute指令循环使得达到数值的玩家TP ^QStV3daw

创建计分板trigger类型
/scoreboard objectives add 设置的计分板名称 trigger ^LhjDGdk1

将计分板属性赋予玩家
/scoreboard players enable @a 设置的计分板名称 ^kvvyFvXG

玩家达到计分板数值
/trigger 计分板名称 add 增加的数值
/trigger 计分板名称  （该命令为直接增加1） ^JUWEvGlr

TP ^D1JA760W

清除玩家计分板数值
/scoreboard players reset @a 计分板名称 ^GGvdMDVe

execute指令循环使得达到数值的玩家TP
/execute as @a[scores={设置的计分板名称=1}] at @s run tp 1_player ^xQ26bjp7

将计分板属性赋予玩家
/scoreboard players enable @a 设置的计分板名称 ^iWNwdf60

玩家达到计分板数值
/trigger 计分板名称 add 增加的数值
/trigger 计分板名称  （该命令为直接增加1） ^J2Jy074Z

TP ^tGs4rubZ

execute指令循环使得达到数值的玩家TP
/execute as @a[scores={设置的计分板名称=1}] at @s run tp 1_player ^20CS3DZx

清除玩家计分板数值
/scoreboard players reset @a 计分板名称 ^O2Lqw58e

创建计分板trigger类型
/scoreboard objectives add 设置的计分板名称 trigger ^TKzjJSxU

新玩家 ^0UvN8Dof

手动 ^wTXXSBbn

自动 ^LSgmnL7h

命令方块拉杆或者给予出生带你附近的人指令
/scoreboard players enable @p 计分板名称
/scoreboard players enable @p[distance=..2] 计分板名称
 ^1zAspqkw

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.25",
	"elements": [
		{
			"type": "rectangle",
			"version": 178,
			"versionNonce": 683740080,
			"isDeleted": false,
			"id": "0jTM3oHunVZPAp_dMuhXJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -266.9494323730469,
			"y": 263.2122116088867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 129.3233642578125,
			"height": 60,
			"seed": 1265528597,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "cUlB1Cea"
				},
				{
					"id": "3MHs1ejGJs1Pxk11kmovS",
					"type": "arrow"
				}
			],
			"updated": 1698846617089,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 228,
			"versionNonce": 141215568,
			"isDeleted": false,
			"id": "cUlB1Cea",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -254.21771240234375,
			"y": 268.2122116088867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 103.85992431640625,
			"height": 50,
			"seed": 921098677,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617089,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "创建计分板\ntrigger类型",
			"rawText": "创建计分板\ntrigger类型",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "0jTM3oHunVZPAp_dMuhXJ",
			"originalText": "创建计分板\ntrigger类型",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 319,
			"versionNonce": 1172856523,
			"isDeleted": false,
			"id": "3MHs1ejGJs1Pxk11kmovS",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -133.82241821289062,
			"y": 293.92426261660415,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 76.07257080078124,
			"height": 1.3200616469696342,
			"seed": 596501877,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127503,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "0jTM3oHunVZPAp_dMuhXJ",
				"gap": 3.80364990234375,
				"focus": 0.061053073355775776
			},
			"endBinding": {
				"elementId": "eD2UMLgrdQPRNX7rv_0Ns",
				"gap": 2.28216552734375,
				"focus": 0.08927920352215386
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					76.07257080078124,
					-1.3200616469696342
				]
			]
		},
		{
			"type": "rectangle",
			"version": 214,
			"versionNonce": 1144347984,
			"isDeleted": false,
			"id": "eD2UMLgrdQPRNX7rv_0Ns",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -55.467681884765625,
			"y": 268.53731536865234,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 235.06427001953125,
			"height": 48.686431884765625,
			"seed": 848760629,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "3MHs1ejGJs1Pxk11kmovS",
					"type": "arrow"
				}
			],
			"updated": 1698846617089,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 208,
			"versionNonce": 1247141808,
			"isDeleted": false,
			"id": "p5ahn3rA",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -38.960601806640625,
			"y": 281.9268264770508,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 200,
			"height": 25,
			"seed": 1633762267,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "xW_lfJUvbIMOhLNfnzD8R",
					"type": "arrow"
				}
			],
			"updated": 1698846617089,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "将计分板属性赋予玩家",
			"rawText": "将计分板属性赋予玩家",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "将计分板属性赋予玩家",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 137,
			"versionNonce": 373109584,
			"isDeleted": false,
			"id": "xW_lfJUvbIMOhLNfnzD8R",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 58.641265869140625,
			"y": 317.9844741821289,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.04290771484375,
			"height": 98.13363647460938,
			"seed": 2101632885,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1698846617089,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "p5ahn3rA",
				"focus": 0.031165234774596887,
				"gap": 11.057647705078125
			},
			"endBinding": {
				"elementId": "hhOL7Fk__wU6NvLoPAQAp",
				"focus": -0.17242214636644781,
				"gap": 2.282135009765625
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					3.04290771484375,
					98.13363647460938
				]
			]
		},
		{
			"type": "rectangle",
			"version": 185,
			"versionNonce": 1574857136,
			"isDeleted": false,
			"id": "hhOL7Fk__wU6NvLoPAQAp",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -34.928009033203125,
			"y": 418.4002456665039,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 235.824951171875,
			"height": 49.447174072265625,
			"seed": 1511612827,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "xW_lfJUvbIMOhLNfnzD8R",
					"type": "arrow"
				}
			],
			"updated": 1698846617089,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 162,
			"versionNonce": 1155156304,
			"isDeleted": false,
			"id": "lcKxsCqT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -5.303924560546875,
			"y": 435.6627883911133,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 180,
			"height": 25,
			"seed": 1769650997,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Bx4JK3cdOXC9my2gu6YoS",
					"type": "arrow"
				}
			],
			"updated": 1698846617089,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "玩家达到计分板数值",
			"rawText": "玩家达到计分板数值",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "玩家达到计分板数值",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "diamond",
			"version": 192,
			"versionNonce": 1137030064,
			"isDeleted": false,
			"id": "E-YOVyub3Y6yxG43kLrjL",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -3.738311767578125,
			"y": 540.8771133422852,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 146.05938720703125,
			"height": 120,
			"seed": 706878459,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "LWRNj2MQ"
				},
				{
					"id": "Bx4JK3cdOXC9my2gu6YoS",
					"type": "arrow"
				}
			],
			"updated": 1698846617089,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 194,
			"versionNonce": 191143760,
			"isDeleted": false,
			"id": "LWRNj2MQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 54.626548767089844,
			"y": 588.3771133422852,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 29.299972534179688,
			"height": 25,
			"seed": 226211189,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "TP",
			"rawText": "TP",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "E-YOVyub3Y6yxG43kLrjL",
			"originalText": "TP",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 178,
			"versionNonce": 313616395,
			"isDeleted": false,
			"id": "Bx4JK3cdOXC9my2gu6YoS",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 67.76992797851562,
			"y": 468.60816192626953,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.7537576019024357,
			"height": 71.60546031134436,
			"seed": 906181531,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127509,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "lcKxsCqT",
				"gap": 7.94537353515625,
				"focus": 0.190181578255424
			},
			"endBinding": {
				"elementId": "E-YOVyub3Y6yxG43kLrjL",
				"gap": 1,
				"focus": -0.0017680439605050014
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0.7537576019024357,
					71.60546031134436
				]
			]
		},
		{
			"type": "rectangle",
			"version": 210,
			"versionNonce": 2050241872,
			"isDeleted": false,
			"id": "Ce23FtWqVCzgSoKmHtpzv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -322.4823913574219,
			"y": 416.8788528442383,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 242.67150878906253,
			"height": 60,
			"seed": 289127515,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "xohwt5cf"
				},
				{
					"id": "8edqEm-lp70sQEBLKGn_8",
					"type": "arrow"
				},
				{
					"id": "qqyjs6D57bP34W_RBDPnY",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 216,
			"versionNonce": 441485232,
			"isDeleted": false,
			"id": "xohwt5cf",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -291.1466369628906,
			"y": 434.3788528442383,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 180,
			"height": 25,
			"seed": 1227235579,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "清除玩家计分板数值",
			"rawText": "清除玩家计分板数值",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Ce23FtWqVCzgSoKmHtpzv",
			"originalText": "清除玩家计分板数值",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 138,
			"versionNonce": 2147364523,
			"isDeleted": false,
			"id": "8edqEm-lp70sQEBLKGn_8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3.868988037109375,
			"y": 602.4959182739258,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 137.69134521484375,
			"height": 120.19467163085938,
			"seed": 311171323,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127513,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "Ce23FtWqVCzgSoKmHtpzv",
				"gap": 5.422393798828125,
				"focus": -0.17177250917234602
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-137.69134521484375,
					-120.19467163085938
				]
			]
		},
		{
			"type": "arrow",
			"version": 118,
			"versionNonce": 1094263115,
			"isDeleted": false,
			"id": "qqyjs6D57bP34W_RBDPnY",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -77.52865600585938,
			"y": 438.93985748291016,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 49.4471435546875,
			"height": 0,
			"seed": 919054613,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127513,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Ce23FtWqVCzgSoKmHtpzv",
				"gap": 2.282226562499986,
				"focus": -0.2646331787109375
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					49.4471435546875,
					0
				]
			]
		},
		{
			"type": "rectangle",
			"version": 242,
			"versionNonce": 2063802704,
			"isDeleted": false,
			"id": "EHewM02P7coEQGyVFtFNj",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -130.77944946289062,
			"y": 702.1508865356445,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 396.3380737304688,
			"height": 69.98675537109375,
			"seed": 295795003,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "QStV3daw"
				},
				{
					"id": "WnbBmumi71YgralLYuNpj",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 330,
			"versionNonce": 53894064,
			"isDeleted": false,
			"id": "QStV3daw",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -115.64035034179685,
			"y": 724.6442642211914,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 366.05987548828125,
			"height": 25,
			"seed": 946001883,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "execute指令循环使得达到数值的玩家TP",
			"rawText": "execute指令循环使得达到数值的玩家TP",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "EHewM02P7coEQGyVFtFNj",
			"originalText": "execute指令循环使得达到数值的玩家TP",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 160,
			"versionNonce": 264028139,
			"isDeleted": false,
			"id": "WnbBmumi71YgralLYuNpj",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 71.50776540622334,
			"y": 701.1508865356445,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.6949297128639671,
			"height": 41.60052490234375,
			"seed": 556818645,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127518,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "EHewM02P7coEQGyVFtFNj",
				"gap": 1,
				"focus": 0.02374518692984845
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-0.6949297128639671,
					-41.60052490234375
				]
			]
		},
		{
			"type": "rectangle",
			"version": 434,
			"versionNonce": 491742640,
			"isDeleted": false,
			"id": "d9Zf8b57IHTi3UubJ4si3",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 525.309905322423,
			"y": 238.33504304068055,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 527.9036094263981,
			"height": 85,
			"seed": 384630459,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "LhjDGdk1"
				},
				{
					"id": "AyNZgM5NIs1cBvIymcSm2",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 698,
			"versionNonce": 772214096,
			"isDeleted": false,
			"id": "LhjDGdk1",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 532.8818577407002,
			"y": 255.83504304068055,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 512.7597045898438,
			"height": 50,
			"seed": 1609789275,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "创建计分板trigger类型\n/scoreboard objectives add 设置的计分板名称 trigger",
			"rawText": "创建计分板trigger类型\n/scoreboard objectives add 设置的计分板名称 trigger",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "d9Zf8b57IHTi3UubJ4si3",
			"originalText": "创建计分板trigger类型\n/scoreboard objectives add 设置的计分板名称 trigger",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 1139,
			"versionNonce": 1467482411,
			"isDeleted": false,
			"id": "AyNZgM5NIs1cBvIymcSm2",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1057.0171646511649,
			"y": 277.1747192965576,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 51.1813600378498,
			"height": 1.253694485540052,
			"seed": 1814219771,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127522,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "d9Zf8b57IHTi3UubJ4si3",
				"gap": 3.8036499023438637,
				"focus": 0.064033457138755
			},
			"endBinding": {
				"elementId": "FhKIwoAdj4-BN_i86qkH3",
				"gap": 2.282165527343693,
				"focus": 0.0892792035221558
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					51.1813600378498,
					-1.253694485540052
				]
			]
		},
		{
			"type": "rectangle",
			"version": 395,
			"versionNonce": 978903888,
			"isDeleted": false,
			"id": "FhKIwoAdj4-BN_i86qkH3",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1110.4806902163587,
			"y": 224.92149718883462,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 520.1361630088406,
			"height": 99.13459055047282,
			"seed": 1065194651,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "AyNZgM5NIs1cBvIymcSm2",
					"type": "arrow"
				},
				{
					"id": "b2l9AEPHutN12KTiRIXZk",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 375,
			"versionNonce": 1586870704,
			"isDeleted": false,
			"id": "kvvyFvXG",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1141.881946041468,
			"y": 248.72097180463436,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 473.73974609375,
			"height": 50,
			"seed": 968247611,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "LPqfK72ju9gaYbdr6YCVV",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "将计分板属性赋予玩家\n/scoreboard players enable @a 设置的计分板名称",
			"rawText": "将计分板属性赋予玩家\n/scoreboard players enable @a 设置的计分板名称",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "将计分板属性赋予玩家\n/scoreboard players enable @a 设置的计分板名称",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 711,
			"versionNonce": 1241512272,
			"isDeleted": false,
			"id": "LPqfK72ju9gaYbdr6YCVV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1368.2173502847315,
			"y": 309.7786195097125,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.26020386574055,
			"height": 128.8989717537993,
			"seed": 539978203,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "kvvyFvXG",
				"gap": 11.057647705078125,
				"focus": 0.031165234774596887
			},
			"endBinding": {
				"elementId": "-A_04VBf98azsjcm_mCp2",
				"gap": 2.282135009765625,
				"focus": -0.17242214636644781
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-10.26020386574055,
					128.8989717537993
				]
			]
		},
		{
			"type": "rectangle",
			"version": 336,
			"versionNonce": 1360200624,
			"isDeleted": false,
			"id": "-A_04VBf98azsjcm_mCp2",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1145.77658617306,
			"y": 440.9597262732774,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 504.84244113035606,
			"height": 94.13982391357423,
			"seed": 1744533115,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "LPqfK72ju9gaYbdr6YCVV",
					"type": "arrow"
				},
				{
					"id": "tLW1v-4Ha_VY3SIA8A1fA",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 497,
			"versionNonce": 1079267152,
			"isDeleted": false,
			"id": "JUWEvGlr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1153.7575062287344,
			"y": 454.1152417825402,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 409.2799072265625,
			"height": 75,
			"seed": 1071443739,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "tLW1v-4Ha_VY3SIA8A1fA",
					"type": "arrow"
				},
				{
					"id": "2srzRkpeHi_7rxlBuNtKI",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "玩家达到计分板数值\n/trigger 计分板名称 add 增加的数值\n/trigger 计分板名称  （该命令为直接增加1）",
			"rawText": "玩家达到计分板数值\n/trigger 计分板名称 add 增加的数值\n/trigger 计分板名称  （该命令为直接增加1）",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "玩家达到计分板数值\n/trigger 计分板名称 add 增加的数值\n/trigger 计分板名称  （该命令为直接增加1）",
			"lineHeight": 1.25,
			"baseline": 67
		},
		{
			"type": "diamond",
			"version": 253,
			"versionNonce": 1498877360,
			"isDeleted": false,
			"id": "rQzIY3_rrMVi6NhI9ALeZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 984.9209164533377,
			"y": 524.4873115584378,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 146.05938720703125,
			"height": 120,
			"seed": 1514558395,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "D1JA760W"
				},
				{
					"id": "tLW1v-4Ha_VY3SIA8A1fA",
					"type": "arrow"
				},
				{
					"id": "MUlq1bErNp7J4316yMxLH",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 253,
			"versionNonce": 1437459792,
			"isDeleted": false,
			"id": "D1JA760W",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1043.2857769880056,
			"y": 571.9873115584378,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 29.299972534179688,
			"height": 25,
			"seed": 2002396251,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "TP",
			"rawText": "TP",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "rQzIY3_rrMVi6NhI9ALeZ",
			"originalText": "TP",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 523,
			"versionNonce": 600044139,
			"isDeleted": false,
			"id": "tLW1v-4Ha_VY3SIA8A1fA",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1177.7256135799325,
			"y": 544.4184131018907,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 66.65065174759184,
			"height": 22.420777897629478,
			"seed": 787144955,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127530,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "-A_04VBf98azsjcm_mCp2",
				"gap": 9.318862915039062,
				"focus": 0.13468623161870444
			},
			"endBinding": {
				"elementId": "rQzIY3_rrMVi6NhI9ALeZ",
				"gap": 1.000000000000064,
				"focus": 0.003708529562461978
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-66.65065174759184,
					22.420777897629478
				]
			]
		},
		{
			"type": "rectangle",
			"version": 410,
			"versionNonce": 2003090256,
			"isDeleted": false,
			"id": "GTmFjdMG95UA5eJRiXDC8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 481.0855848170212,
			"y": 423.9261718346039,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 422.39295959472656,
			"height": 85.67447662353516,
			"seed": 2054883739,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "GGvdMDVe"
				},
				{
					"id": "2srzRkpeHi_7rxlBuNtKI",
					"type": "arrow"
				},
				{
					"id": "MUlq1bErNp7J4316yMxLH",
					"type": "arrow"
				},
				{
					"id": "b2l9AEPHutN12KTiRIXZk",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 454,
			"versionNonce": 718496176,
			"isDeleted": false,
			"id": "GGvdMDVe",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 489.0821744776657,
			"y": 441.7634101463715,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 406.3997802734375,
			"height": 50,
			"seed": 2134711867,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "清除玩家计分板数值\n/scoreboard players reset @a 计分板名称",
			"rawText": "清除玩家计分板数值\n/scoreboard players reset @a 计分板名称",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "GTmFjdMG95UA5eJRiXDC8",
			"originalText": "清除玩家计分板数值\n/scoreboard players reset @a 计分板名称",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 585,
			"versionNonce": 1725163051,
			"isDeleted": false,
			"id": "MUlq1bErNp7J4316yMxLH",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 985.6225420494296,
			"y": 572.4222235266004,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 105.96223603964779,
			"height": 61.82157506846136,
			"seed": 403939035,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127547,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "rQzIY3_rrMVi6NhI9ALeZ",
				"gap": 8.876901689422432,
				"focus": -0.5022215931754942
			},
			"endBinding": {
				"elementId": "GTmFjdMG95UA5eJRiXDC8",
				"gap": 1,
				"focus": -0.3943551200169048
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-105.96223603964779,
					-61.82157506846136
				]
			]
		},
		{
			"type": "arrow",
			"version": 804,
			"versionNonce": 1398662379,
			"isDeleted": false,
			"id": "2srzRkpeHi_7rxlBuNtKI",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 906.6557617830713,
			"y": 476.5236065004521,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 231.99673525448657,
			"height": 1.2006150300994136,
			"seed": 529599355,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127546,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "GTmFjdMG95UA5eJRiXDC8",
				"gap": 3.177217371323536,
				"focus": 0.19692335606090727
			},
			"endBinding": {
				"elementId": "JUWEvGlr",
				"gap": 15.105009191176578,
				"focus": 0.3307605650082299
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					231.99673525448657,
					1.2006150300994136
				]
			]
		},
		{
			"type": "rectangle",
			"version": 461,
			"versionNonce": 1581918032,
			"isDeleted": false,
			"id": "O83GqZwk7g6dI6zugXnB4",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 777.0527523908377,
			"y": 695.2702095076565,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 766.2409515380859,
			"height": 85,
			"seed": 2046288923,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "xQ26bjp7"
				},
				{
					"id": "1sOKlxH4VJA7bcuguNlSB",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 622,
			"versionNonce": 541767088,
			"isDeleted": false,
			"id": "xQ26bjp7",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 817.4434002790213,
			"y": 712.7702095076565,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 685.4596557617188,
			"height": 50,
			"seed": 1597679803,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "execute指令循环使得达到数值的玩家TP\n/execute as @a[scores={设置的计分板名称=1}] at @s run tp 1_player",
			"rawText": "execute指令循环使得达到数值的玩家TP\n/execute as @a[scores={设置的计分板名称=1}] at @s run tp 1_player",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "O83GqZwk7g6dI6zugXnB4",
			"originalText": "execute指令循环使得达到数值的玩家TP\n/execute as @a[scores={设置的计分板名称=1}] at @s run tp 1_player",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 446,
			"versionNonce": 1596626795,
			"isDeleted": false,
			"id": "1sOKlxH4VJA7bcuguNlSB",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1119.4264510836988,
			"y": 694.2702095076565,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 59.9543871694236,
			"height": 51.109649658203125,
			"seed": 1694226779,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127551,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "O83GqZwk7g6dI6zugXnB4",
				"gap": 1,
				"focus": 0.023745186929848946
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-59.9543871694236,
					-51.109649658203125
				]
			]
		},
		{
			"type": "freedraw",
			"version": 68,
			"versionNonce": 180912048,
			"isDeleted": false,
			"id": "P0i7MVBIRjqKcJFMmIsgd",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 987.7383616583139,
			"y": 446.03954562414674,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 54.94127061631946,
			"height": 40.57203504774304,
			"seed": 1576738741,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8452012803819571,
					0
				],
				[
					5.916748046875,
					5.071512858072879
				],
				[
					11.83349609375,
					9.297756618923586
				],
				[
					16.904975043402715,
					14.369269476996465
				],
				[
					22.821723090277715,
					19.440782335069457
				],
				[
					29.583740234375,
					24.51226128472217
				],
				[
					34.65528700086804,
					27.04803466796875
				],
				[
					39.72676595052087,
					32.119513617621465
				],
				[
					45.64351399739587,
					36.345791286892336
				],
				[
					50.7149929470487,
					38.88153076171875
				],
				[
					52.40553114149304,
					39.72679985894092
				],
				[
					54.09600151909706,
					39.72679985894092
				],
				[
					54.94127061631946,
					40.57203504774304
				],
				[
					54.94127061631946,
					40.57203504774304
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 67,
			"versionNonce": 1136956240,
			"isDeleted": false,
			"id": "wq2tmoMzoUGTYX03LKpNr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1037.6081533249805,
			"y": 446.03954562414674,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 52.40559895833326,
			"height": 41.41730414496533,
			"seed": 711628213,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-2.535739474826414,
					-0.8452690972222854
				],
				[
					-8.452555338541742,
					-0.8452690972222854
				],
				[
					-14.369303385416629,
					1.690504286024293
				],
				[
					-23.667060004340215,
					9.297756618923586
				],
				[
					-32.11954752604163,
					16.05977376302087
				],
				[
					-43.10784233940967,
					23.667026095920164
				],
				[
					-47.334052191840215,
					29.583774142795164
				],
				[
					-50.7150607638888,
					34.65528700086804
				],
				[
					-50.7150607638888,
					36.345791286892336
				],
				[
					-50.7150607638888,
					37.19102647569446
				],
				[
					-52.40559895833326,
					39.72679985894092
				],
				[
					-52.40559895833326,
					40.57203504774304
				],
				[
					-52.40559895833326,
					40.57203504774304
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "arrow",
			"version": 182,
			"versionNonce": 1131145419,
			"isDeleted": false,
			"id": "b2l9AEPHutN12KTiRIXZk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 903.9359872633017,
			"y": 421.12699794660546,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 241.74629295975274,
			"height": 97.02966235161205,
			"seed": 419915291,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127547,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "GTmFjdMG95UA5eJRiXDC8",
				"gap": 2.8363054168565895,
				"focus": -0.11669474820856265
			},
			"endBinding": {
				"elementId": "FhKIwoAdj4-BN_i86qkH3",
				"focus": 0.495738445117299,
				"gap": 1
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					149.50828636795586,
					-25.711646299365952
				],
				[
					241.74629295975274,
					-97.02966235161205
				]
			]
		},
		{
			"type": "arrow",
			"version": 1300,
			"versionNonce": 1487809995,
			"isDeleted": false,
			"id": "VG6I1TTfsOdcJyYHdcEEc",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3040.754208341688,
			"y": 255.22580069498724,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 51.389322985810395,
			"height": 0.9654437596281014,
			"seed": 704396059,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127563,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "8GcQOSNo9_gEXEkBM0Jon",
				"gap": 9.045524130697913,
				"focus": 0.3116273771722514
			},
			"endBinding": {
				"elementId": "D6U8vTaPV1D5i8FRmmnPS",
				"gap": 2.28216552734375,
				"focus": 0.08927920352215289
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					51.389322985810395,
					-0.9654437596281014
				]
			]
		},
		{
			"type": "rectangle",
			"version": 463,
			"versionNonce": 1074811824,
			"isDeleted": false,
			"id": "D6U8vTaPV1D5i8FRmmnPS",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3094.4256968548416,
			"y": 204.6258600608843,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 520.1361630088406,
			"height": 99.13459055047282,
			"seed": 1520181179,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "VG6I1TTfsOdcJyYHdcEEc",
					"type": "arrow"
				},
				{
					"id": "yljlFRpvA2g8z8NJx7HH1",
					"type": "arrow"
				},
				{
					"id": "xUrHhCCjAnZbQM_H0dqmj",
					"type": "arrow"
				},
				{
					"id": "x3YvyILUlivddCf99lDM6",
					"type": "arrow"
				},
				{
					"id": "hHUlNnZle6d8nTFkPYoPJ",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 435,
			"versionNonce": 1184104272,
			"isDeleted": false,
			"id": "iWNwdf60",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3130.632386098796,
			"y": 223.61990125783882,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 473.73974609375,
			"height": 50,
			"seed": 51802203,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "0NfKHp_wP1s6m1UgPwDdv",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "将计分板属性赋予玩家\n/scoreboard players enable @a 设置的计分板名称",
			"rawText": "将计分板属性赋予玩家\n/scoreboard players enable @a 设置的计分板名称",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "将计分板属性赋予玩家\n/scoreboard players enable @a 设置的计分板名称",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 886,
			"versionNonce": 472538544,
			"isDeleted": false,
			"id": "0NfKHp_wP1s6m1UgPwDdv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3356.229243411849,
			"y": 284.67754896291694,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.294023457715411,
			"height": 133.7044051726445,
			"seed": 356363515,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "iWNwdf60",
				"focus": 0.03208711479227609,
				"gap": 11.057647705078125
			},
			"endBinding": {
				"elementId": "J2Jy074Z",
				"focus": -0.022415841476071605,
				"gap": 15.437650519028466
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-13.294023457715411,
					133.7044051726445
				]
			]
		},
		{
			"type": "rectangle",
			"version": 391,
			"versionNonce": 1484232016,
			"isDeleted": false,
			"id": "G5gwLQrqys-BcjWgcvMPK",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3129.721592811543,
			"y": 420.66408914532707,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 504.84244113035606,
			"height": 94.13982391357423,
			"seed": 613701019,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "0NfKHp_wP1s6m1UgPwDdv",
					"type": "arrow"
				},
				{
					"id": "JUdL2ARPtd106LI_UHcf5",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 554,
			"versionNonce": 1014179760,
			"isDeleted": false,
			"id": "J2Jy074Z",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3137.7025128672176,
			"y": 433.8196046545899,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 409.2799072265625,
			"height": 75,
			"seed": 810347067,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "JUdL2ARPtd106LI_UHcf5",
					"type": "arrow"
				},
				{
					"id": "0NfKHp_wP1s6m1UgPwDdv",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "玩家达到计分板数值\n/trigger 计分板名称 add 增加的数值\n/trigger 计分板名称  （该命令为直接增加1）",
			"rawText": "玩家达到计分板数值\n/trigger 计分板名称 add 增加的数值\n/trigger 计分板名称  （该命令为直接增加1）",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "玩家达到计分板数值\n/trigger 计分板名称 add 增加的数值\n/trigger 计分板名称  （该命令为直接增加1）",
			"lineHeight": 1.25,
			"baseline": 67
		},
		{
			"type": "diamond",
			"version": 309,
			"versionNonce": 1433955152,
			"isDeleted": false,
			"id": "8Lc0pIapPmBWUSCuaYg4S",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2968.8659230918206,
			"y": 504.1916744304874,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 146.05938720703125,
			"height": 120,
			"seed": 759818971,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "tGs4rubZ"
				},
				{
					"id": "JUdL2ARPtd106LI_UHcf5",
					"type": "arrow"
				},
				{
					"id": "pgD6yaHKNk_OmnJQkDwp6",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 309,
			"versionNonce": 756199856,
			"isDeleted": false,
			"id": "tGs4rubZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3027.2307836264886,
			"y": 551.6916744304874,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 29.299972534179688,
			"height": 25,
			"seed": 1344132987,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "TP",
			"rawText": "TP",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "8Lc0pIapPmBWUSCuaYg4S",
			"originalText": "TP",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 688,
			"versionNonce": 536213675,
			"isDeleted": false,
			"id": "JUdL2ARPtd106LI_UHcf5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3161.4940924774514,
			"y": 524.1227759739404,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 66.49689287607634,
			"height": 22.40207136745653,
			"seed": 386609179,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127554,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "J2Jy074Z",
				"gap": 15.303171319350497,
				"focus": 0.07631137889240669
			},
			"endBinding": {
				"elementId": "8Lc0pIapPmBWUSCuaYg4S",
				"gap": 1,
				"focus": 0.0037085295624647544
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-66.49689287607634,
					22.40207136745653
				]
			]
		},
		{
			"type": "arrow",
			"version": 676,
			"versionNonce": 1430309701,
			"isDeleted": false,
			"id": "pgD6yaHKNk_OmnJQkDwp6",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2969.608314434085,
			"y": 552.0930939293589,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 105.76119785196079,
			"height": 61.78808259917025,
			"seed": 335836347,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813166854,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "8Lc0pIapPmBWUSCuaYg4S",
				"gap": 8.876901689422496,
				"focus": -0.502221593175497
			},
			"endBinding": {
				"elementId": "w9eNOKLvMJPqhsVhtKxsS",
				"gap": 7.149128870480581,
				"focus": -0.5157503649327457
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-105.76119785196079,
					-61.78808259917025
				]
			]
		},
		{
			"type": "rectangle",
			"version": 517,
			"versionNonce": 791795536,
			"isDeleted": false,
			"id": "kn-W4ZQliizlBxugLCUX2",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2759.729855383487,
			"y": 674.9745723797062,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 766.2409515380859,
			"height": 85,
			"seed": 1448395259,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "20CS3DZx"
				},
				{
					"id": "6vI41ggxD2tg6NltYqnYm",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 678,
			"versionNonce": 1995834800,
			"isDeleted": false,
			"id": "20CS3DZx",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2800.1205032716707,
			"y": 692.4745723797062,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 685.4596557617188,
			"height": 50,
			"seed": 1006684827,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "execute指令循环使得达到数值的玩家TP\n/execute as @a[scores={设置的计分板名称=1}] at @s run tp 1_player",
			"rawText": "execute指令循环使得达到数值的玩家TP\n/execute as @a[scores={设置的计分板名称=1}] at @s run tp 1_player",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "kn-W4ZQliizlBxugLCUX2",
			"originalText": "execute指令循环使得达到数值的玩家TP\n/execute as @a[scores={设置的计分板名称=1}] at @s run tp 1_player",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 560,
			"versionNonce": 935987691,
			"isDeleted": false,
			"id": "6vI41ggxD2tg6NltYqnYm",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3102.679131019548,
			"y": 673.9745723797062,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 59.26206046678996,
			"height": 51.109649658203125,
			"seed": 1818410811,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127557,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "kn-W4ZQliizlBxugLCUX2",
				"gap": 1,
				"focus": 0.023745186929847374
			},
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-59.26206046678996,
					-51.109649658203125
				]
			]
		},
		{
			"type": "arrow",
			"version": 337,
			"versionNonce": 225929349,
			"isDeleted": false,
			"id": "yljlFRpvA2g8z8NJx7HH1",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2869.9605202306448,
			"y": 390.34502937338505,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 259.66676663089265,
			"height": 86.54333090634196,
			"seed": 2115314971,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813166854,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "w9eNOKLvMJPqhsVhtKxsS",
				"gap": 20.240430281193255,
				"focus": -0.6078997191743276
			},
			"endBinding": {
				"elementId": "D6U8vTaPV1D5i8FRmmnPS",
				"focus": 0.495738445117299,
				"gap": 1
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					167.42876003909578,
					-15.22531485409587
				],
				[
					259.66676663089265,
					-86.54333090634196
				]
			]
		},
		{
			"type": "rectangle",
			"version": 494,
			"versionNonce": 1849871307,
			"isDeleted": false,
			"id": "w9eNOKLvMJPqhsVhtKxsS",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2434.305028116917,
			"y": 405.6349034457994,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 422.39295959472656,
			"height": 85.67447662353516,
			"seed": 409366549,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "O2Lqw58e"
				},
				{
					"id": "yljlFRpvA2g8z8NJx7HH1",
					"type": "arrow"
				},
				{
					"id": "pgD6yaHKNk_OmnJQkDwp6",
					"type": "arrow"
				}
			],
			"updated": 1700813159650,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 528,
			"versionNonce": 1076954341,
			"isDeleted": false,
			"id": "O2Lqw58e",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2442.3016177775617,
			"y": 423.472141757567,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 406.3997802734375,
			"height": 50,
			"seed": 111781237,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1700813159637,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "清除玩家计分板数值\n/scoreboard players reset @a 计分板名称",
			"rawText": "清除玩家计分板数值\n/scoreboard players reset @a 计分板名称",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "w9eNOKLvMJPqhsVhtKxsS",
			"originalText": "清除玩家计分板数值\n/scoreboard players reset @a 计分板名称",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "rectangle",
			"version": 498,
			"versionNonce": 909859152,
			"isDeleted": false,
			"id": "8GcQOSNo9_gEXEkBM0Jon",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2503.805074784592,
			"y": 202.9911714094485,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 527.9036094263981,
			"height": 85,
			"seed": 837399835,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "TKzjJSxU"
				},
				{
					"id": "VG6I1TTfsOdcJyYHdcEEc",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 762,
			"versionNonce": 1623040944,
			"isDeleted": false,
			"id": "TKzjJSxU",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2511.377027202869,
			"y": 220.4911714094485,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 512.7597045898438,
			"height": 50,
			"seed": 986339771,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "创建计分板trigger类型\n/scoreboard objectives add 设置的计分板名称 trigger",
			"rawText": "创建计分板trigger类型\n/scoreboard objectives add 设置的计分板名称 trigger",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "8GcQOSNo9_gEXEkBM0Jon",
			"originalText": "创建计分板trigger类型\n/scoreboard objectives add 设置的计分板名称 trigger",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "diamond",
			"version": 156,
			"versionNonce": 1310961488,
			"isDeleted": false,
			"id": "DsI7cV2--N9bYalnqqfAj",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3165.1455568210276,
			"y": -41.12934815791658,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 142.96133094901552,
			"height": 133.35056049951888,
			"seed": 2079732123,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "0UvN8Dof"
				},
				{
					"id": "xUrHhCCjAnZbQM_H0dqmj",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 144,
			"versionNonce": 1521331632,
			"isDeleted": false,
			"id": "0UvN8Dof",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3206.3858895582816,
			"y": 13.208291966963138,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"width": 60,
			"height": 25,
			"seed": 42237941,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "新玩家",
			"rawText": "新玩家",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "DsI7cV2--N9bYalnqqfAj",
			"originalText": "新玩家",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 160,
			"versionNonce": 2072999691,
			"isDeleted": false,
			"id": "xUrHhCCjAnZbQM_H0dqmj",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3255.041758711318,
			"y": 76.8052179083596,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"width": 68.02723666440716,
			"height": 121.13538506554701,
			"seed": 1989089819,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127566,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "DsI7cV2--N9bYalnqqfAj",
				"gap": 1.288137133418175,
				"focus": 0.14508361569022074
			},
			"endBinding": {
				"elementId": "D6U8vTaPV1D5i8FRmmnPS",
				"gap": 6.6852570869776855,
				"focus": 0.0005749760733378279
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					68.02723666440716,
					121.13538506554701
				]
			]
		},
		{
			"type": "freedraw",
			"version": 92,
			"versionNonce": 1846310832,
			"isDeleted": false,
			"id": "P73SVmmLiIK9LWulzSKAT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3238.358217694591,
			"y": 100.87844507550295,
			"strokeColor": "#e03131",
			"backgroundColor": "#b2f2bb",
			"width": 24.28197959410636,
			"height": 33.994685710658416,
			"seed": 195687317,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.9425957730954906,
					4.856411504474181
				],
				[
					4.856411504474181,
					10.684042967231733
				],
				[
					10.684042967231562,
					15.540454471705914
				],
				[
					14.569156585157998,
					20.39682701204788
				],
				[
					18.45427020308489,
					25.2531995523899
				],
				[
					19.425568089632634,
					27.195756361353176
				],
				[
					21.36808593446358,
					30.109611056864082
				],
				[
					22.339383821011324,
					32.05212890169514
				],
				[
					24.28197959410636,
					33.994685710658416
				],
				[
					24.28197959410636,
					33.994685710658416
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 71,
			"versionNonce": 551295824,
			"isDeleted": false,
			"id": "nyfFCFWoc8cQ75zoPrbA4",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3259.726386871414,
			"y": 103.79229977101397,
			"strokeColor": "#e03131",
			"backgroundColor": "#b2f2bb",
			"width": 20.396788047915834,
			"height": 31.08083101514751,
			"seed": 1354423317,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617090,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.9138157313788042
				],
				[
					-3.885113617926436,
					8.741486158268515
				],
				[
					-9.712745080683817,
					14.569156585158225
				],
				[
					-13.597858698610708,
					18.45423123895256
				],
				[
					-16.511674429989398,
					22.339344856878995
				],
				[
					-19.42549016136809,
					25.253199552389958
				],
				[
					-20.396788047915834,
					29.138274206184235
				],
				[
					-20.396788047915834,
					31.08083101514751
				],
				[
					-20.396788047915834,
					31.08083101514751
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "diamond",
			"version": 113,
			"versionNonce": 2130837936,
			"isDeleted": false,
			"id": "ZIngqhenPuXtfWymvHr4K",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3360.2617672238603,
			"y": -29.89864124032536,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"width": 146.28895720391893,
			"height": 126.0255625058817,
			"seed": 851159003,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "wTXXSBbn"
				},
				{
					"id": "x3YvyILUlivddCf99lDM6",
					"type": "arrow"
				}
			],
			"updated": 1698846617090,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 95,
			"versionNonce": 1801204048,
			"isDeleted": false,
			"id": "wTXXSBbn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3413.33400652484,
			"y": 20.60774938614506,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 40,
			"height": 25,
			"seed": 1992786203,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617091,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "手动",
			"rawText": "手动",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ZIngqhenPuXtfWymvHr4K",
			"originalText": "手动",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "diamond",
			"version": 205,
			"versionNonce": 750144432,
			"isDeleted": false,
			"id": "ipd6oXl2Whplrhjb_AvCJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3573.22094527675,
			"y": -16.89164874099825,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"width": 146.28895720391893,
			"height": 126.0255625058817,
			"seed": 606845723,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "LSgmnL7h"
				},
				{
					"id": "hHUlNnZle6d8nTFkPYoPJ",
					"type": "arrow"
				},
				{
					"id": "EQG4NOugHVt0nP-BulmwU",
					"type": "arrow"
				}
			],
			"updated": 1698846617091,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 190,
			"versionNonce": 1500088144,
			"isDeleted": false,
			"id": "LSgmnL7h",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3626.29318457773,
			"y": 33.61474188547217,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 40,
			"height": 25,
			"seed": 1658560443,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617091,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "自动",
			"rawText": "自动",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ipd6oXl2Whplrhjb_AvCJ",
			"originalText": "自动",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 72,
			"versionNonce": 119500875,
			"isDeleted": false,
			"id": "x3YvyILUlivddCf99lDM6",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3429.7889638424786,
			"y": 99.80223584439268,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 44.64484174172412,
			"height": 95.4388016547501,
			"seed": 977751931,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127569,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ZIngqhenPuXtfWymvHr4K",
				"gap": 5.145472138798333,
				"focus": -0.37704359666604753
			},
			"endBinding": {
				"elementId": "D6U8vTaPV1D5i8FRmmnPS",
				"gap": 9.384822561741515,
				"focus": 0.01085038919221875
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-44.64484174172412,
					95.4388016547501
				]
			]
		},
		{
			"type": "arrow",
			"version": 94,
			"versionNonce": 1131551115,
			"isDeleted": false,
			"id": "hHUlNnZle6d8nTFkPYoPJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3641.4102089247663,
			"y": 108.07574487968576,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 144.37249962632177,
			"height": 88.20282538834768,
			"seed": 417349307,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700813127572,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ipd6oXl2Whplrhjb_AvCJ",
				"gap": 2.4324960505324,
				"focus": -0.9351638823251185
			},
			"endBinding": {
				"elementId": "D6U8vTaPV1D5i8FRmmnPS",
				"gap": 8.34728979285083,
				"focus": 0.13994081699054595
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-144.37249962632177,
					88.20282538834768
				]
			]
		},
		{
			"type": "freedraw",
			"version": 33,
			"versionNonce": 1106976688,
			"isDeleted": false,
			"id": "UCrLT3OblQcDlm69Gvb3j",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3358.1867016860783,
			"y": 111.20271455091009,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#ffc9c9",
			"width": 59.138035949014466,
			"height": 39.42537117306949,
			"seed": 1883651355,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617091,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.0375327688906282
				],
				[
					2.074982295421705,
					4.150047833203075
				],
				[
					5.187497359734152,
					6.225071749804613
				],
				[
					8.3000124240466,
					10.375119583007631
				],
				[
					10.375077961828083,
					13.487634647320078
				],
				[
					11.412610730718825,
					16.60014971163247
				],
				[
					12.450060257249788,
					16.60014971163247
				],
				[
					14.525125795030817,
					16.60014971163247
				],
				[
					22.825221461437195,
					14.525167416210707
				],
				[
					26.97526929463993,
					8.300095666406094
				],
				[
					31.125233885483794,
					4.150047833203075
				],
				[
					34.237832192155565,
					-2.0750239166015376
				],
				[
					39.42532955188972,
					-6.225071749804556
				],
				[
					42.53792785856194,
					-10.375119583007631
				],
				[
					45.650442922873935,
					-13.487634647320021
				],
				[
					49.800490756077124,
					-16.60014971163247
				],
				[
					52.91300582038957,
					-19.712706397124634
				],
				[
					56.02552088470202,
					-21.787730313726172
				],
				[
					58.100503180123724,
					-22.825221461437025
				],
				[
					59.138035949014466,
					-22.825221461437025
				],
				[
					59.138035949014466,
					-22.825221461437025
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 91,
			"versionNonce": 1183576912,
			"isDeleted": false,
			"id": "3ghZnxHZeC-REbB0oFFPt",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3536.6559064398675,
			"y": 125.99365401043556,
			"strokeColor": "#2f9e44",
			"backgroundColor": "#ffc9c9",
			"width": 59.138035949014466,
			"height": 39.42537117306949,
			"seed": 962862555,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1698846617091,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					1.0375327688906282
				],
				[
					2.074982295421705,
					4.150047833203075
				],
				[
					5.187497359734152,
					6.225071749804613
				],
				[
					8.3000124240466,
					10.375119583007631
				],
				[
					10.375077961828083,
					13.487634647320078
				],
				[
					11.412610730718825,
					16.60014971163247
				],
				[
					12.450060257249788,
					16.60014971163247
				],
				[
					14.525125795030817,
					16.60014971163247
				],
				[
					22.825221461437195,
					14.525167416210707
				],
				[
					26.97526929463993,
					8.300095666406094
				],
				[
					31.125233885483794,
					4.150047833203075
				],
				[
					34.237832192155565,
					-2.0750239166015376
				],
				[
					39.42532955188972,
					-6.225071749804556
				],
				[
					42.53792785856194,
					-10.375119583007631
				],
				[
					45.650442922873935,
					-13.487634647320021
				],
				[
					49.800490756077124,
					-16.60014971163247
				],
				[
					52.91300582038957,
					-19.712706397124634
				],
				[
					56.02552088470202,
					-21.787730313726172
				],
				[
					58.100503180123724,
					-22.825221461437025
				],
				[
					59.138035949014466,
					-22.825221461437025
				],
				[
					59.138035949014466,
					-22.825221461437025
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "arrow",
			"version": 388,
			"versionNonce": 885697825,
			"isDeleted": false,
			"id": "EQG4NOugHVt0nP-BulmwU",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3834.4040037966643,
			"y": -19.639806608108806,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 108.06207270226332,
			"height": 58.858797301841925,
			"seed": 1355334491,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1700839010920,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "A__r6ZJCjjolMe7NqNpy1",
				"gap": 5.187580602093931,
				"focus": 0.4748381815905203
			},
			"endBinding": {
				"elementId": "ipd6oXl2Whplrhjb_AvCJ",
				"gap": 9.711651592676304,
				"focus": 0.5817728806789925
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-108.06207270226332,
					58.858797301841925
				]
			]
		},
		{
			"type": "rectangle",
			"version": 283,
			"versionNonce": 1155064171,
			"isDeleted": false,
			"id": "A__r6ZJCjjolMe7NqNpy1",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3839.591584398758,
			"y": -158.35775634500223,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"width": 626.6563903900648,
			"height": 176.2011728449665,
			"seed": 1943273909,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "1zAspqkw"
				},
				{
					"id": "EQG4NOugHVt0nP-BulmwU",
					"type": "arrow"
				}
			],
			"updated": 1700813127575,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 401,
			"versionNonce": 314717515,
			"isDeleted": false,
			"id": "1zAspqkw",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 3878.319956595744,
			"y": -120.25716992251898,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"width": 549.1996459960938,
			"height": 100,
			"seed": 920432757,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1700813127577,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "命令方块拉杆或者给予出生带你附近的人指令\n/scoreboard players enable @p 计分板名称\n/scoreboard players enable @p[distance=..2] 计分板名称\n",
			"rawText": "命令方块拉杆或者给予出生带你附近的人指令\n/scoreboard players enable @p 计分板名称\n/scoreboard players enable @p[distance=..2] 计分板名称\n",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "A__r6ZJCjjolMe7NqNpy1",
			"originalText": "命令方块拉杆或者给予出生带你附近的人指令\n/scoreboard players enable @p 计分板名称\n/scoreboard players enable @p[distance=..2] 计分板名称\n",
			"lineHeight": 1.25,
			"baseline": 92
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "#b2f2bb",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 460.8286951007058,
		"scrollY": 1452.9468190729697,
		"zoom": {
			"value": 0.2
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%