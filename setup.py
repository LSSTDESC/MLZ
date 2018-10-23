import sys

files_f90 = ['mlz_desc/ml_codes/som.f90', ]
from numpy.distutils.core import setup, Extension

extra_link_args = []
libraries = []
library_dirs = []
include_dirs = ['mlz_desc/ml_codes']
setup(
    name='MLZ-DESC',
    version='1.2',
    author='Matias Carrasco Kind (original), Bela Abolfathi (DESC)',
    author_email='babolfat@uci.edu',
    ext_modules=[Extension('somF', files_f90, include_dirs=['mlz_desc/ml_codes'], ), ],
    packages=['mlz_desc', 'mlz_desc.plot', 'mlz_desc.utils', 'mlz_desc.test', 'mlz_desc.ml_codes'],
    py_modules=['mlz_desc','mlz_desc.plot','mlz_desc.utils','mlz_desc.test','mlz_desc.ml_codes'],
    package_data={'mlz_desc': ['test/SDSS_MGS.train', 'test/SDSS_MGS.test', 'test/SDSS_MGS.inputs', 'plot/*.txt']},
    scripts=['mlz_desc/runMLZ', 'mlz_desc/plot/plot_map', 'mlz_desc/plot/plot_results', 'mlz_desc/plot/plot_importance',
             'mlz_desc/plot/plot_tree', 'mlz_desc/utils/use_pdfs', 'mlz_desc/plot/plot_pdf_use', 'mlz_desc/plot/plot_sparse'],
    license='LICENSE.txt',
    description='MLZ: Machine Learning for photo-Z, a photometric redshift PDF estimator (DESC version)',
    long_description=open('README.txt').read(),
    url='http://lcdm.astro.illinois.edu/static/code/mlz/MLZ-1.2/doc/html/index.html',
    install_requires=['mpi4py', 'numpy', 'matplotlib', 'healpy', 'scipy', 'astropy'],
)
