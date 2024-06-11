import valid_dir
import valid_lang
import valid_name
import valid_short_name
import valid_scope
import valid_display
import valid_orientation
import valid_icons
import valid_start_url
import valid_id
import valid_color
import valid_shortcuts
import valid_applications
import os

input_folder = "../files2analyze"


def main(flag=False):
    for filename in os.listdir(input_folder):
        origin = filename
        path = os.path.join(input_folder, filename)
        valid_dir.main(path)
        valid_lang.main(path)
        valid_name.main(path)
        valid_short_name.main(path)
        valid_scope.main(path, origin)
        valid_display.main(path)
        valid_orientation.main(path)
        valid_icons.main(path, origin)
        valid_start_url.main(path, origin)
        valid_id.main(path, origin)
        valid_color.main(path)
        valid_shortcuts.main(path, origin)
        valid_applications.main(path, origin)


if __name__ == "__main__":
    main()
