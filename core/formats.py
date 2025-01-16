from import_export.formats import base_formats
import tablib

class SemiColonCSV(base_formats.CSV):
    """
    Кастомный CSV-формат с разделителем ";"
    """
    def create_dataset(self, in_stream, **kwargs):
        if isinstance(in_stream, bytes):
            in_stream = in_stream.decode('utf-8-sig')
        kwargs['delimiter'] = ';'
        return tablib.Dataset().load(in_stream, **kwargs)

    def get_title(self):
        return "semicolon-csv"
