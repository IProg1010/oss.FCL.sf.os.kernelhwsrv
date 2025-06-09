cmake_minimum_required(VERSION 3.20)

# Optional: print out extra messages to see what is going on. Comment it to have less verbose messages
set(CMAKE_VERBOSE_MAKEFILE ON)

# Path to toolchain file. This one has to be before 'project()' below
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/toolchain.cmake)
set(GIT_HEAD_FILE "${CMAKE_CURRENT_SOURCE_DIR}/.git/HEAD")

project(kernel C CXX ASM)

#set(PATH_TO_SDK ${CMAKE_SOURCE_DIR}/../../cmsis CACHE PATH "Path to foled with sdk for chip of stm32f1X")

set(EXECUTABLE ${PROJECT_NAME}.elf)
#set(LINKER_FILE ${CMAKE_SOURCE_DIR}/memory_link.ld)

set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_C_STANDARD 11)
set(CMAKE_ASM_FLAGS "-x assembler-with-cpp")
#set_property(SOURCE startup_stm32f103xb.s APPEND PROPERTY COMPILE_OPTIONS "-x" "assembler-with-cpp")

message("PAth to ${PATH_TO_SDK}")
message("Cmake source dir" ${CMAKE_SOURCE_DIR})

include_directories(/usr/include/)

add_subdirectory(src)

# List of source files
#set(SOURCE_FILE 
#	${CMAKE_SOURCE_DIR}/main.cpp

#	)
#set(SOURCE_FILE 
#    ${CMAKE_SOURCE_DIR}/main.cpp

#    )

#Build the executable based on the source files
add_executable(${EXECUTABLE} ${SOURCE_FILE})

# List of compiler defines, prefix with -D compiler option
target_compile_definitions(${EXECUTABLE} PRIVATE
	-D__DEBUG_MODE__
	)

# List of includ directories
target_include_directories(${EXECUTABLE} PUBLIC
	${CMAKE_SOURCE_DIR}/inc
	${CMAKE_SOURCE_DIR}/
	)

include_directories(
	${CMAKE_SOURCE_DIR}/
	)

# Compiler options
#target_compile_options(${EXECUTABLE} PRIVATE
	#-mcpu=
	#-mthumb
	#-march=rv32i_zicsr
	#-S -o
	#-march=rv32imac_zicsr_zifencei
	#-with-arch=rv32gc
	#-march=rv32imac_zicsr
#	-Wall
#	-g 
#	-Os 
#	-flto 
#	-ffunction-sections 
#	-fdata-sections 
#	-fmessage-length=0 
	#-msmall-data-limit=8
	#-march=rv32imafc 
	#-mabi=ilp32f
#	-static-libgcc 
#	-DCH32V30x_D8C
	#-nostdlib
#	-Wall
#	-O1
	#-specs=nosys.specs
#	)

# Linker options
#target_link_options(${EXECUTABLE} PUBLIC
#	-T${LINKER_FILE}
	#-mcpu=cortex-m4
	#-mthumb
	#-specs=nano.specs
#	-specs=nano.specs 
#	-specs=nosys.specs
#	-Wl,--gc-sections
#	-lgcc
#	-nostartfiles
	#-static-libgcc
#	-lstdc++
#	-lg
#	-u _printf_float #for ptintf float
	#-u _scanf_float #for scanf float
#	-lc
#	-Dformat-default=float
#	)

add_custom_command(TARGET ${EXECUTABLE}
	POST_BUILD
	COMMAND ${CMAKE_SIZE_UTIL} ${EXECUTABLE})

	execute_process(COMMAND git log --pretty=format:'%h' -n 1
	OUTPUT_VARIABLE GIT_REV
	ERROR_QUIET)

if ("${GIT_REV}" STREQUAL "")
	set(GIT_REV "N/A")
	set(GIT_DIFF "")
	set(GIT_TAG "N/A")
	set(GIT_BRANCH "N/A")
else()
	execute_process(
			COMMAND bash -c "git diff --quiet --exit-code || echo +"
			OUTPUT_VARIABLE GIT_DIFF)
	execute_process(
			COMMAND git describe --exact-match --tags
			OUTPUT_VARIABLE GIT_TAG ERROR_QUIET)
	execute_process(
		COMMAND git rev-parse --abbrev-ref HEAD
		OUTPUT_VARIABLE GIT_BRANCH)

	string(STRIP "${GIT_REV}" GIT_REV)
	string(SUBSTRING "${GIT_REV}" 1 7 GIT_REV)
	string(STRIP "${GIT_DIFF}" GIT_DIFF)
	string(STRIP "${GIT_TAG}" GIT_TAG)
	string(STRIP "${GIT_BRANCH}" GIT_BRANCH)
endif()

# Optional: Create hex, bin and S-Record files after the build
add_custom_command(TARGET ${EXECUTABLE}
        POST_BUILD
        COMMAND ${CMAKE_OBJCOPY} -O srec --srec-len=64 ${EXECUTABLE} ${PROJECT_NAME}.s19
        COMMAND ${CMAKE_OBJCOPY} -O ihex ${EXECUTABLE} ${PROJECT_NAME}.hex
        COMMAND ${CMAKE_OBJCOPY} -O binary ${EXECUTABLE} ${PROJECT_NAME}_${GIT_REV}.bin)