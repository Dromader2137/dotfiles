#
# ~/.bashrc
#

export VISUAL=nvim
export EDITOR="$VISUAL"
export FILEMANAGER=pcmanfm

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
