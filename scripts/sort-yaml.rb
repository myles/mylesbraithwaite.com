require 'yaml'

# TODO: This should be better written.

fobj = File.new('source/_data/tags.yml', 'r')

tags = YAML.load(fobj.read)

fobj.close

fobj = File.new('source/_data/tags.yml', 'w')

yaml_dump = YAML.dump(tags.sort.to_h)

fobj.write(yaml_dump)

fobj.close
