require 'jekyll'
require 'nokogiri'
require 'redcarpet'

class Jekyll::Converters::Markdown::CustomRedcarpetParser
  module CommonMethods
    def add_code_tags(code, lang)
      code = code.to_s
      code = code.sub(
        /<pre>/,
        "<pre><code class=\"language-#{lang}\" data-lang=\"#{lang}\">"
      )
      code = code.sub(%r{</pre>}, '</code></pre>')
      code
    end

    def block_quote(quote)
      %(<blockquote class="blockquote">#{quote}</blockquote>)
    end

    def footnotes(text)
      %(<div class="footnotes"><hr class="footnotes__seperator"/><ol class="footnotes__list">#{text}</ol></div>)
    end

    def footnote_def(text, number)
      doc = Nokogiri::HTML.fragment(text)

      doc.css('p').last.add_child %(<a href="#footnote-ref-#{number}" class="footnotes__back-link" rev="footnote">&#8617;</a>)

      %(<li class="footnotes__item" id="footnote-#{number}">#{doc.to_html}</li>)
    end

    def header(text, header_level)
      header_id = Jekyll::Utils.slugify(text)

      header_levels = {
        1 => 'heading-one',
        2 => 'heading-two',
        3 => 'heading-three',
        4 => 'heading-four',
        5 => 'heading-five',
        6 => 'heading-six'
      }

      %(<h#{header_level} class="#{header_levels[header_level]}" id="heading-#{header_id}">#{text}</h#{header_level}>)
    end

    def footnote_ref(number)
      %(<sup id="footnote-ref-#{number}" class="footnote"><a href="#footnote-#{number}" class="footnote__link" rel="footnote">#{number}</a></sup>)
    end
  end

  module WithPygments
    include CommonMethods
    def block_code(code, lang)
      Jekyll::External.require_with_graceful_fail('pygments')
      lang = lang && lang.split.first || 'text'
      add_code_tags(
        Pygments.highlight(
          code,
          lexer: lang,
          options: { encoding: 'utf-8' }
        ),
        lang
      )
    end
  end

  module WithoutHighlighting
    require 'cgi'

    include CommonMethods

    def code_wrap(code)
      "<figure class=\"highlight\"><pre>#{CGI.escapeHTML(code)}</pre></figure>"
    end

    def block_code(code, lang)
      lang = lang && lang.split.first || 'text'
      add_code_tags(code_wrap(code), lang)
    end
  end

  module WithRouge
    def block_code(code, lang)
      code = "<pre>#{super}</pre>"

      output = '<div class="highlight">'
      output << add_code_tags(code, lang)
      output << '</div>'
    end

    protected

    def rouge_formatter(_lexer)
      Rouge::Formatters::HTML.new(wrap: false)
    end
  end

  def initialize(config)
    Jekyll::External.require_with_graceful_fail('redcarpet')
    @config = config
    @redcarpet_extensions = {}
    @config['redcarpet']['extensions'].each do |e|
      @redcarpet_extensions[e.to_sym] = true
    end

    @renderer ||= class_with_proper_highlighter(@config['highlighter'])
  end

  def class_with_proper_highlighter(highlighter)
    Class.new(Redcarpet::Render::HTML) do
      case highlighter
      when 'pygments'
        include WithPygments
      when 'rouge'
        Jekyll::External.require_with_graceful_fail(%w(
                                                      rouge rouge/plugins/redcarpet
                                                    ))

        unless Gem::Version.new(Rouge.version) > Gem::Version.new('1.3.0')
          abort 'Please install Rouge 1.3.0 or greater and try running Jekyll again.'
        end

        include Rouge::Plugins::Redcarpet
        include CommonMethods
        include WithRouge
      else
        include WithoutHighlighting
      end
    end
  end

  def convert(content)
    @redcarpet_extensions[:fenced_code_blocks] = \
      !@redcarpet_extensions[:no_fenced_code_blocks]
    if @redcarpet_extensions[:smart]
      @renderer.send :include, Redcarpet::Render::SmartyPants
    end
    markdown = Redcarpet::Markdown.new(
      @renderer.new(@redcarpet_extensions),
      @redcarpet_extensions
    )
    markdown.render(content)
  end
end
