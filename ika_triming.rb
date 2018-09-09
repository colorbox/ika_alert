require 'fileutils'
require 'RMagick'
require 'rubygems'


def crop_icons(filename:, distdir:)
  original = Magick::Image.read(filename).first
  prefix = "#{distdir.gsub('/','_')}_#{File.basename(filename, ".*")}"

  width = original.columns
  height = original.rows

  icon_width = 53.0/1280.0 * width
  icon_height = 60.0/720.0 * height

  icon_start_column_gap = (53.0+5.0)/1280.0 * width

  icon_rows_from = 16.0/720.0 * height

  friends_start_column = 356.0/1280.0 * width
  enemy_start_column = 697.0/1280.0 * width

  image = original.crop(friends_start_column, icon_rows_from, icon_width, icon_height)
  image.resize(80,90).write("#{distdir}/#{prefix}-1.jpg")

  image = original.crop(friends_start_column + icon_start_column_gap * 1, icon_rows_from, icon_width, icon_height)
  image.resize(80,90).write("#{distdir}/#{prefix}-2.jpg")

  image = original.crop(friends_start_column + icon_start_column_gap * 2, icon_rows_from, icon_width, icon_height)
  image.resize(80,90).write("#{distdir}/#{prefix}-3.jpg")

  image = original.crop(friends_start_column + icon_start_column_gap * 3 - 1, icon_rows_from, icon_width, icon_height)
  image.resize(80,90).write("#{distdir}/#{prefix}-4.jpg")

  image = original.crop(enemy_start_column, icon_rows_from, icon_width, icon_height)
  image.resize(80,90).write("#{distdir}/#{prefix}-5.jpg")

  image = original.crop(enemy_start_column + icon_start_column_gap * 1, icon_rows_from, icon_width, icon_height)
  image.resize(80,90).write("#{distdir}/#{prefix}-6.jpg")

  image = original.crop(enemy_start_column + icon_start_column_gap * 2, icon_rows_from, icon_width, icon_height)
  image.resize(80,90).write("#{distdir}/#{prefix}-7.jpg")

  image = original.crop(enemy_start_column + icon_start_column_gap * 3 - 1, icon_rows_from, icon_width, icon_height)
  image.resize(80,90).write("#{distdir}/#{prefix}-8.jpg")
end

sliced_images_dirname = ARGV[0]
raise('you need image directory with args') if sliced_images_dirname.nil?
movie_name = sliced_images_dirname.split('/').last
dist_dir = "data/icons/#{movie_name}"
FileUtils.mkdir_p dist_dir

puts "generate icons from #{sliced_images_dirname} to #{dist_dir}"

Dir.entries(sliced_images_dirname).each do |filename|
  next unless File.extname(filename)==".jpg"
  filepath = "#{sliced_images_dirname}/#{filename}"
  crop_icons(filename: filepath ,distdir: dist_dir)
end
