#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_14348 = ref_278 # MOV operation
ref_15339 = ref_14348 # MOV operation
ref_15345 = (0x1F02C962 | ref_15339) # OR operation
ref_16616 = ref_15345 # MOV operation
ref_16622 = (0x1F8797B2 & ref_16616) # AND operation
ref_17216 = ref_16622 # MOV operation
ref_26206 = ref_278 # MOV operation
ref_31033 = ref_17216 # MOV operation
ref_31640 = ref_26206 # MOV operation
ref_31644 = ref_31033 # MOV operation
ref_31646 = (ref_31644 & ref_31640) # AND operation
ref_32240 = ref_31646 # MOV operation
ref_41230 = ref_278 # MOV operation
ref_42476 = ref_41230 # MOV operation
ref_42482 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_42476)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_47970 = ref_32240 # MOV operation
ref_48569 = ref_47970 # MOV operation
ref_48583 = (ref_48569 >> (0x7 & 0x3F)) # SHR operation
ref_54074 = ref_32240 # MOV operation
ref_54673 = ref_54074 # MOV operation
ref_54687 = ((ref_54673 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55064 = ref_48583 # MOV operation
ref_55068 = ref_54687 # MOV operation
ref_55070 = (ref_55068 | ref_55064) # OR operation
ref_55957 = ref_42482 # MOV operation
ref_55961 = ref_55070 # MOV operation
ref_55963 = ((ref_55961 + ref_55957) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_56558 = ref_55963 # MOV operation
ref_107477 = ref_56558 # MOV operation
ref_114448 = ref_56558 # MOV operation
ref_115310 = ref_107477 # MOV operation
ref_115314 = ref_114448 # MOV operation
ref_115316 = ((ref_115314 + ref_115310) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_115911 = ref_115316 # MOV operation
ref_129274 = ref_56558 # MOV operation
ref_135351 = ref_32240 # MOV operation
ref_136597 = ref_135351 # MOV operation
ref_136603 = (0x7 & ref_136597) # AND operation
ref_137227 = ref_136603 # MOV operation
ref_137241 = ((ref_137227 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_137618 = ref_129274 # MOV operation
ref_137622 = ref_137241 # MOV operation
ref_137624 = (ref_137622 | ref_137618) # OR operation
ref_138218 = ref_137624 # MOV operation
ref_138220 = ((ref_138218 >> 56) & 0xFF) # Byte reference - MOV operation
ref_138221 = ((ref_138218 >> 48) & 0xFF) # Byte reference - MOV operation
ref_138222 = ((ref_138218 >> 40) & 0xFF) # Byte reference - MOV operation
ref_138223 = ((ref_138218 >> 32) & 0xFF) # Byte reference - MOV operation
ref_138224 = ((ref_138218 >> 24) & 0xFF) # Byte reference - MOV operation
ref_138225 = ((ref_138218 >> 16) & 0xFF) # Byte reference - MOV operation
ref_138226 = ((ref_138218 >> 8) & 0xFF) # Byte reference - MOV operation
ref_138227 = (ref_138218 & 0xFF) # Byte reference - MOV operation
ref_149311 = ref_138220 # MOVZX operation
ref_149655 = (ref_149311 & 0xFF) # MOVZX operation
ref_170167 = ref_138227 # MOVZX operation
ref_170511 = (ref_170167 & 0xFF) # MOVZX operation
ref_170513 = (ref_170511 & 0xFF) # Byte reference - MOV operation
ref_181596 = (ref_149655 & 0xFF) # MOVZX operation
ref_181940 = (ref_181596 & 0xFF) # MOVZX operation
ref_181942 = (ref_181940 & 0xFF) # Byte reference - MOV operation
ref_191007 = ref_17216 # MOV operation
ref_198617 = ((((((((ref_170513) << 8 | ref_138221) << 8 | ref_138222) << 8 | ref_138223) << 8 | ref_138224) << 8 | ref_138225) << 8 | ref_138226) << 8 | ref_181942) # MOV operation
ref_204055 = ref_32240 # MOV operation
ref_204662 = ref_198617 # MOV operation
ref_204666 = ref_204055 # MOV operation
ref_204668 = (ref_204666 & ref_204662) # AND operation
ref_205939 = ref_204668 # MOV operation
ref_205945 = (0x1F & ref_205939) # AND operation
ref_206569 = ref_205945 # MOV operation
ref_206583 = ((ref_206569 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_206960 = ref_191007 # MOV operation
ref_206964 = ref_206583 # MOV operation
ref_206966 = (ref_206964 | ref_206960) # OR operation
ref_207560 = ref_206966 # MOV operation
ref_226577 = ref_115911 # MOV operation
ref_233548 = ref_115911 # MOV operation
ref_234410 = ref_226577 # MOV operation
ref_234414 = ref_233548 # MOV operation
ref_234416 = ((ref_234414 + ref_234410) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_235011 = ref_234416 # MOV operation
ref_248374 = ref_235011 # MOV operation
ref_254451 = ((((((((ref_170513) << 8 | ref_138221) << 8 | ref_138222) << 8 | ref_138223) << 8 | ref_138224) << 8 | ref_138225) << 8 | ref_138226) << 8 | ref_181942) # MOV operation
ref_255697 = ref_254451 # MOV operation
ref_255703 = (0x7 & ref_255697) # AND operation
ref_256327 = ref_255703 # MOV operation
ref_256341 = ((ref_256327 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_256718 = ref_248374 # MOV operation
ref_256722 = ref_256341 # MOV operation
ref_256724 = (ref_256722 | ref_256718) # OR operation
ref_257318 = ref_256724 # MOV operation
ref_257320 = ((ref_257318 >> 56) & 0xFF) # Byte reference - MOV operation
ref_257321 = ((ref_257318 >> 48) & 0xFF) # Byte reference - MOV operation
ref_257322 = ((ref_257318 >> 40) & 0xFF) # Byte reference - MOV operation
ref_257323 = ((ref_257318 >> 32) & 0xFF) # Byte reference - MOV operation
ref_257324 = ((ref_257318 >> 24) & 0xFF) # Byte reference - MOV operation
ref_257325 = ((ref_257318 >> 16) & 0xFF) # Byte reference - MOV operation
ref_257326 = ((ref_257318 >> 8) & 0xFF) # Byte reference - MOV operation
ref_257327 = (ref_257318 & 0xFF) # Byte reference - MOV operation
ref_268411 = ref_257320 # MOVZX operation
ref_268755 = (ref_268411 & 0xFF) # MOVZX operation
ref_289267 = ref_257327 # MOVZX operation
ref_289611 = (ref_289267 & 0xFF) # MOVZX operation
ref_289613 = (ref_289611 & 0xFF) # Byte reference - MOV operation
ref_300696 = (ref_268755 & 0xFF) # MOVZX operation
ref_301040 = (ref_300696 & 0xFF) # MOVZX operation
ref_301042 = (ref_301040 & 0xFF) # Byte reference - MOV operation
ref_310107 = ref_207560 # MOV operation
ref_317717 = ((((((((ref_289613) << 8 | ref_257321) << 8 | ref_257322) << 8 | ref_257323) << 8 | ref_257324) << 8 | ref_257325) << 8 | ref_257326) << 8 | ref_301042) # MOV operation
ref_323155 = ((((((((ref_170513) << 8 | ref_138221) << 8 | ref_138222) << 8 | ref_138223) << 8 | ref_138224) << 8 | ref_138225) << 8 | ref_138226) << 8 | ref_181942) # MOV operation
ref_323762 = ref_317717 # MOV operation
ref_323766 = ref_323155 # MOV operation
ref_323768 = (ref_323766 & ref_323762) # AND operation
ref_325039 = ref_323768 # MOV operation
ref_325045 = (0x1F & ref_325039) # AND operation
ref_325669 = ref_325045 # MOV operation
ref_325683 = ((ref_325669 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_326060 = ref_310107 # MOV operation
ref_326064 = ref_325683 # MOV operation
ref_326066 = (ref_326064 | ref_326060) # OR operation
ref_326660 = ref_326066 # MOV operation
ref_344664 = ((((((((ref_170513) << 8 | ref_138221) << 8 | ref_138222) << 8 | ref_138223) << 8 | ref_138224) << 8 | ref_138225) << 8 | ref_138226) << 8 | ref_181942) # MOV operation
ref_349491 = ((((((((ref_289613) << 8 | ref_257321) << 8 | ref_257322) << 8 | ref_257323) << 8 | ref_257324) << 8 | ref_257325) << 8 | ref_257326) << 8 | ref_301042) # MOV operation
ref_349843 = ref_344664 # MOV operation
ref_349847 = ref_349491 # MOV operation
ref_349849 = (ref_349847 | ref_349843) # OR operation
ref_351120 = ref_349849 # MOV operation
ref_351126 = (0xF & ref_351120) # AND operation
ref_352142 = ref_351126 # MOV operation
ref_352148 = (0x1 | ref_352142) # OR operation
ref_357639 = ref_32240 # MOV operation
ref_358238 = ref_357639 # MOV operation
ref_358252 = (ref_358238 >> (0x1 & 0x3F)) # SHR operation
ref_359523 = ref_358252 # MOV operation
ref_359529 = (0xF & ref_359523) # AND operation
ref_360545 = ref_359529 # MOV operation
ref_360551 = (0x1 | ref_360545) # OR operation
ref_365403 = ref_326660 # MOV operation
ref_366002 = ref_365403 # MOV operation
ref_366014 = ref_360551 # MOV operation
ref_366016 = (ref_366002 >> ((ref_366014 & 0xFF) & 0x3F)) # SHR operation
ref_371507 = ref_32240 # MOV operation
ref_372106 = ref_371507 # MOV operation
ref_372120 = (ref_372106 >> (0x1 & 0x3F)) # SHR operation
ref_373391 = ref_372120 # MOV operation
ref_373397 = (0xF & ref_373391) # AND operation
ref_374413 = ref_373397 # MOV operation
ref_374419 = (0x1 | ref_374413) # OR operation
ref_375694 = ref_374419 # MOV operation
ref_375696 = ((0x40 - ref_375694) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_375704 = ref_375696 # MOV operation
ref_380551 = ref_326660 # MOV operation
ref_381150 = ref_380551 # MOV operation
ref_381162 = ref_375704 # MOV operation
ref_381164 = ((ref_381150 << ((ref_381162 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_381541 = ref_366016 # MOV operation
ref_381545 = ref_381164 # MOV operation
ref_381547 = (ref_381545 | ref_381541) # OR operation
ref_382171 = ref_381547 # MOV operation
ref_382183 = ref_352148 # MOV operation
ref_382185 = ((ref_382171 << ((ref_382183 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_387037 = ((((((((ref_170513) << 8 | ref_138221) << 8 | ref_138222) << 8 | ref_138223) << 8 | ref_138224) << 8 | ref_138225) << 8 | ref_138226) << 8 | ref_181942) # MOV operation
ref_391864 = ((((((((ref_289613) << 8 | ref_257321) << 8 | ref_257322) << 8 | ref_257323) << 8 | ref_257324) << 8 | ref_257325) << 8 | ref_257326) << 8 | ref_301042) # MOV operation
ref_392216 = ref_387037 # MOV operation
ref_392220 = ref_391864 # MOV operation
ref_392222 = (ref_392220 | ref_392216) # OR operation
ref_393493 = ref_392222 # MOV operation
ref_393499 = (0xF & ref_393493) # AND operation
ref_394515 = ref_393499 # MOV operation
ref_394521 = (0x1 | ref_394515) # OR operation
ref_395796 = ref_394521 # MOV operation
ref_395798 = ((0x40 - ref_395796) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_395806 = ref_395798 # MOV operation
ref_401292 = ref_32240 # MOV operation
ref_401891 = ref_401292 # MOV operation
ref_401905 = (ref_401891 >> (0x1 & 0x3F)) # SHR operation
ref_403176 = ref_401905 # MOV operation
ref_403182 = (0xF & ref_403176) # AND operation
ref_404198 = ref_403182 # MOV operation
ref_404204 = (0x1 | ref_404198) # OR operation
ref_409056 = ref_326660 # MOV operation
ref_409655 = ref_409056 # MOV operation
ref_409667 = ref_404204 # MOV operation
ref_409669 = (ref_409655 >> ((ref_409667 & 0xFF) & 0x3F)) # SHR operation
ref_415160 = ref_32240 # MOV operation
ref_415759 = ref_415160 # MOV operation
ref_415773 = (ref_415759 >> (0x1 & 0x3F)) # SHR operation
ref_417044 = ref_415773 # MOV operation
ref_417050 = (0xF & ref_417044) # AND operation
ref_418066 = ref_417050 # MOV operation
ref_418072 = (0x1 | ref_418066) # OR operation
ref_419347 = ref_418072 # MOV operation
ref_419349 = ((0x40 - ref_419347) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_419357 = ref_419349 # MOV operation
ref_424204 = ref_326660 # MOV operation
ref_424803 = ref_424204 # MOV operation
ref_424815 = ref_419357 # MOV operation
ref_424817 = ((ref_424803 << ((ref_424815 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_425194 = ref_409669 # MOV operation
ref_425198 = ref_424817 # MOV operation
ref_425200 = (ref_425198 | ref_425194) # OR operation
ref_425824 = ref_425200 # MOV operation
ref_425836 = ref_395806 # MOV operation
ref_425838 = (ref_425824 >> ((ref_425836 & 0xFF) & 0x3F)) # SHR operation
ref_426215 = ref_382185 # MOV operation
ref_426219 = ref_425838 # MOV operation
ref_426221 = (ref_426219 | ref_426215) # OR operation
ref_426815 = ref_426221 # MOV operation
ref_427817 = ref_426815 # MOV operation
ref_427819 = ref_427817 # MOV operation

print ref_427819 & 0xffffffffffffffff