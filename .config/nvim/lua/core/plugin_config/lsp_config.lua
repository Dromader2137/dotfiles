require('mason').setup()
require('mason-lspconfig').setup({
  ensure_installed = { "lua_ls", "clangd", "pyright" }
})

local capabilities = require('cmp_nvim_lsp').default_capabilities()

require('lspconfig').lua_ls.setup {
  capabilities = capabilities,
  settings = {
        Lua = {
            diagnostics = {
                globals = { 'vim' }
            }
        }
    },
  telemetry = {
    enable = false,
  },
}

require('lspconfig').clangd.setup {
  capabilities = capabilities,
  telemetry = {
    enable = false,
  },
}

require('lspconfig').pyright.setup {
  capabilities = capabilities,
  telemetry = {
    enable = false,
  },
}

vim.diagnostic.config({
  virtual_text = true,
  severity_sort = true,
  update_in_insert = true,
  signs = false,
})
