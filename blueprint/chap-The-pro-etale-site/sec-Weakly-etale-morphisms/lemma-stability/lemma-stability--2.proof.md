+++
kind = "proof"
of = "lemma-stability--2"
order = 32010
+++
Flatness is stable under composition. The diagonal of $V\to X$
factors as
$$
V\longrightarrow V\times_UV\longrightarrow V\times_XV.
$$
The first map is the diagonal of $V\to U$, and the second is a base
change of the diagonal of $U\to X$. Both are flat. This proves
stability under composition of the flat-diagonal condition as well.
Together with the identity case, these two flatness conditions give
the multiplicative property from which Lean obtains the assertion.
