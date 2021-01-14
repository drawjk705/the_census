"""
This type stub file was generated by pyright.
"""

__author__ = {"github.com/": ["casperdcl"]}

class TqdmCallback(keras.callbacks.Callback):
    """`keras` callback for epoch and batch progress"""

    @staticmethod
    def bar2callback(bar, pop=..., delta=...): ...
    def __init__(
        self,
        epochs=...,
        data_size=...,
        batch_size=...,
        verbose=...,
        tqdm_class=...,
        **tqdm_kwargs
    ) -> None:
        """
        Parameters
        ----------
        epochs  : int, optional
        data_size  : int, optional
            Number of training pairs.
        batch_size  : int, optional
            Number of training pairs per batch.
        verbose  : int
            0: epoch, 1: batch (transient), 2: batch. [default: 1].
            Will be set to `0` unless both `data_size` and `batch_size`
            are given.
        tqdm_class : optional
            `tqdm` class to use for bars [default: `tqdm.auto.tqdm`].
        tqdm_kwargs  : optional
            Any other arguments used for all bars.
        """
        ...
    def on_train_begin(self, *_, **__): ...
    def on_epoch_begin(self, *_, **__): ...
    def on_train_end(self, *_, **__): ...
    def display(self):
        """displays in the current cell in Notebooks"""
        ...
