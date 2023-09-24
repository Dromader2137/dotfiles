export ZSH="$HOME/.oh-my-zsh"

if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

ZSH_THEME="robbyrussell"

plugins=(git)

source $ZSH/oh-my-zsh.sh

export EDITOR='nvim'

alias la="ls -A"
alias ll="ls -lA"
alias vi="nvim"
alias monitor-on="xrandr --output DP-1-0 --right-of eDP-1 --auto; ~/.fehbg"
alias monitor-off="xrandr --output DP-1-0 --off; ~/.fehbg"

alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
