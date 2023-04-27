require('lualine').setup {
  options = {
    icons_enabled = true,
    theme = 'catppuccin',
  },

  sections = {
    lualine_a =
    {
      {
        'mode',
        path = 0,
      }
    }
  }
}
