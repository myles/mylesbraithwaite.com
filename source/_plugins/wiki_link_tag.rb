module Jekyll
  module Tags
    class WikiLink < Liquid::Tag
      def initialize(tag_name, relative_path, tokens)
        super

        @relative_path = relative_path.strip
      end

      def render(context)
        site = context.registers[:site]

        site.wiki do |item|
          if item.relative_path == @relative_path or item.relative_path == "/#{@relative_path}"
            if item.title
              return '<a href="#{item.url}">#{item.title}</a>'
            else
              return '<a href="#{item.url}">#{@relative_path}</a>'
            end
          end

          return '<span class="wiki-link-doesnt-exist">#{@relative_path}</span>'
        end
      end
    end
  end
end

Liquid::Template.register_tag('wiki', Jekyll::Tags::WikiLink)
