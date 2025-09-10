cmake_minimum_required(VERSION 3.20)

# Optional: print out extra messages to see what is going on. Comment it to have less verbose messages
set(CMAKE_VERBOSE_MAKEFILE ON)

# Path to toolchain file. This one has to be before 'project()' below
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/../../../../toolchain.cmake)
set(GIT_HEAD_FILE "${CMAKE_CURRENT_SOURCE_DIR}/.git/HEAD")

project(memmodel C CXX ASM)

#set(PATH_TO_SDK ${CMAKE_SOURCE_DIR}/../../cmsis CACHE PATH "Path to foled with sdk for chip of stm32f1X")

set(memmodel ${PROJECT_NAME}.ldd)
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
################# memmodel ##############################
#/oss.FCL.sf.os.kernelhwsrv/kernel/eka/memmodel/memmodel.mmp
set(MEMMODEL_LIB_NAME memmodel)
set(SOURCE_FILES
    ./epoc/putils.cpp 
    ./epoc/pcodeseg.cpp 
    ./epoc/pprocess.cpp 
    ./epoc/pglobals.cpp
    ./epoc/nvram.cpp
    
    ./epoc/mmubase/ramalloc.cpp 
    ./epoc/mmubase/mmubase.cpp 
    ./epoc/mmubase/kblockmap.cpp 
    ./epoc/mmubase/defragbase.cpp

    ./epoc/moving/mchunk.cpp 
    ./epoc/moving/mglobals.cpp 
    ./epoc/moving/minit.cpp 
    ./epoc/moving/mkernel.cpp
    ./epoc/moving/mcodeseg.cpp 
    ./epoc/moving/mmu.cpp 
    ./epoc/moving/mprocess.cpp
    ./epoc/moving/mutils.cpp 
    ./epoc/moving/mdefrag.cpp

    ./epoc/moving/arm/xglobals.cpp 
    ./epoc/moving/arm/xinit.cpp 
    ./epoc/moving/arm/xipc.cia 
    ./epoc/moving/arm/xkernel.cpp 
    ./epoc/moving/arm/xkernel.cia
    ./epoc/moving/arm/xmmu.cpp 
    ./epoc/moving/arm/xmmu.cia 
    ./epoc/moving/arm/xsched.cpp 
    ./epoc/moving/arm/xsched.cia
    
    ./epoc/direct/mchunk.cpp 
    ./epoc/direct/mglobals.cpp 
    ./epoc/direct/minit.cpp 
    ./epoc/direct/mkernel.cpp
    ./epoc/direct/mcodeseg.cpp 
    ./epoc/direct/mprocess.cpp 
    ./epoc/direct/mutils.cpp 
    ./epoc/direct/mdefrag.cpp

    ./epoc/direct/arm/xglobals.cpp 
    ./epoc/direct/arm/xinit.cpp 
    ./epoc/direct/arm/xipc.cia 
    ./epoc/direct/arm/xkernel.cpp
    ./epoc/direct/arm/xsched.cpp 
    ./epoc/direct/arm/xsched.cia 
    ./epoc/direct/arm/xutils.cpp

    ./epoc/multiple/mchunk.cpp 
    ./epoc/multiple/mglobals.cpp 
    ./epoc/multiple/minit.cpp 
    ./epoc/multiple/mkernel.cpp
    ./epoc/multiple/mcodeseg.cpp 
    ./epoc/multiple/mmu.cpp 
    ./epoc/multiple/mprocess.cpp
    ./epoc/multiple/mutils.cpp 
    ./epoc/multiple/mdefrag.cpp

    ./epoc/multiple/arm/xglobals.cpp 
    ./epoc/multiple/arm/xinit.cpp 
    ./epoc/multiple/arm/xipc.cia 
    ./epoc/multiple/arm/xkernel.cpp 
    ./epoc/multiple/arm/xkernel.cia
    ./epoc/multiple/arm/xmmu.cpp 
    ./epoc/multiple/arm/xmmu.cia 
    ./epoc/multiple/arm/xsched.cpp 
    ./epoc/multiple/arm/xsched.cia

	./epoc/flexible/mchunk.cpp 
    ./epoc/flexible/minit.cpp 
    ./epoc/flexible/mkernel.cpp
	./epoc/flexible/mcodeseg.cpp 
    ./epoc/flexible/mprocess.cpp 
    ./epoc/flexible/mshbuf.cpp
	
    ./epoc/flexible/mmu/mmu.cpp
    ./epoc/flexible/mmu/mvalloc.cpp 
    ./epoc/flexible/mmu/mptalloc.cpp 
    ./epoc/flexible/mmu/mpdalloc.cpp 
    ./epoc/flexible/mmu/mm.cpp
    ./epoc/flexible/mmu/maddrcont.cpp 
    ./epoc/flexible/mmu/mpagearray.cpp 
    ./epoc/flexible/mmu/mslaballoc.cpp
    ./epoc/flexible/mmu/mobject.cpp 
    ./epoc/flexible/mmu/mmapping.cpp 
    ./epoc/flexible/mmu/mmappinglist.cpp
    ./epoc/flexible/mmu/mmanager.cpp 
    ./epoc/flexible/mmu/maddressspace.cpp 
    ./epoc/flexible/mmu/mcleanup.cpp
    ./epoc/flexible/mmu/mpager.cpp 
    ./epoc/flexible/mmu/mrom.cpp 
    ./epoc/flexible/mmu/mdatapaging.cpp 
    ./epoc/flexible/mmu/mcodepaging.cpp
    ./epoc/flexible/mmu/mexport.cpp 
    ./epoc/flexible/mmu/mthrash.cpp
    ./epoc/flexible/mmu/mdefrag.cpp 
    ./epoc/flexible/mmu/mlargemappings.cpp
    ./epoc/flexible/mmu/mpagecleaner.cpp
		
    ./epoc/mmubase/kblockmap.cpp 
    ./epoc/mmubase/ramalloc.cpp 
    ./epoc/mmubase/defragbase.cpp

    ./epoc/flexible/arm/xinit.cpp 
    ./epoc/flexible/arm/xipc.cpp 
    ./epoc/flexible/arm/xipc.cia 
    ./epoc/flexible/arm/xkernel.cpp 
    ./epoc/flexible/arm/xkernel.cia 
    ./epoc/flexible/arm/xsched.cpp 
    ./epoc/flexible/arm/xsched.cia

    ./epoc/flexible/mmu/arm/xmmu.cpp 
    ./epoc/flexible/mmu/arm/xmmu.cia
)

set(INCLUDE_FILES 
    ./kern_int.mmh)
#    ../nkern/nkern.mmp)

add_executable(${MEMMODEL_LIB_NAME} ${SOURCE_FILES})# ${INCLUDE_FILES})

set(EPOC_KERNEL_DIR 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

message("INCLUDEDIR:${CMAKE_CURRENT_SOURCE_DIR}/../../include, ${EPOC_KERNEL_DIR}")
target_include_directories(${MEMMODEL_LIB_NAME} PUBLIC 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/ 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/nkern/arm 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel 
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/kernel/arm
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/dummy_genexec/epoc32/include/
                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/dummy_genexec/epoc32/include/kernel

                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/flexible/mmu/arm

                            ${CMAKE_CURRENT_SOURCE_DIR}/../include/memmodel/epoc/flexible/mmu

                            ${EPOC_KERNEL_DIR})


target_compile_definitions(${MEMMODEL_LIB_NAME} PUBLIC
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


target_compile_options(${MEMMODEL_LIB_NAME} PUBLIC
                                -fpermissive 
                                )

###############################################
