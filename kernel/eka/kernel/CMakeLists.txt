cmake_minimum_required(VERSION 3.20)

# Optional: print out extra messages to see what is going on. Comment it to have less verbose messages
set(CMAKE_VERBOSE_MAKEFILE ON)

# Path to toolchain file. This one has to be before 'project()' below
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/../../../../toolchain.cmake)
set(GIT_HEAD_FILE "${CMAKE_CURRENT_SOURCE_DIR}/.git/HEAD")

project(kernel C CXX ASM)

#set(PATH_TO_SDK ${CMAKE_SOURCE_DIR}/../../cmsis CACHE PATH "Path to foled with sdk for chip of stm32f1X")

set(LIBRARY ${PROJECT_NAME}.ldd)
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



################# edev ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/edev.mmp
set(EDEV_LIB_NAME edev)
set(SOURCE_FILES
    ../compsupp/rvct/ucppfini.cpp
    ./arm/d_entry.cia
    ./arm/d_entry.cpp
	)

set(INCLUDE_FILES 
    ./kern_int.mmh)

add_library(${EDEV_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

set(EPOC_KERNEL_DIR 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
target_include_directories(${EDEV_LIB_NAME} PUBLIC 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
                            ${EPOC_KERNEL_DIR})


target_compile_definitions(${EDEV_LIB_NAME} PUBLIC
                                __GCC32__=1 
                                __MARM__=1
                                __EABI__=1
                                __KERNEL_MODE__=1
                                _WIN32=1
                                __EPOC32__=1
                                __GCC32__=1)


target_compile_options(${EDEV_LIB_NAME} PUBLIC
                                -fpermissive 
                                )

###############################################

################# eext ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/eext.mmp
set(EEXT_LIB_NAME eext)
set(SOURCE_FILES
    ./arm/x_entry.cia
    ./arm/x_entry.cpp
	)

set(INCLUDE_FILES 
    ./kern_int.mmh)

add_library(${EEXT_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

set(EPOC_KERNEL_DIR 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
target_include_directories(${EEXT_LIB_NAME} PUBLIC 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
                            ${EPOC_KERNEL_DIR})


target_compile_definitions(${EEXT_LIB_NAME} PUBLIC
                                __GCC32__=1 
                                __MARM__=1
                                __EABI__=1
                                __KERNEL_MODE__=1
                                _WIN32=1
                                __EPOC32__=1
                                __GCC32__=1)


target_compile_options(${EEXT_LIB_NAME} PUBLIC
                                -fpermissive 
                                )

###############################################

################# ekernsmp ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/ekern_lib.mmp
#set(EKERNSMP_LIB_NAME ekernsmp)
#set(SOURCE_FILES
#    ./arm/x_entry.cia
#    ./arm/x_entry.cpp
#	)

#set(INCLUDE_FILES 
#    ./kern_int.mmh)

#add_library(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1
#                                __GCC32__=1)


#target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################


################# ekern ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/ekern.mmp
set(EKERNSMP_LIB_NAME ekernsmp)
set(SOURCE_FILES
    #array_eabi.cpp
    
    arm/cglobals.cpp 
    arm/cexec.cpp 
    arm/cexec.cia 
    arm/cinit.cpp
    arm/ckernel.cpp 
    arm/ckernel.cia 
    arm/cipc.cpp 
    arm/cipc.cia 
    arm/csched.cia
    arm/cutils.cpp 
    arm/cutils.cia
    arm/cache.cpp 
    arm/cache_maintenance.cia 
    arm/cache_maintenance.cpp
    arm/cache_maintenancev7.cia 
    arm/cache_external.cpp

    arm/byte_pair.cia

    ../klib/arm/ckdes8.cia 
    ../klib/arm/cumem.cia 
    ../klib/arm/cbma.cia
	../common/arm/carray.cia 
    ../common/arm/cdes8.cia 
    ../common/arm/cmem.cia

    ../common/arm/cgcchelp.cpp 
    ../common/arm/cgcchelp.cia

    sglobals.cpp 
    device.cpp 
    eventq.cpp
    sexec.cpp 
    sinit.cpp 
    skernel.cpp
    scodeseg.cpp 
    sipc.cpp 
    notifier.cpp 
    object.cpp 
    power.cpp 
    server.cpp
    sha256.cpp 
    securerng.cpp
    stimer.cpp 
    sutils.cpp 
    random.cpp
    sprocess.cpp 
    sthread.cpp 
    smqueue.cpp
    sproperty.cpp
    ssharedio.cpp
    ssecure.cpp
    emi.cpp
    objectix.cpp
    sbtrace.cpp
    stest.cpp
    sshbuf.cpp 
    smap.cpp
    srandombuff.cpp
    kerncorestats.cpp

    ../klib/dbase.cpp 
    ../klib/kdes8.cpp
    ../klib/kheap.cpp 
    ../klib/bma.cpp

    ../common/alloc.cpp 
    ../common/array.cpp 
    ../common/des8.cpp 
    ../common/mem.cpp

    ../common/heap_hybrid.cpp 
    ../common/debugfunction.cpp   
    ../common/secure.cpp
    ../common/gcchelp.cpp
)

set(INCLUDE_FILES 
    ./kern_int.mmh)
#    ../nkern/nkern.mmp)

add_executable(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

set(EPOC_KERNEL_DIR 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel/arm
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/dummy_genexec/epoc32/include/
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/dummy_genexec/epoc32/include/kernel
                            ${EPOC_KERNEL_DIR})


target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
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


target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
                                -fpermissive 
                                )

###############################################



################# ekll ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/ekll.mmp
#set(EKERNSMP_LIB_NAME ekernsmp)
#set(SOURCE_FILES
#    ./arm/x_entry.cia
#    ./arm/x_entry.cpp
#	)

#set(INCLUDE_FILES 
#    ./kern_int.mmh)

#add_library(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1
#                                __GCC32__=1)


#target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################



################# evar ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/evar.mmp
#set(EKERNSMP_LIB_NAME ekernsmp)
#set(SOURCE_FILES
#    ./arm/x_entry.cia
#    ./arm/x_entry.cpp
#	)

#set(INCLUDE_FILES 
#    ./kern_int.mmh)

#add_library(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1
#                                __GCC32__=1)


#target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################


################# evfp ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/evfp.mmp
#set(EKERNSMP_LIB_NAME ekernsmp)
#set(SOURCE_FILES
#    ./arm/x_entry.cia
#    ./arm/x_entry.cpp
#	)

#set(INCLUDE_FILES 
#    ./kern_int.mmh)

#add_library(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1
#                                __GCC32__=1)


#target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################



################# exmoncommon_lib ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/exmoncommon_lib.mmp
#set(EKERNSMP_LIB_NAME ekernsmp)
#set(SOURCE_FILES
#    ./arm/x_entry.cia
#    ./arm/x_entry.cpp
#	)

#set(INCLUDE_FILES 
#    ./kern_int.mmh)

#add_library(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1
#                                __GCC32__=1)


#target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################


################# exmoncommon ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/exmoncommon.mmp
#set(EKERNSMP_LIB_NAME ekernsmp)
#set(SOURCE_FILES
#    ./arm/x_entry.cia
#    ./arm/x_entry.cpp
#	)

#set(INCLUDE_FILES 
#    ./kern_int.mmh)

#add_library(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1
#                                __GCC32__=1)


#target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################



################# exmondebug ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/exmondebug.mmp
#set(EKERNSMP_LIB_NAME ekernsmp)
#set(SOURCE_FILES
#    ./arm/x_entry.cia
#    ./arm/x_entry.cpp
#	)

#set(INCLUDE_FILES 
#    ./kern_int.mmh)

#add_library(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1
#                                __GCC32__=1)


#target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################


################# exmonlog ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/exmonlog.mmp
#set(EKERNSMP_LIB_NAME ekernsmp)
#set(SOURCE_FILES
#    ./arm/x_entry.cia
#    ./arm/x_entry.cpp
#	)

#set(INCLUDE_FILES 
#    ./kern_int.mmh)

#add_library(${EKERNSMP_LIB_NAME} ${SOURCE_FILES} ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EKERNSMP_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EKERNSMP_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1
#                                __GCC32__=1)


#target_compile_options(${EKERNSMP_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################


################# exstart ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/exstart.mmp
#set(EXSTAR_LIB_NAME exstart)
#set(SOURCE_FILES
#	exstart.cpp
#	)

#set(INCLUDE_FILES 
#    ../../kernel/kern_ext.mmh)

#add_library(${EXSTAR_LIB_NAME} ${SOURCE_FILES}) # ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#   ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EXSTAR_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EXSTAR_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1)


#target_compile_options(${EXSTAR_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################


################# kc_exe ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/kc_exe.mmp
#set(EXSTAR_LIB_NAME exstart)
#set(SOURCE_FILES
#	exstart.cpp
#	)

#set(INCLUDE_FILES 
#    ../../kernel/kern_ext.mmh)

#add_library(${EXSTAR_LIB_NAME} ${SOURCE_FILES}) # ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#   ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EXSTAR_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EXSTAR_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1)


#target_compile_options(${EXSTAR_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################



################# kdebug ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/kdebug.mmp
#set(EXSTAR_LIB_NAME exstart)
#set(SOURCE_FILES
#	exstart.cpp
#	)

#set(INCLUDE_FILES 
#    ../../kernel/kern_ext.mmh)

#add_library(${EXSTAR_LIB_NAME} ${SOURCE_FILES}) # ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#   ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EXSTAR_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EXSTAR_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1)


#target_compile_options(${EXSTAR_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################


################# kdebugv6 ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/kernel/kdebugv6.mmp
#set(EXSTAR_LIB_NAME exstart)
#set(SOURCE_FILES
#	exstart.cpp
#	)

#set(INCLUDE_FILES 
#    ../../kernel/kern_ext.mmh)

#add_library(${EXSTAR_LIB_NAME} ${SOURCE_FILES}) # ${INCLUDE_FILES})

#set(EPOC_KERNEL_DIR 
#   ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

#message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
#target_include_directories(${EXSTAR_LIB_NAME} PUBLIC 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
#                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
#                            ${EPOC_KERNEL_DIR})


#target_compile_definitions(${EXSTAR_LIB_NAME} PUBLIC
#                                __GCC32__=1 
#                                __MARM__=1
#                                __EABI__=1
#                                __KERNEL_MODE__=1
#                                _WIN32=1
#                                __EPOC32__=1)


#target_compile_options(${EXSTAR_LIB_NAME} PUBLIC
#                                -fpermissive 
#                                )

###############################################
