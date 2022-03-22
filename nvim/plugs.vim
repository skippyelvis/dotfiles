call plug#begin("~/.vim/plugged")
    Plug 'SirVer/ultisnips'
    Plug 'honza/vim-snippets'
    Plug 'preservim/nerdcommenter'
    Plug 'mhinz/vim-startify'
    Plug 'jiangmiao/auto-pairs'
    Plug 'davidhalter/jedi-vim'
    Plug 'terryma/vim-multiple-cursors'
    Plug 'machakann/vim-highlightedyank'
    Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
    Plug 'deoplete-plugins/deoplete-go'
    Plug 'deoplete-plugins/deoplete-jedi'
    Plug 'Shougo/neco-syntax'
    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
    Plug 'nanotech/jellybeans.vim'
    Plug 'tmhedberg/SimpylFold' 
    Plug 'Konfekt/FastFold'
    Plug 'kyazdani42/nvim-web-devicons' 
    Plug 'kyazdani42/nvim-tree.lua'
    Plug 'nvim-lua/plenary.nvim'
    Plug 'nvim-telescope/telescope.nvim'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
call plug#end()

" airline
let g:airline#extensions#tabline#enabled=1
let g:airline_theme = 'luna'

" Find files using Telescope command-line sugar.
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

lua <<EOF
require'nvim-tree'.setup{
view = {
    side = 'right'
    },
}
EOF

" treesitter
lua <<EOF
require'nvim-treesitter.configs'.setup {
  ensure_installed = {"python", "vim", "bash", "javascript", "c", "go"},
  sync_install = false,
  highlight = {
    enable = true,
    additional_vim_regex_highlighting = false,
  },
}
EOF

"set foldmethod=expr
"set foldexpr=nvim_treesitter#foldexpr()

" simpylfold
let g:SimpylFold_docstring_preview = 1
set foldlevel=1

" gocode
let g:deoplete#sources#go#gocode_binary = $GOPATH.'/bin/gocode'

"colorscheme setup
colorscheme jellybeans
hi Comment cterm=italic

" ultisnips
let g:UltiSnipsExpandTrigger="<C-e>"
let g:UltiSnipsJumpForwardTrigger="<C-e>"
let g:UltiSnipsJumpBackwardTrigger="<C-r>"

"deoplete options
let g:deoplete#enable_at_startup = 1
call deoplete#custom#option('ignore_sources', {'_': ['around', 'buffer']})
call deoplete#custom#source('_', 'max_menu_width', 80)
function! s:check_back_space() abort "{{{
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction"}}}
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ deoplete#manual_complete()
set splitbelow
highlight Pmenu ctermbg=8 guibg=#606060
highlight PmenuSel ctermbg=1 guifg=#dddd00 guibg=#1f82cd
highlight PmenuSidebar ctermbg=0 guibg=#d6d6d6

"jedi-vim options
let g:jedi#completions_enabled = 0
let g:jedi#use_splits_not_buffers = "right"
let g:jedi#show_call_signatures = "2"

" highlighted-yank options
hi HighlightedyankRegion cterm=reverse gui=reverse
let g:Highlightedyank_highlight_duration = 1000
