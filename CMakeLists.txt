cmake_minimum_required(VERSION 3.20)

# Optional: print out extra messages to see what is going on. Comment it to have less verbose messages
set(CMAKE_VERBOSE_MAKEFILE ON)

# Path to toolchain file. This one has to be before 'project()' below
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/toolchain.cmake)

if(CMAKE_HOST_WIN32)
	message("Build in Windows host")
	set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/toolchain.win.cmake)
	#set(ch32tools "A:/work/ch32/ch32tools/ch32v307/C++/Use MRS Create C++ project-example/CH32V307VCT6")
#elseif(CMAKE_HOST_APPLE)
#message("Host is macOS.")
elseif(CMAKE_HOST_UNIX)
	message("Build for Linux host")
	set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/toolchain.unix.cmake)
	#set(ch32tools "/home/batyrshin/secdisk2/work/ch32/ch32tools/ch32v307/C++/Use MRS Create C++ project-example/CH32V307VCT6")
endif()

set(GIT_HEAD_FILE "${CMAKE_CURRENT_SOURCE_DIR}/.git/HEAD")

project(kernel C CXX ASM)

#add_subdirectory(brdbootldr)
#add_subdirectory(bsptemplate)
#add_subdirectory(halservices)
add_subdirectory(kernel/eka)
#add_subdirectory(kerneltest)
#add_subdirectory(userlibandfileserver)
