FROM ubuntu:20.04
COPY /dist .
ENTRYPOINT ["./test"] 
