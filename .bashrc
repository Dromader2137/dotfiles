export VISUAL=nvim
export EDITOR="$VISUAL"
export FILEMANAGER=pcmanfm
export QT_QPA_PLATFORMTHEME=qt5ct

[[ $- != *i* ]] && return

alias la='ls -A'
alias ll='ls -lA'
alias cls='clear'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
alias show-wifi='nmcli dev wifi'
alias connect-wifi='nmcli dev wifi connect --ask'

PS1='\[\033[34m\]\[\033[30m\]\[\033[44m\] \w \[\033[40m\]\[\033[34m\]\n 󰘍 \[\033[37m\]'
