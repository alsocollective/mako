import SVGCompress
import shapely

SVGCompress.compress_by_method(filename = 'waves0.svg', optimize = True, optimize_options='optimize_tothe_max', compression_type = 'simplify', epsilon = 5, selection_tuple = ('bboxarea', 600), curve_fidelity = 1, pre_select = True, operation_key = 'hull')