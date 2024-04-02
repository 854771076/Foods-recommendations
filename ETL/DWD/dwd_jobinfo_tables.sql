
create database dwd_foods;
CREATE TABLE `dwd_foods`.`dwd_foods_db_spider_t_foods`(
  `id` string,
  `name` string,
  `url` string,
  `raw` string,
  `type` string,
  `type_code` int,
  `img` string,
  `raw_detail` string,
  `cookbook_make` string,
  `crawler_date` timestamp,
  `cdc_sync_date` timestamp
  )
PARTITIONED BY (partition_date string);






-- 处理foods
select 
cast ( id as int) as id,
`name`,
`url`,
`raw` ,
`type`,
Case when
type="不限" then 0
when type="猪肉" then 1
when type="排骨" then 2
when type="猪蹄" then 3
when type="猪肚" then 4
when type="五花肉" then 5
when type="猪肝" then 6
when type="猪血" then 7
when type="猪腰" then 8
when type="猪皮" then 9
when type="猪肘" then 10
when type="猪耳朵" then 11
when type="猪心" then 12
when type="猪肺" then 13
when type="猪大肠" then 14
when type="猪大骨头" then 15
when type="猪小排" then 16
when type="猪里脊肉" then 17
when type="猪排" then 18
when type="猪舌头" then 19
when type="牛肉" then 21
when type="牛腩" then 22
when type="牛排" then 23
when type="肥牛" then 24
when type="牛肚" then 25
when type="牛蹄筋" then 26
when type="牛尾" then 27
when type="羊肉" then 29
when type="羊排" then 30
when type="羊肝" then 31
when type="羊蝎子" then 32
when type="羊骨" then 33
when type="鸡肉" then 35
when type="鸡翅" then 36
when type="鸡腿" then 37
when type="鸡爪" then 38
when type="鸡肝" then 39
when type="鸡胗" then 40
when type="鸡心" then 41
when type="火鸡肉" then 42
when type="乌鸡" then 43
when type="鸭肉" then 45
when type="鸭肝" then 46
when type="鸭腿" then 47
when type="鸭翅" then 48
when type="鸭胗" then 49
when type="鸭血" then 50
when type="鸭掌" then 51
when type="鸭肠" then 52
when type="腊肉" then 54
when type="火腿" then 55
when type="香肠" then 56
when type="咸肉" then 57
when type="肉松" then 58
when type="培根" then 59
when type="午餐肉" then 60
when type="熏肉" then 61
when type="兔肉" then 63
when type="鹿肉" then 64
when type="驴肉" then 65
when type="雪蛤" then 66
when type="蚕蛹" then 67
when type="鹅肝" then 68
when type="乳鸽" then 69
when type="鸽肉" then 70
when type="鸡蛋" then 72
when type="鸭蛋" then 73
when type="鹌鹑蛋" then 74
when type="咸鸭蛋" then 75
when type="松花蛋" then 76
when type="奶酪" then 78
when type="黄油" then 79
when type="奶油" then 80
when type="草鱼" then 82
when type="鲤鱼" then 83
when type="鲫鱼" then 84
when type="鲢鱼" then 85
when type="青鱼" then 86
when type="鲶鱼" then 87
when type="银鱼" then 88
when type="罗非鱼" then 89
when type="武昌鱼" then 90
when type="鳊鱼" then 91
when type="桂鱼" then 92
when type="乌鳢" then 93
when type="泥鳅" then 94
when type="黄鳝" then 95
when type="带鱼" then 97
when type="鲈鱼" then 98
when type="鳕鱼" then 99
when type="鲅鱼" then 100
when type="金枪鱼" then 101
when type="鲳鱼" then 102
when type="鳗鱼" then 103
when type="三文鱼" then 104
when type="龙利鱼" then 105
when type="梭鱼" then 106
when type="秋刀鱼" then 107
when type="比目鱼" then 108
when type="沙丁鱼" then 109
when type="多春鱼" then 110
when type="石斑鱼" then 111
when type="鲷鱼" then 112
when type="老板鱼" then 113
when type="黄花鱼" then 114
when type="马面鱼" then 115
when type="小黄鱼" then 116
when type="鱼丸" then 118
when type="鱼头" then 119
when type="鱼干" then 120
when type="鱼籽" then 121
when type="花胶" then 122
when type="虾" then 124
when type="虾米" then 125
when type="龙虾" then 126
when type="虾皮" then 127
when type="海虾" then 128
when type="北极虾" then 129
when type="基围虾" then 130
when type="小龙虾" then 131
when type="河虾" then 132
when type="皮皮虾" then 133
when type="虾仁" then 134
when type="螃蟹" then 136
when type="梭子蟹" then 137
when type="河蟹" then 138
when type="蛤蜊" then 140
when type="牡蛎" then 141
when type="鲍鱼" then 142
when type="干贝" then 143
when type="扇贝" then 144
when type="鲜贝" then 145
when type="文蛤" then 146
when type="蛏子" then 147
when type="海螺" then 148
when type="青口" then 149
when type="河蚌" then 150
when type="淡菜" then 151
when type="生蚝" then 152
when type="北极贝" then 153
when type="海带" then 155
when type="紫菜" then 156
when type="裙带菜" then 157
when type="海藻" then 158
when type="发菜" then 159
when type="墨鱼" then 161
when type="鱿鱼" then 162
when type="章鱼" then 163
when type="海参" then 164
when type="甲鱼" then 165
when type="田螺" then 166
when type="海蜇头" then 167
when type="海蜇皮" then 168
when type="田鸡" then 169
when type="牛蛙" then 170
when type="白菜" then 172
when type="油菜" then 173
when type="芹菜" then 174
when type="菠菜" then 175
when type="小白菜" then 176
when type="韭菜" then 177
when type="生菜" then 178
when type="茼蒿" then 179
when type="香菜" then 180
when type="芦笋" then 181
when type="苋菜" then 182
when type="芥菜" then 183
when type="莴笋" then 184
when type="茭白" then 185
when type="雪里蕻" then 186
when type="菜花" then 187
when type="西兰花" then 188
when type="黄花菜" then 189
when type="荠菜" then 190
when type="百合" then 191
when type="蕨菜" then 192
when type="橄榄菜" then 193
when type="菊花" then 194
when type="豌豆尖" then 195
when type="槐花" then 196
when type="韭黄" then 197
when type="紫甘蓝" then 198
when type="西芹" then 199
when type="茴香" then 200
when type="娃娃菜" then 201
when type="芥蓝" then 202
when type="苦菊" then 203
when type="空心菜" then 204
when type="油麦菜" then 205
when type="马兰头" then 206
when type="水芹菜" then 207
when type="芦荟" then 208
when type="芝麻菜" then 209
when type="红菜苔" then 210
when type="卷心菜" then 211
when type="蒜薹" then 212
when type="枸杞菜" then 213
when type="豌豆苗" then 214
when type="萝卜叶" then 215
when type="木耳菜" then 216
when type="藜蒿" then 217
when type="马齿苋" then 218
when type="圆生菜" then 219
when type="芥兰" then 220
when type="紫背天葵" then 221
when type="土豆" then 223
when type="红薯" then 224
when type="芋头" then 225
when type="胡萝卜" then 226
when type="白萝卜" then 227
when type="竹笋" then 228
when type="魔芋" then 229
when type="山药" then 230
when type="藕" then 231
when type="牛蒡" then 232
when type="荸荠" then 233
when type="紫薯" then 234
when type="青萝卜" then 235
when type="春笋" then 236
when type="冬笋" then 237
when type="菱角" then 238
when type="慈菇" then 239
when type="心里美萝卜" then 240
when type="甜菜根" then 241
when type="红萝卜" then 242
when type="慈姑" then 243
when type="荞头" then 244
when type="苤蓝" then 245
when type="豆角" then 247
when type="茄子" then 248
when type="青椒" then 249
when type="西红柿" then 250
when type="荷兰豆" then 251
when type="豇豆" then 252
when type="扁豆" then 253
when type="黄瓜" then 254
when type="冬瓜" then 255
when type="苦瓜" then 256
when type="南瓜" then 257
when type="丝瓜" then 258
when type="西葫芦" then 259
when type="葫芦" then 260
when type="红椒" then 261
when type="油豆角" then 262
when type="瓠瓜" then 263
when type="佛手瓜" then 264
when type="彩椒" then 265
when type="圆茄子" then 266
when type="辣椒" then 267
when type="绿茄子" then 268
when type="笋瓜" then 269
when type="四季豆" then 270
when type="方瓜" then 271
when type="节瓜" then 272
when type="秋葵" then 273
when type="蘑菇" then 275
when type="草菇" then 276
when type="香菇" then 277
when type="平菇" then 278
when type="金针菇" then 279
when type="口蘑" then 280
when type="银耳" then 281
when type="猴头菇" then 282
when type="竹荪" then 283
when type="杏鲍菇" then 284
when type="茶树菇" then 285
when type="鸡腿菇" then 286
when type="蟹味菇" then 287
when type="牛肝菌" then 288
when type="元蘑" then 289
when type="木耳" then 290
when type="榛蘑" then 291
when type="海鲜菇" then 292
when type="干香菇" then 293
when type="红菇" then 294
when type="松蘑" then 295
when type="虫草花" then 296
when type="苜蓿" then 298
when type="霸王花" then 299
when type="蒜苗" then 301
when type="洋葱" then 302
when type="青蒜" then 303
when type="小葱" then 304
when type="大葱" then 305
when type="葱白" then 306
when type="大蒜" then 307
when type="绿豆芽" then 309
when type="黄豆芽" then 310
when type="黄豆" then 311
when type="毛豆" then 312
when type="青豆" then 313
when type="绿豆" then 314
when type="黑豆" then 315
when type="蚕豆" then 316
when type="芸豆" then 317
when type="红腰豆" then 318
when type="白豆" then 319
when type="赤小豆" then 320
when type="花豆" then 321
when type="豌豆粒" then 322
when type="白扁豆" then 323
when type="鲜豌豆" then 324
when type="山药豆" then 325
when type="鹰嘴豆" then 326
when type="豆腐" then 328
when type="豆腐干" then 329
when type="腐竹" then 330
when type="千张" then 331
when type="豆腐丝" then 332
when type="豆腐皮" then 333
when type="豆豉" then 334
when type="苹果" then 336
when type="香蕉" then 337
when type="柠檬" then 338
when type="菠萝" then 339
when type="草莓" then 340
when type="山楂" then 341
when type="梨" then 342
when type="李子" then 343
when type="猕猴桃" then 344
when type="柚子" then 345
when type="芒果" then 346
when type="柿子" then 347
when type="荔枝" then 348
when type="石榴" then 349
when type="葡萄" then 350
when type="樱桃" then 351
when type="西瓜" then 352
when type="木瓜" then 353
when type="火龙果" then 354
when type="椰子" then 355
when type="无花果" then 356
when type="桂圆" then 357
when type="西瓜皮" then 358
when type="桑葚" then 359
when type="桃" then 360
when type="蔓越莓" then 361
when type="香瓜" then 362
when type="金桔" then 363
when type="杨梅" then 364
when type="蓝莓" then 365
when type="牛油果" then 366
when type="桔子" then 367
when type="杨桃" then 368
when type="百香果" then 369
when type="哈密瓜" then 370
when type="榴莲" then 371
when type="甘蔗" then 372
when type="佛手柑" then 373
when type="柑桔" then 374
when type="樱桃番茄" then 375
when type="橙" then 376
when type="鸭梨" then 377
when type="雪莲果" then 378
when type="覆盆子" then 379
when type="黑橄榄" then 380
when type="枇杷" then 381
when type="葡萄柚" then 382
when type="树莓" then 383
when type="香梨" then 384
when type="车厘子" then 385
when type="提子" then 386
when type="花生" then 388
when type="腰果" then 389
when type="松子" then 390
when type="核桃" then 391
when type="芝麻" then 392
when type="杏仁" then 393
when type="莲子" then 394
when type="榛子" then 395
when type="夏威夷果" then 396
when type="海底椰" then 397
when type="红枣" then 398
when type="南瓜子" then 399
when type="开心果" then 400
when type="板栗" then 401
when type="白果" then 402
when type="葵花籽仁" then 403
when type="桂圆肉" then 404
when type="山核桃" then 405
when type="葡萄干" then 406
when type="亚麻籽" then 407
when type="黑芝麻" then 408
when type="蜜枣" then 409
when type="柿饼" then 410
when type="荞麦面" then 412
when type="面包" then 413
when type="米饭" then 414
when type="粉丝" then 415
when type="米粉" then 416
when type="全麦粉" then 417
when type="小麦面粉" then 418
when type="燕麦片" then 419
when type="淀粉" then 420
when type="大米粥" then 421
when type="麦芽" then 423
when type="大米" then 424
when type="糯米" then 425
when type="黑米" then 426
when type="小米" then 427
when type="小麦" then 428
when type="玉米" then 429
when type="西米" then 430
when type="薏米" then 431
when type="燕麦" then 432
when type="红豆" then 433
when type="紫米" then 434
when type="糙米" then 435
when type="香米" then 436
when type="荞麦" then 437
when type="高粱米" then 438
when type="黄米" then 439
when type="大麦" then 440
when type="粳米" then 441
when type="鸭血糯" then 442
when type="红曲" then 443
when type="燕窝" then 445
when type="人参" then 446
when type="香椿" then 447
when type="桂花" then 448
when type="紫苏" then 449
when type="穿心莲" then 450
when type="罗汉果" then 451
when type="金银花" then 452
when type="鱼腥草" then 453
when type="石耳" then 454
when type="枸杞子" then 455
when type="麦冬" then 456
when type="葛根" then 457
when type="黄芪" then 458
when type="枸杞叶" then 459
when type="决明子" then 460
when type="当归" then 461
when type="乌梅" then 462
when type="田七" then 463
when type="芡实" then 464
when type="紫苏叶" then 465
when type="金樱子" then 466
when type="甘草" then 467
when type="桂皮" then 468
when type="薄荷" then 469
when type="沙参" then 470
when type="荷叶" then 471
when type="西洋参" then 472
when type="肉桂" then 473
when type="陈皮" then 474
when type="茯苓" then 475
when type="白芷" then 476
when type="灵芝" then 477
when type="玉竹" then 478
when type="干黄花菜" then 479
when type="折耳根" then 480
when type="桔皮" then 481
when type="丁香" then 482
when type="五指毛桃" then 483
when type="党参" then 484
when type="兰香子" then 485
when type="冬虫夏草" then 486
when type="阿胶粉" then 487
when type="土三七" then 488
when type="大黄" then 489
when type="天麻" then 490
when type="橙皮" then 491
when type="白豆蔻" then 492
when type="石斛" then 493
when type="砂仁" then 494
when type="红花" then 495
when type="肉蔻" then 496
when type="艾叶" then 497
when type="草果" then 498
when type="薰衣草" then 499
when type="藏红花" then 500
when type="豆蔻" then 501
when type="野蒜" then 502
when type="鱼胶粉" then 503
when type="鱼腥草叶" then 504
when type="鱼腥草根" then 505
when type="鼠尾草" then 506
when type="阿胶" then 507
when type="蛋白粉" then 508
when type="柚子皮" then 509
when type="玄参" then 510
when type="干姜" then 511
when type="川贝" then 512
when type="蒲公英" then 513
when type="雪莲花" then 514
when type="桃胶" then 515
when type="琥珀" then 516
when type="土茯苓" then 517
when type="玫瑰茄" then 518
when type="五倍子" then 519
when type="荆芥" then 520
when type="迷迭香" then 521
when type="牛蒡子" then 522
when type="紫草" then 523
when type="北芪" then 524
when type="大青叶" then 525
when type="天花粉" then 526
when type="射干" then 527
when type="白参" then 528
when type="乳香" then 529
when type="僵蚕" then 530
when type="全蝎" then 531
when type="桃花" then 532
when type="姜黄" then 533
when type="味精" then 535
when type="红糖" then 536
when type="冰糖" then 537
when type="白糖" then 538
when type="姜" then 539
when type="醋" then 540
when type="豆瓣酱" then 541
when type="番茄酱" then 542
when type="山葵" then 543
when type="辣根" then 544
when type="干辣椒" then 545
when type="胡椒" then 546
when type="芥末" then 547
when type="咖喱" then 548
when type="芝麻油" then 549
when type="胡椒粉" then 550
when type="花椒" then 551
when type="酱油" then 552
when type="茴香籽" then 553
when type="八角" then 554
when type="猪油" then 555
when type="花生油" then 556
when type="苏打粉" then 557
when type="料酒" then 558
when type="蚝油" then 559
when type="孜然" then 560
when type="巧克力" then 562
when type="金枪鱼罐头" then 563
when type="红豆沙" then 564
when type="麦芽糖" then 565
when type="爆米花" then 566
when type="牛奶" then 568
when type="酸奶" then 569
when type="豆浆" then 570
when type="蜂蜜" then 571
when type="绿茶" then 572
when type="可可粉" then 573
when type="藕粉" then 574
when type="江米酒" then 575
when type="茶叶" then 576
when type="黄酒" then 577
when type="花茶" then 578
when type="普洱茶" then 579
when type="柠檬水" then 580
when type="玫瑰花茶" then 581
when type="红茶" then 582
when type="花粉" then 583
when type="菊花茶" then 584
when type="铁观音" then 585
when type="大麦茶" then 586
when type="柚子茶" then 587
when type="苹果醋" then 588
when type="柠檬茶" then 589
when type="桑葚酒" then 590
when type="龙井茶" then 591
end as type_code,
`img` ,
`raw_detail` ,
`cookbook_make`,
`crawler_date`,
`partition_date`,
now() as `cdc_sync_date`
from ods_foods.ods_foods_db_spider_t_foods;

CREATE TABLE `dwd_foods`.`dwd_foods_db_foods_t_resume` (
  `id` int,
  type1 int,
  type2 int,
  type3 int,
  `created_time`  timestamp,
  `last_update`  timestamp,
  `user_id` int,
  `cdc_sync_date` timestamp
) PARTITIONED BY (partition_date string);



-- 获取最新简历到dwd
select 
`id`,
type1,
type2,
type3,
`created_time`  ,
`last_update` ,
`user_id` ,
`partition_date`,
now() as `cdc_sync_date`
from (select *, row_number() over (distribute by id sort by last_update DESC ) as rank from `ods_foods`.`ods_foods_db_foods_t_resume`) t1
where t1.rank = 1;

