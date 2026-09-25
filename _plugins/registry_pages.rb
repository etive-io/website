# Generates one page per package in _data/registry.json (built by
# scripts/build-registry.py from registry.yml). Plugin pages are therefore
# never written by hand: their content comes from each package's own README
# and metadata.
module Registry
  class PackagePage < Jekyll::Page
    def initialize(site, pkg, readme_html)
      @site = site
      @base = site.source
      @dir  = File.join("plugins", pkg["slug"])
      @name = "index.html"
      process(@name)
      @content = ""
      @data = {
        "layout" => "plugin",
        "title" => pkg["name"],
        "description" => pkg["summary"],
        "package" => pkg,
        "readme_html" => readme_html,
      }
    end
  end

  class Generator < Jekyll::Generator
    safe true
    priority :normal

    def generate(site)
      registry = site.data["registry"]
      return unless registry

      markdown = site.find_converter_instance(Jekyll::Converters::Markdown)
      registry["packages"].each do |pkg|
        next if pkg["category"] == "core"

        readme = (pkg["source"] || {})["readme"]
        html =
          if readme.nil?
            nil
          elsif readme["format"] == "html"
            readme["text"]
          elsif readme["format"] == "markdown"
            markdown.convert(readme["text"])
          else
            "<pre>#{CGI.escapeHTML(readme["text"])}</pre>"
          end
        site.pages << PackagePage.new(site, pkg, html)
      end
    end
  end
end
