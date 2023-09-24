vim.g.mapleader = ' '
vim.g.maplocalleader = ' '
vim.opt.scrolloff = 10
vim.wo.nu = true
vim.wo.relativenumber = true
vim.opt.backspace = '2'
vim.opt.showcmd = true
vim.opt.laststatus = 2
vim.opt.autowrite = true
vim.opt.autoread = true

vim.opt.tabstop = 2
vim.opt.shiftwidth = 2
vim.opt.shiftround = true
vim.opt.expandtab = true

vim.keymap.set('n', '<c-b>', ':ToggleTerm<CR>')
vim.keymap.set("t", "<c-b>", "<C-\\><C-n>:ToggleTerm<CR>")
