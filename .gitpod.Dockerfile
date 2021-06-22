FROM gitpod/workspace-full

LABEL maintainer="giridharsalana@gmail.com"

# Install custom tools, runtime, etc.
RUN sudo apt-get update && sudo apt-get install -y && \
    sudo apt-get install --quiet --yes fish
    
# Apply user-specific settings

RUN sudo chsh -s /usr/bin/fish

USER gipod

#SHELL ["fish", "--command"]

ENV SHELL /usr/bin/fish

ENV LANG=C.UTF-8 LANGUAGE=C.UTF-8 LC_ALL=C.UTF-8

RUN source .Init_Source

ENTRYPOINT [ "fish" ]
