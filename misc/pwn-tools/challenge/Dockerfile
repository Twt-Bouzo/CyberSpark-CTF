#in case the task requeries python to be installed:
#FROM python:3.9-slim-buster
#else if its just a system : 
FROM ubuntu:22.04

RUN apt-get install libc6
# Install some libs
RUN apt-get update && apt-get -y upgrade

Run apt-get install -y g++
# create ctf-user
RUN  groupadd -r ctf && useradd -r -g ctf ctf
#libs
COPY src.cpp /home/ctf/
COPY Pwn_tools /home/ctf/ 
COPY launch.sh /home/ctf/
COPY ynetd /home/ctf/
#set some proper permissions
#RUN pip install inputimeout 
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/src.cpp
RUN chmod 750 /home/ctf/ynetd
RUN chmod 750 /home/ctf/launch.sh
WORKDIR /home/ctf/
RUN g++ -o pwn_tools src.cpp
USER ctf
EXPOSE 2024

CMD /home/ctf/ynetd -p 2024 /home/ctf/launch.sh
