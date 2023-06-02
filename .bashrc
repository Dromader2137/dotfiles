export VISUAL=nvim
export EDITOR="$VISUAL"
export FILEMANAGER=pcmanfm
export QT_QPA_PLATFORMTHEME=qt5ct

[[ $- != *i* ]] && return

alias clear='cls'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
