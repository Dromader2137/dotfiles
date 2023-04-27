require("luasnip.loaders.from_vscode").lazy_load()

local cmp = require('cmp')

cmp.setup({
  mapping = cmp.mapping.preset.insert({
    ['<CR>'] = cmp.mapping.confirm({ select = true }),
    ['<C-Space>'] = cmp.mapping.complete(),
  }),
  snippet = {
    expand = function(args)
      require('luasnip').lsp_expand(args.body)
    end,
  },
  sources = cmp.config.sources({
    {name = 'nvim_lsp' },
    {name = 'luasnip' },
  }, {
    {name = 'buffer' }
  }),
})
