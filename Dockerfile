FROM ubuntu:20.04
COPY /dist/test /root/test
ENTRYPOINT ["root/test"] 
