
get_filename_component(CMAKE_SOURCE_DIR "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)
if(NOT MSVC)
    set(LINT_COMMAND ${PYTHON2_EXECUTABLE} ${CMAKE_SOURCE_DIR}/3rdparty/lint/cpplint.py --output=vs7)
else()
    if(NOT PYTHON2_EXECUTABLE)
        message(FATAL_ERROR "Cannot lint without python 2")
    endif()
    # format output so VS can bring us to the offending file/line
    set(LINT_COMMAND ${PYTHON2_EXECUTABLE} ${CMAKE_SOURCE_DIR}/3rdparty/lint/cpplint.py --output=vs7)
endif()
set(SRC_FILE_EXTENSIONS h hpp hu c cpp cu cc)
set(EXCLUDE_FILE_EXTENSTIONS pb.h pb.cc)
set(LINT_DIRS include src gui tests)

cmake_policy(SET CMP0009 NEW)  # suppress cmake warning

# find all files of interest
foreach(ext ${SRC_FILE_EXTENSIONS})
    foreach(dir ${LINT_DIRS})
        file(GLOB_RECURSE FOUND_FILES ${CMAKE_SOURCE_DIR}/${dir}/*.${ext})
        set(LINT_SOURCES ${LINT_SOURCES} ${FOUND_FILES})
    endforeach()
endforeach()

# find all files that should be excluded
foreach(ext ${EXCLUDE_FILE_EXTENSTIONS})
    file(GLOB_RECURSE FOUND_FILES ${CMAKE_SOURCE_DIR}/*.${ext})
    set(EXCLUDED_FILES ${EXCLUDED_FILES} ${FOUND_FILES})
endforeach()

# exclude generated pb files
if(EXCLUDED_FILES)
    list(REMOVE_ITEM LINT_SOURCES ${EXCLUDED_FILES})
endif()

MESSAGE("LINT COMMAND = ${LINT_COMMAND}")
MESSAGE("LINT_SOURCES = ${LINT_SOURCES}")

execute_process(
    COMMAND ${LINT_COMMAND} ${LINT_SOURCES}
    ERROR_VARIABLE LINT_OUTPUT
    ERROR_STRIP_TRAILING_WHITESPACE
)

MESSAGE("LINT_OUTPUT = ${LINT_OUTPUT}")

string(REPLACE "\n" ";" LINT_OUTPUT ${LINT_OUTPUT})

list(GET LINT_OUTPUT -1 LINT_RESULT)
list(REMOVE_AT LINT_OUTPUT -1)
string(REPLACE " " ";" LINT_RESULT ${LINT_RESULT})
list(GET LINT_RESULT -1 NUM_ERRORS)
if(NUM_ERRORS GREATER 0)    
    foreach(msg ${LINT_OUTPUT})
        string(FIND ${msg} "Done" result)
        if(result LESS 0)    
            if(MSVC)
              # avoid STATUS since it adds two dashes and prevents
              # VS from properly parsing the messages.
              # TODO: parse ${msg} so that we can add error or warning
              # so that lint errors appear in the Error List. Or maybe
              # should we just modify the cpplint.py?
              message("${msg}")
            else()            
              message(STATUS ${msg})
            endif()
        endif()
    endforeach()
    message(FATAL_ERROR "Lint found ${NUM_ERRORS} errors!")
else()
    message(STATUS "Lint did not find any errors!")
endif()

