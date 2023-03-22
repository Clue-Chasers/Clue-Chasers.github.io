from pathlib import Path
import logging
import shutil

import sys
sys.path.append(str(Path.cwd()))
from site_builder.structure_settings import StructureSettings
from site_builder.file_collector import FileCollector
from site_builder.page_generator import PageGenerator
from site_builder.name_conversion import NameConverter


logging.basicConfig()
logging.getLogger('site_builder.page_generator').level = logging.DEBUG
# logging.getLogger('site_builder.name_conversion').level = logging.ERROR


if __name__ == '__main__':
    if (previous_build_dir := Path('docs/cc-master')).exists():
        shutil.rmtree(previous_build_dir)

settings = StructureSettings.from_yaml('structure_settings.yml')

files = FileCollector(settings.files)

name_converter = NameConverter(settings.name_convert, settings.files.source_dir)

page_generator = PageGenerator(files, name_converter, settings.files.source_dir)
page_generator.generate_pages()
