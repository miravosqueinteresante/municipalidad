Jekyll::Hooks.register :pages, :post_init do |page|
  if page.name == "sitemap.xml"
    page.data["home_in_sitemap"] = true
  end
end

Jekyll::Hooks.register :site, :post_write do |site|
  sitemap_path = File.join(site.dest, "sitemap.xml")
  next unless File.exist?(sitemap_path)

  content = File.read(sitemap_path)
  home_entry = %(  <url>\n    <loc>https://muchotexto.net/</loc>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>\n)
  home_loc = "<loc>https://muchotexto.net/</loc>"

  unless content.include?(home_loc)
    content = content.sub("</urlset>", "#{home_entry}</urlset>")
    File.write(sitemap_path, content)
  end
end
