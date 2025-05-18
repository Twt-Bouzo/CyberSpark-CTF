FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    build-essential \
    gdb \
    nano \
    && apt clean

# Create low-privilege user
RUN groupadd -r ctf && useradd -r -g ctf ctf

# Copy challenge files
COPY Debug /home/ctf/
COPY launch.sh /home/ctf/
COPY ynetd /home/ctf/
COPY flag.txt /home/ctf/

# Permissions: allow only binary to access the flag
RUN chown root:ctf /home/ctf/flag.txt && \
    chmod 440 /home/ctf/flag.txt && \
    chmod 750 /home/ctf/Debug && \
    chmod 750 /home/ctf/ynetd && \
    chmod 750 /home/ctf/launch.sh && \
    chown -R root:ctf /home/ctf

WORKDIR /home/ctf/
USER ctf
EXPOSE 2054

# Entry point: launch binary with ynetd
CMD ["/home/ctf/ynetd", "-p", "2054", "/home/ctf/launch.sh"]
