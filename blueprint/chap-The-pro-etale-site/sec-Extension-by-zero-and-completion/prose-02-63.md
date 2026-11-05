+++
id = "prose-02-63"
kind = "hidden"
title = "Extension by zero and completion (5)"
order = 212
+++
Over a point, for $K=\mathcal O_E$ placed in degree $0$, the reductions
are $K_n=\mathcal O_E/\pi_E^n$, and the lemma is the classical Nakayama
lemma for the complete local ring $\mathcal O_E$. The hypothesis of
completeness cannot be dropped, since $E\neq0$ but $E/\pi_E=0$.

Let $K$ be derived complete. Since $R\Gamma(X_{\mathrm{pro}\acute{e}t},-)$ is a right
adjoint, it commutes with the derived limit, and therefore

$$
R\Gamma(X_{\mathrm{pro}\acute{e}t},K)
\simeq R\varprojlim_nR\Gamma(X_{\mathrm{pro}\acute{e}t},K_n).
$$

When the $K_n$ are classical bounded-below complexes, each term on the
right can be computed on the étale site by
Theorem [theorem-bounded-below-cohomology-comparison]. In this way
we compute the cohomology of $K$ from its tower of reductions $(K_n)$.

In Section [sec-Constructibility] we define constructible complexes over
$\mathcal O_E$, and we show that for Noetherian $X$ they are exactly the
derived complete complexes $K$ whose reduction $K_1$ is constructible
(Proposition [proposition-integral-constructibility-criterion]).
Derived complete complexes can equally be studied over the constant sheaf
with value the discrete ring $\mathcal O_E$
(Lemma [lemma-integral-models](1)).

The rational coefficient sheaves are obtained by inverting $\ell$ and
passing to the colimit over $E$:
$E_X\simeq\mathcal O_{E,X}[1/\ell]$ and $\QbarX\simeq\varinjlim_E E_X$
(Lemma [lemma-comparison-completed-coefficients]).
Chapter [chap-Constructible-complexes] also compares constructible
complexes over $E_X$ and $\QbarX$ with the classical adic categories. It
does so by lattices and by descent to a finite extension.
