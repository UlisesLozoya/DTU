""" Source code for 02466, Introduction to reinforcement learning and control, offered at DTU """
__version__ = "0.0.1"

# Do not import Matplotlib (or imports which import matplotlib) in case you have to run in headless mode.
import shutil
import inspect
import lzma, pickle
import numpy as np
import os

# Global imports from across the API. Allows imports like
# > from cp import Agent, train
# from cp.utils.irlc_plot import main_plot as main_plot
# from cp.utils.irlc_plot import plot_trajectory as plot_trajectory
# try:
#     from cp.ex01.agent import Agent as Agent, train as train
#     from cp.ex09.rl_agent import TabularAgent, ValueAgent
# except ImportError:
#     pass
# from cp.utils.player_wrapper import interactive as interactive
# from cp.utils.lazylog import LazyLog # This one is unclear. Is it required?
# from cp.utils.timer import Timer


def get_ipp_base():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

# def get_students_base():
#     return os.path.join(get_ipp_base(), "../../../02465students/")


def pd2latex_(pd, index=False, escape=False, column_spec=None, **kwargs): # You can add column specs.
    for c in pd.columns:
        if pd[c].values.dtype == 'float64' and all(pd[c].values - np.round(pd[c].values)==0):
            pd[c] = pd[c].astype(int)
    ss = pd.to_latex(index=index, escape=escape, **kwargs)
    return fix_bookstabs_latex_(ss,column_spec=column_spec)

def fix_bookstabs_latex_(ss, linewidth=True, first_column_left=True, column_spec=None):
    to_tabular_x = linewidth

    if to_tabular_x:
        ss = ss.replace("tabular", "tabularx")
    lines = ss.split("\n")
    hd = lines[0].split("{")
    if column_spec is None:
        adj = (('l' if to_tabular_x else 'l') if first_column_left else 'C') + ("".join(["C"] * (len(hd[-1][:-1]) - 1)))
    else:
        adj = column_spec

    # adj = ( ('l' if to_tabular_x else 'l') if first_column_left else 'C') + ("".join(["C"] * (len(hd[-1][:-1])-1)))
    if linewidth:
        lines[0] = "\\begin{tabularx}{\\linewidth}{" + adj + "}"
    else:
        lines[0] = "\\begin{tabular}{" + adj.lower() + "}"

    ss = '\n'.join(lines)
    return ss


def _savepdf_env(file, env):
    from PIL import Image
    import matplotlib.pyplot as plt
    if hasattr(env, 'render_mode') and not env.render_mode == 'rgb_array':
        env.render_mode, rmt = 'rgb_array', env.render_mode
    frame = env.render()
    if hasattr(env, 'render_mode') and not env.render_mode == 'rgb_array':
        env.render_mode = rmt

    im = Image.fromarray(frame)
    snapshot_base = file
    if snapshot_base.endswith(".png"):
        sf = snapshot_base[:-4]
        fext = 'png'
    else:
        fext = 'pdf'
        if snapshot_base.endswith(".pdf"):
            sf = snapshot_base[:-4]
        else:
            sf = snapshot_base

    sf = f"{sf}.{fext}"
    dn = os.path.dirname(sf)
    if len(dn) > 0 and not os.path.isdir(dn):
        os.makedirs(dn)
    print("Saving snapshot of environment to", os.path.abspath(sf))
    if fext == 'png':
        im.save(sf)
        from cp import _move_to_output_directory
        _move_to_output_directory(sf)
    else:
        plt.figure(figsize=(16, 16))
        plt.imshow(im)
        plt.axis('off')
        plt.tight_layout()
        from cp import savepdf
        savepdf(sf, verbose=True)
        # plt.show()



def savepdf(pdf, verbose=False, watermark=False, env=None, _png=False):
    """
    Convenience function for saving PDFs. Just call it after you have created your plot as ``savepdf('my_file.pdf')``
    to save a PDF of the plot.
    You can also pass an environment, in which case the environment will be stored to a pdf file.


    :param pdf: The file to save to, for instance ``"my_pdf.pdf"``
    :param verbose: Print output destination (optional)
    :param watermark: Include a watermark (optional)
    :return: Full path of the created PDF.
    """
    if env is not None:
        _savepdf_env(pdf, env)
        return

    import matplotlib.pyplot as plt
    pdf = os.path.normpath(pdf.strip())
    pdf = pdf+".pdf" if not pdf.endswith(".pdf") else pdf

    if os.sep in pdf:
        pdf = os.path.abspath(pdf)
    else:
        pdf = os.path.join(os.getcwd(), "pdf", pdf)
    if not os.path.isdir(os.path.dirname(pdf)):
        os.makedirs(os.path.dirname(pdf))

    modules = [inspect.getmodule(s[0]) for s in inspect.stack()]
    files = [m.__file__ for m in modules if m is not None]
    if any( [f.endswith("RUN_OUTPUT_CAPTURE.py") for f in files] ):
        return

    # for s in stack:
    #     print(s)
    # print(stack)
    # for k in range(len(stack)-1, -1, -1):
    #     frame = stack[k]
    #     module = inspect.getmodule(frame[0])
    #     filename = module.__file__
    #     print(filename)
    #     if not any([filename.endswith(f) for f in ["pydev_code_executor.py", "pydevd.py", "_pydev_execfile.py", "pydevconsole.py", "pydev_ipython_console.py"] ]):
    #         # print("breaking c. debugger", filename)
    #         break
    # if any( [filename.endswith(f) for f in ["pydevd.py", "_pydev_execfile.py"]]):
    #     print("pdf path could not be resolved due to debug mode being active in pycharm", filename)
    #     return
    # print("Selected filename", filename)
    # wd = os.path.dirname(filename)
    # pdf_dir = wd +"/pdf"
    # if filename.endswith("_RUN_OUTPUT_CAPTURE.py"):
    #     return
    # if not os.path.isdir(pdf_dir):
    #     os.mkdir(pdf_dir)
    wd = os.getcwd()
    ipp_base = os.path.dirname(__file__)
    if False:
        pass
    else:
        plt.savefig(fname=pdf)
    outf = os.path.normpath(os.path.abspath(pdf))
    print("> [savepdf]", pdf + (f" [full path: {outf}]" if verbose else ""))

    return outf


def _move_to_output_directory(file):
    """
    Hidden function: Move file given file to static output dir.
    """
    if not is_this_my_computer():
        return
    CDIR = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
    shared_output_dir = CDIR + "/../../shared/output"
    shutil.copy(file, shared_output_dir + "/"+ os.path.basename(file) )


# def bmatrix(a):
#     if False:
#         return a.__str__()
#     else:
#         np.set_printoptions(suppress=True)
#         """Returns a LaTeX bmatrix
#         :a: numpy array
#         :returns: LaTeX bmatrix as a string
#         """
#         if len(a.shape) > 2:
#             raise ValueError('bmatrix can at most display two dimensions')
#         lines = str(a).replace('[', '').replace(']', '').splitlines()
#         rv = [r'\begin{bmatrix}']
#         rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
#         rv +=  [r'\end{bmatrix}']
#         return '\n'.join(rv)


def is_this_my_computer():
    CDIR = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
    return os.path.exists(CDIR + "/../../Exercises")

# def cache_write(object, file_name, only_on_professors_computer=False, verbose=True, protocol=-1): # -1 is default protocol. Fix crash issue with large files.
#     if only_on_professors_computer and not is_this_my_computer():
#         """ Probably for your own good :-). """
#         return
#
#     dn = os.path.dirname(file_name)
#     if not os.path.exists(dn):
#         os.mkdir(dn)
#     if verbose: print("Writing cache...", file_name)
#     with lzma.open(file_name, 'wb') as f:
#         pickle.dump(object, f)
#         # compress_pickle.dump(object, f, compression="lzma", protocol=protocol)
#     if verbose:
#         print("Done!")


def cache_exists(file_name):
    return os.path.exists(file_name)

# def cache_read(file_name):
#     if os.path.exists(file_name):
#         with lzma.open(file_name, 'rb') as f:
#             return pickle.load(f)
#     else:
#         return None

inputs = []
def minput(ls):
    """
    Higher-order function to fix input.

    The function is given a list of keyboard input strings it will dutifully enter into input. If one of the inputs in the
    list is None, the function will throw an error. This is useful to terminate early and show what the user sees as
    part of the interaction.

    This function should eventually be absorbed into unitgrade once potential kinks involving stdout has been worked out.

    :param ls: Input strings.
    :return: An alternative input-function (for use in mocking)
    """
    inputs.clear()
    for l in ls:
        inputs.append(l)
    def _input(x):
        l = inputs[0]
        if l is None:
            print(x)
            raise GeneratorExit()
            # raise Exception()
        print(x, l)
        del inputs[0]
        return l
    return _input
