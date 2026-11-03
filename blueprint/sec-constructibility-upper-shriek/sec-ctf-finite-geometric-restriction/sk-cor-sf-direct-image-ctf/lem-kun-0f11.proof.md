+++
kind  = "proof"
of    = "lem-kun-0f11"
+++
*Step 1 (sheaves).* A set-indexed direct sum of torsion sheaves is
the filtered colimit of its finite partial sums, with split-injective
transition maps, so for every $q$ the canonical map

$$
\bigoplus_iR^qf_*F_i\longrightarrow
R^qf_*\Bigl(\bigoplus_iF_i\Bigr)
$$

is an isomorphism by
[lemma-weil-pbc-direct-image-filtered-colimit] (and the same argument
with $f$ the structure morphism gives the statement for
$\RGamma(X_{\Et},-)$).
*Step 2 (complexes).* Let $d=\kuncd(f)<\infty$. For every
$K\in D(X_{\Et},\kunZn)$ and $n\in\mathbf Z$ the canonical map
$\mathcal H^n(Rf_*K)\to\mathcal H^n(Rf_*\tau_{\geq n-d-1}K)$ is an
isomorphism (Stacks Project, Derived Categories, Lemma 13.32.2), naturally
in $K$, and $\tau_{\geq n-d-1}$ commutes with direct sums. As in
[Stacks, Tag 0F11], it therefore suffices to treat complexes $K_i$ that are
bounded below by a common bound. For such
$K_i\in D(X_{\Et},\kunZn)$ ([def-weil-pbc-derived-categories]) the
hypercohomology spectral sequences of
[thm-sp-truncation-e2] for the $K_i$ and for
$\bigoplus_iK_i$ have $E_2$-pages $R^pf_*\mathcal H^q(K_i)$
respectively $R^pf_*\mathcal H^q(\bigoplus_iK_i)$, and
$\mathcal H^q(\bigoplus_iK_i)=\bigoplus_i\mathcal H^q(K_i)$, so Step 1
identifies the second $E_2$-page with the direct sum of the first.
The truncation construction of the spectral sequence is compatible with
direct sums, so the spectral sequence of the direct sum is the direct
sum of the spectral sequences; both converge in the half-plane sense of
[lemma-weil-pbc-hypercohomology-convergence] (half-plane, since
$p\ge0$), and a direct sum of separated exhaustive filtrations is
separated and exhaustive. Hence the abutments agree, i.e.

$$
\mathcal H^n\Bigl(Rf_*\bigoplus_iK_i\Bigr)
\cong\bigoplus_i\mathcal H^n(Rf_*K_i)
\qquad(n\in\mathbf Z),
$$

which is the direct-sum statement for uniformly bounded-below complexes,
and by the reduction above for all complexes; the reduction uses the
hypothesis $\kuncd(f)<\infty$ of [def-kun-cd] (for (2), $\kuncd(X)<\infty$).
