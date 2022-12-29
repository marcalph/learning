from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import pytest
# in general its better to check data rather than plots
# @image_comparison(baseline_images=['line_dashes'], remove_text=True,
#                   extensions=['png'])
# def test_line_dashes():
#     fig, ax = plt.subplots()
#     ax.plot(range(10), linestyle=(0, (3, 3)), lw=5)


# @pytest.fixture(scope='function')
# def plot_fn():
#     def _plot(points):
#         plt.plot(points)
#         yield plt.show()
#         plt.close('all')
#     return _plot


# def test_plot_fn(plot_fn):
#     points = [1, 2, 3]
#     plot_fn(points)
#     assert True

@pytest.fixture(scope='function')
def plot_fn(points=range(3)):
    # def _plot(points):
    plot = plt.plot(points)
    return plot
    plt.close('all')
    # return _plot


def test_plot_fn(plot_fn):
    points = [1, 2, 3]
    print(plot_fn)
    assert True