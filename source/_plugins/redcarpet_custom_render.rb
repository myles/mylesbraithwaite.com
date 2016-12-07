require 'jekyll'
require 'nokogiri'
require 'redcarpet'

class RedcarpetExtender < Redcarpet::Render::HTML
  def block_quote(quote)
    %(<blockquote class="blockquote">#{quote}</blockquote>)
  end

  def footnotes(text)
    %(<div class="footnotes"><ol class="footnotes__list">#{text}</ol></div>)
  end

  def footnote_def(text, number)
    doc = Nokogiri::HTML.fragment(text)

    doc.css('p').last.add_next_sibling %(<a href="#footnote-ref-#{number}" class="footnotes__back-link" rev="footnote">&#8617;</a>)

    %(<li class="footnotes__item" id="footnote-#{number}">#{doc.to_html}</li>)
  end

  def footnote_ref(number)
    %(<sup id="footnote-ref-#{number}" class="footnote"><a href="#footnote-#{number}" class="footnote__link" rel="footnote">#{number}</a></sup>)
  end
end

class Jekyll::Converters::Markdown::RedcarpetExt
  def initialize(config)
    @site_config = config
  end

  def extensions
    Hash[ *@site_config['redcarpet']['extensions'].map {|e| [e.to_sym, true]}.flatten ]
  end

  def markdown
    @markdown ||= Redcarpet::Markdown.new(RedcarpetExtender, extensions)
  end

  def convert(content)
    return super unless @site_config['markdown'] == 'RedcarpetExt'
    markdown.render(content)
  end
end
