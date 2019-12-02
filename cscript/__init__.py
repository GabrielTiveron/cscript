"""
CScript é uma implementação de C em Python com várias extensões sintáticas.

As extensões foram escolhidas para desagradar igualmente usuários tradicionais de C e
de linguagens de programação tradicionais.
"""

from .symbol import Symbol, var
from .parser import parse
from .runtime import eval, env, global_env

__version__ = '0.1.0'
