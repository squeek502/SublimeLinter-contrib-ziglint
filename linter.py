from SublimeLinter.lint import Linter, STREAM_STDOUT, WARNING


class Ziglint(Linter):
    cmd = ('ziglint', '-file', '${file}')
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)'
    default_type = WARNING
    error_stream = STREAM_STDOUT
    tempfile_suffix = '-'
    defaults = {
        'selector': 'source.zig'
    }
