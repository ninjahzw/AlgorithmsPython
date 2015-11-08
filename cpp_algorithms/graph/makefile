CXX = g++-4.9
INC = -I.
CPP_ELEVEN =-std=c++14
CC_FLAGS = -Wall
SOURCES = $(wildcard src/*.cpp)
OBJECTS = $(patsubst src/%.cpp,obj/%.o,$(SOURCES))
EXECUTABLE = graph

#-------

all: $(EXECUTABLE) 

$(EXECUTABLE): $(OBJECTS)
	$(CXX) -o $@ $^

obj/%.o: src/%.cpp
	$(CXX) $(CC_FLAGS) ${CPP_ELEVEN} -c $^ -o $@

clean:
	rm -rf obj/*.o
