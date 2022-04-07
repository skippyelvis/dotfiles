func bak() {
    mv $1 $1.bak
}

func gpush() {
    git add .
    git commit -m $1
    git push
}
