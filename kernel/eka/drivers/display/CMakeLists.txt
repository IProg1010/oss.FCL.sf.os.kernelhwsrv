cmake_minimum_required(VERSION 3.20)

# Optional: print out extra messages to see what is going on. Comment it to have less verbose messages
set(CMAKE_VERBOSE_MAKEFILE ON)

# Path to toolchain file. This one has to be before 'project()' below
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/../../../../toolchain.cmake)
set(GIT_HEAD_FILE "${CMAKE_CURRENT_SOURCE_DIR}/.git/HEAD")

project(display_eka C CXX ASM)

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
set(SOURCE_FILES
	display.cpp
	)

set(INCLUDE_FILES 
    ../../kernel/kern_ext.mmh)

add_library(${LIBRARY} ${SOURCE_FILES} ${INCLUDE_FILES})

set(EPOC_KERNEL_DIR 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../kernel)

target_include_directories(${LIBRARY} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} ${EPOC_KERNEL_DIR})
