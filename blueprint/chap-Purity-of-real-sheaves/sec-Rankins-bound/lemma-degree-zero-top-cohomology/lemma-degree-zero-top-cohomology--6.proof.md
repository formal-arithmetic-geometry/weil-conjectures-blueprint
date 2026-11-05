+++
kind = "proof"
of = "lemma-degree-zero-top-cohomology--6"
order = 1150013
uses = ["lemma-degree-zero-top-cohomology--5", "lemma-filtrations-spectra", "lemma-degree-zero-top-cohomology--2"]
+++
If $\gamma$ is an eigenvalue on $Q(\mathcal F)$, then $\gamma^{-1}$
is an eigenvalue on $\Gamma(X,\mathcal F^\vee)$, by the dual-spectrum
calculation of [lemma-filtrations-spectra]. By
[lemma-degree-zero-top-cohomology--5], at some closed point $x$ the
number $\gamma^{-\deg(x)}$ is an eigenvalue on
$(\mathcal F^\vee)_{\bar x}$. The stalk of the dual is the dual of the
stalk, so $\gamma^{\deg(x)}$ is an eigenvalue on $\mathcal F_{\bar x}$.
The punctual bound and $\deg(x)>0$ give $|\iota(\gamma)|\le q^{a/2}$.

On a smooth geometrically connected affine curve,
[lemma-degree-zero-top-cohomology--2] identifies $H_c^2$ with
$Q(\mathcal F)(-1)$. Its eigenvalues are therefore $q\gamma$, and
$|\iota(q\gamma)|\le q^{(a+2)/2}$. This recovers the top-degree bound
in the affine case from the formalized coinvariant estimate.
