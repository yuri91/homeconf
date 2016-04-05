#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return



# Enable color and human friendly output.
alias ls='ls -h --color=auto'
alias dir='dir -h --color=auto'
alias vdir='vdir -h --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

#solarized colors for the above commands
eval `dircolors ~/.dircolors`

#PS1='[\u@\h \W]\$ '
#PS1='[\h]\[\e[0;32m\][\D{%T}]\[\e[m\] \[\e[0;31m\]\u\[\e[m\] \[\e[1;34m\]\w\[\e[m\] \[\e[0;31m\]\$ \[\e[m\]\n--->'
source ~/.bash_prompt

#editor
alias v='nvim'
export EDITOR='nvim'
export SYSTEMD_EDITOR='nvim'

#personal aliases
alias gping='ping www.google.com'
alias update='yaourt -Syu --aur'
alias cprsync='rsync -a --stats --progress'
alias scrotclip=$'scrot \'/tmp/%F_%T.png\' -s -e \'xclip -selection c -t image/png $f\''


#go
export GOPATH=~/projects/go
export GOMAXPROCS=8
export PATH="$PATH:$GOPATH/bin"

#cabal
export PATH="$PATH:/home/yuri/.cabal/bin"

