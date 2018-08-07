require 'fileutils'
require 'RMagick'
require 'rubygems'


def crop_icons(filename:, distdir:)
  original = Magick::Image.read(filename).first
  prefix = distdir.gsub('/','_') + File.basename(filename, ".*")

  puts(prefix)

  image = original.crop(356, 15, 53, 60)
  image.write("#{distdir}/#{prefix}-1.jpg")

  image = original.crop(356 + 53 + 5, 15, 53, 60)
  image.write("#{distdir}/#{prefix}-2.jpg")

  image = original.crop(356 + (53 + 5) * 2, 15, 53, 60)
  image.write("#{distdir}/#{prefix}-3.jpg")

  image = original.crop(356 + (53 + 5) * 3 - 1, 15, 53, 60)
  image.write("#{distdir}/#{prefix}-4.jpg")

  image = original.crop(356 + (53 + 5) * 3 + 167, 15, 53, 60)
  image.write("#{distdir}/#{prefix}-5.jpg")

  image = original.crop(356 + (53 + 5) * (3+1) + 167, 15, 53, 60)
  image.write("#{distdir}/#{prefix}-6.jpg")

  image = original.crop(356 + (53 + 5) * (3+2) + 167, 15, 53, 60)
  image.write("#{distdir}/#{prefix}-7.jpg")

  image = original.crop(356 + (53 + 5) * (3+3) + 167 - 1, 15, 53, 60)
  image.write("#{distdir}/#{prefix}-8.jpg")
end

sliced_images_dirname = ARGV[0]
raise('you need image directory with args') if sliced_images_dirname.nil?
movie_name = sliced_images_dirname.split('/').last
dist_dir = "data/icons/#{movie_name}"
FileUtils.mkdir_p dist_dir

Dir.entries(sliced_images_dirname).each do |filename|
  next unless File.extname(filename)==".jpg"
  filepath = "#{sliced_images_dirname}/#{filename}"
  puts filepath
  crop_icons(filename: filepath ,distdir: dist_dir)
end
