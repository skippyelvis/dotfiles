set nocompatible
set showmatch
set ignorecase
set mouse=v
set mouse=a
set hlsearch
set incsearch
set tabstop=4
set softtabstop=4
set expandtab
set shiftwidth=4
set autoindent
set number
set wildmode=longest,list
filetype plugin on
filetype plugin indent on
syntax on
syntax enable
set clipboard=unnamedplus
set ttyfast
" set spell
" set noswapfile
" set backupdir=~/.cache/vim
"set cursorline

set splitright
set splitbelow

if (has("termguicolors"))
    set termguicolors
endif

source ~/.config/nvim/plugs.vim
source ~/.config/nvim/maps.vim
source ~/.config/nvim/aucmd.vim

let g:python_host_prog=expand('/usr/bin/python3')
let g:python3_host_prog=expand('/usr/bin/python3')
