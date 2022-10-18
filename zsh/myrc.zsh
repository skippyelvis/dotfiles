alias cl="clear"
alias le="exa -l --icons"
alias treee="exa --icons --tree"
alias vim="nvim"
alias p3="python3"
alias pipi="pip install --user"
alias install="sudo pacman -S"
alias yinstall="yay -S"
alias icat="kitty +icat"

export ix="ix.cs.uoregon.edu"
export ixd="ix-dev.cs.uoregon.edu"

alias sshix="ssh $UOID@$ix"
alias sshixd="ssh $UOID@$ixd"

export EDITOR="nvim"
export RANGER_LOAD_DEFAULT_RC="FALSE"

export PATH=$PATH:$HOME/.local/bin
export PATH=$PATH:/usr/local/go/bin
export PATH=$PATH:/home/$USER/cli

bak() {
    cp $1 $1.bak
}

HISTFILE=~/.zsh_histfile
HISTSIZE=1000
SAVEHIST=1000
setopt appendhistory

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/skippyelvis/cli/google-cloud-sdk/path.zsh.inc' ]; then . '/home/skippyelvis/cli/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/home/skippyelvis/cli/google-cloud-sdk/completion.zsh.inc' ]; then . '/home/skippyelvis/cli/google-cloud-sdk/completion.zsh.inc'; fi
