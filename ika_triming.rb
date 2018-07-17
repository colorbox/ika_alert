require 'RMagick'
require 'rubygems'


def crop_icons(filename)
  original = Magick::Image.read(filename).first
  prefix = File.basename(filename, ".*")

  image = original.crop(356, 15, 53, 60)
  image.write("icons/#{prefix}-1.jpg")

  image = original.crop(356 + 53 + 5, 15, 53, 60)
  image.write("icons/#{prefix}-2.jpg")

  image = original.crop(356 + (53 + 5) * 2, 15, 53, 60)
  image.write("icons/#{prefix}-3.jpg")

  image = original.crop(356 + (53 + 5) * 3 - 1, 15, 53, 60)
  image.write("icons/#{prefix}-4.jpg")

  image = original.crop(356 + (53 + 5) * 3 + 167, 15, 53, 60)
  image.write("icons/#{prefix}-5.jpg")

  image = original.crop(356 + (53 + 5) * (3+1) + 167, 15, 53, 60)
  image.write("icons/#{prefix}-6.jpg")

  image = original.crop(356 + (53 + 5) * (3+2) + 167, 15, 53, 60)
  image.write("icons/#{prefix}-7.jpg")

  image = original.crop(356 + (53 + 5) * (3+3) + 167 - 1, 15, 53, 60)
  image.write("icons/#{prefix}-8.jpg")

end

Dir.entries("./douga").each do |filename|
  next unless File.extname(filename)==".jpg"
  puts "./douga/#{filename}"
  crop_icons("./douga/#{filename}")
end
