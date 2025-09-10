cmake_minimum_required(VERSION 3.20)

# Optional: print out extra messages to see what is going on. Comment it to have less verbose messages
set(CMAKE_VERBOSE_MAKEFILE ON)

# Path to toolchain file. This one has to be before 'project()' below
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/../../../../toolchain.cmake)
set(GIT_HEAD_FILE "${CMAKE_CURRENT_SOURCE_DIR}/.git/HEAD")

project(nkernsmp C CXX ASM)

#set(PATH_TO_SDK ${CMAKE_SOURCE_DIR}/../../cmsis CACHE PATH "Path to foled with sdk for chip of stm32f1X")

set(nkernsmp ${PROJECT_NAME}.ldd)
#set(LINKER_FILE ${CMAKE_SOURCE_DIR}/memory_link.ld)

set(CMAKE_CXX_STANDARD 98)
#set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_C_STANDARD 98)
set(CMAKE_ASM_FLAGS "-x assembler-with-cpp")
#set_property(SOURCE startup_stm32f103xb.s APPEND PROPERTY COMPILE_OPTIONS "-x" "assembler-with-cpp")

message("PAth to ${PATH_TO_SDK}")
message("Cmake source dir" ${CMAKE_SOURCE_DIR})

#include_directories(/usr/include/)

#add_subdirectory(src)

# List of source files
################# nkernsmp ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/nkernsmp/nkernsmp.mmp
set(NKERNSMP_LIB_NAME nkernsmp)
set(SOURCE_FILES
    ./nkern.cpp 
    ./nkerns.cpp 
    ./sched.cpp 
    ./dfcs.cpp 
    ./nk_timer.cpp 
    ./nk_irq.cpp 
    ./nk_bal.cpp
    
    ../nkern/nklib.cpp

    ../common/arm/atomics.cia
    ./arm/vectors.cia 
    ./arm/ncsched.cpp 
    ./arm/ncsched.cia 
    ./arm/nctimer.cia 
    ./arm/ncutilf.cia 
    ./arm/ncirq.cpp 
    ./arm/ncirq.cia 
    ./arm/ncthrd.cia

    ./arm/ncutils.cia 
    ./arm/ncutils.cpp 
    ./arm/ncthrd.cpp 
    ./arm/ncglob.cpp 
    ./arm/nccpu.cpp 
    ./arm/nccpu.cia

    ../nkern/arm/nklib.cia
)

set(INCLUDE_FILES 
    ./kern_int.mmh)
#    ../nkern/nkern.mmp)

add_executable(${NKERNSMP_LIB_NAME} ${SOURCE_FILES})# ${INCLUDE_FILES})

set(EPOC_KERNEL_DIR 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
target_include_directories(${NKERNSMP_LIB_NAME} PUBLIC 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel/arm
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/dummy_genexec/epoc32/include/
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/dummy_genexec/epoc32/include/kernel

                            ${EPOC_KERNEL_DIR})


target_compile_definitions(${NKERNSMP_LIB_NAME} PUBLIC
                                __GCC32__=1 
                                __MARM__=1
                                __EABI__=1
                                __KERNEL_MODE__=1
                                #_WIN32=1
                                __EPOC32__=1
                                __GCC32__=1
                                __EXPORT_MEMCPY__=1
                                __IN_KERNEL__=1
                                __REPLACE_GENERIC_UTILS=1
                                __EXPORT_MEMCPY__=1)


target_compile_options(${NKERNSMP_LIB_NAME} PUBLIC
                                -fpermissive 
                                )

#target_link_libraries(${NKERNSMP_LIB_NAME} PUBLIC
#START ARMCC
#ARMRT
#ifdef ARMCC_2
#ARMLIBS					c_a__un.l cpprt_a__u.l
#ifndef ARMCC_2_1
#ARMLIBS					h_a__un.l 
#endif
#else
#ifdef ARMCC_4
#ARMLIBS					c_5.l     h_5.l     cpprt_5.l
#else
#ARMLIBS					c_4.l     h_4.l     cpprt_4.l
#endif
#endif
#END
#)
###############################################
