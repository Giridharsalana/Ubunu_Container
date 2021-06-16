FROM gitpod/workspace-full

LABEL maintainer="giridharsalana@gmail.com"

# Install custom tools, runtime, etc.
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends apt-utils && \
    sudo apt-get install --quiet --yes software-properties-common openssh-client git && \
    sudo add-apt-repository --yes ppa:fish-shell/release-3 && \
    sudo apt-get install --quiet --yes fish
    
# Apply user-specific settings

RUN sudo chsh -s /usr/bin/fish

RUN source .Init_Source

USER Giri

#SHELL ["fish", "--command"]

ENV SHELL /usr/bin/fish

ENV LANG=C.UTF-8 LANGUAGE=C.UTF-8 LC_ALL=C.UTF-8

ENTRYPOINT [ "fish" ]
