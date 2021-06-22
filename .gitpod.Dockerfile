FROM gitpod/workspace-full

LABEL maintainer="giridharsalana@gmail.com"

# Install custom tools, runtime, etc.
RUN sudo apt-get update && sudo apt-get install -y && \
    sudo apt-get install --quiet --yes fish
    
# Apply user-specific settings

RUN mkdir -p /home/gitpod/.config/fish/

RUN  echo "function c\n    clear\nend" > /home/gitpod/.config/fish/config.fish

RUN sudo chsh -s /usr/bin/fish

ENV SHELL /usr/bin/fish

ENV LANG=C.UTF-8 LANGUAGE=C.UTF-8 LC_ALL=C.UTF-8

ENTRYPOINT [ "fish" ]
