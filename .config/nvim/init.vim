call plug#begin()
Plug 'tpope/vim-sensible'
Plug 'vim-pandoc/vim-pandoc'
Plug 'vim-pandoc/vim-pandoc-syntax'
Plug 'dhruvasagar/vim-table-mode'
Plug 'bling/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'tpope/vim-fugitive'
Plug 'altercation/vim-colors-solarized'
Plug 'Shougo/deoplete.nvim'
Plug 'lambdatoast/elm.vim'
Plug 'bronson/vim-trailing-whitespace'
Plug 'scrooloose/nerdcommenter'
Plug 'scrooloose/nerdtree'
Plug 'ctrlpvim/ctrlp.vim'

call plug#end()

"vim-pandoc
let g:pandoc#modules#disabled = ["folding"]
let g:pandoc#formatting#mode = 'hA'
let g:pandoc#formatting#smart_autoformat_on_cursormoved = 1
"vim-pandoc-after
let g:pandoc#after#modules#enabled = ["tablemode"]

"vim-table-mode
let g:table_mode_corner_corner="+"
let g:table_mode_header_fillchar="="

"vim-airline
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
" certain number of spaces are allowed after tabs, but not in between
let g:airline#extensions#whitespace#mixed_indent_algo = 1
" solazized!
let g:airline_theme='solarized'

"deoplete
let g:deoplete#enable_at_startup = 1
autocmd InsertLeave,CompleteDone * if pumvisible() == 0 | pclose | endif

"ctrlp
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlPMixed'
let g:ctrlp_working_path_mode = 'ra'

" nerdree
" close vim if nerdtree is the only window
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" toggle
map <C-n> :NERDTreeToggle<CR>

"colorscheme
set background=dark
colorscheme solarized

"personal stuff
set colorcolumn=80
set number
set clipboard=unnamedplus
"This unsets the "last search pattern" register by hitting return
nnoremap <CR> :noh<CR><CR>
" genius
nnoremap ; :
" http://usevim.com/2012/10/19/vim101-set-hidden/
set hidden
" space as leader
map <space> <leader>
" close buffer
nnoremap <leader>q :bd<CR>

"language-specific (google style)
autocmd FileType cpp setlocal shiftwidth=2 tabstop=2 expandtab
