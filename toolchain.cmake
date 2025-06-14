set(CMAKE_SYSTEM_NAME Generic)
#set(CMAKE_SYSTEM_PROCESSOR RISC-V)
set(CMAKE_SYSTEM_PROCESSOR ARMV11)

set(TOOLCHAIN_DIR "/home/batyrshin/work/symbian/arm-2012.03-42-arm-none-symbianelf-i686-pc-linux-gnu/arm-2012.03/bin")

set(BINUTILS_PATH ${TOOLCHAIN_DIR})

set(TOOLCHAIN_PREFIX ${TOOLCHAIN_DIR}/arm-none-symbianelf-)

set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

set(CMAKE_C_COMPILER "${TOOLCHAIN_PREFIX}gcc")
set(CMAKE_ASM_COMPILER  "${TOOLCHAIN_PREFIX}gcc")
set(CMAKE_CXX_COMPILER "${TOOLCHAIN_PREFIX}g++")

set(CMAKE_OBJCOPY ${TOOLCHAIN_PREFIX}objcopy CACHE INTERNAL "objcopy tool")
set(CMAKE_SIZE_UTIL ${TOOLCHAIN_PREFIX}size CACHE INTERNAL "size tool")

set(CMAKE_FIND_ROOT_PATH ${BINUTILS_PATH})
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

#set(SYMBIAN_SDK_PATH "/home/batyrshin/secdisk2/work/symbian/S60_3rd_SDK_MR_API_Plug-In_Pack_v5_43")