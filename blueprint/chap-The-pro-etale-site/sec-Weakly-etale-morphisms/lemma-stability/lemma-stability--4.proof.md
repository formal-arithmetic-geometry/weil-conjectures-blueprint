+++
kind = "proof"
of = "lemma-stability--4"
order = 32012
+++
Flatness of $f$ can be checked on a Zariski open covering of $X$.
The open subschemes
$$
f^{-1}(X_i)\times_{X_i}f^{-1}(X_i)
$$
cover $U\times_XU$, and the restriction of $\Delta_{U/X}$ over each
of them is the diagonal of $f^{-1}(X_i)\to X_i$. Thus flatness of
the diagonal can also be checked on this covering. Lean applies
locality on the target to the flat-diagonal property and combines it
with locality of flatness of $f$.
