+++
id = "def-weil-pbc-hypercohomology-filtrations-detailed"
kind = "theorem"
title = "Hypercohomology spectral sequences"
order = 1182
lean = ["AlgebraicGeometry.Etale.hypercohomologySpectralSequence", "AlgebraicGeometry.Etale.hypercohomologySpectralSequence_baseChange"]
uses = ["def-weil-pbc-derived-exchange"]
+++
Let $K\in\Dplus(X_{\Et})$ have torsion cohomology and choose $a$ with
$\mathcal H^q(K)=0$ for $q<a$. Canonical truncations define spectral sequences

$$
 E_2^{p,q}=R^pf_*\mathcal H^q(K)
 \Longrightarrow\mathcal H^{p+q}(Rf_*K)
$$

and

$$
 E_2'{}^{p,q}=R^pf'_*g'^{-1}\mathcal H^q(K)
 \Longrightarrow\mathcal H^{p+q}(Rf'_*g'^{-1}K),
$$

whose filtration in degree $n$ is the image filtration obtained from
$\tau_{\leq q}K\to K$.

## Proof

The truncation triangles $\tau_{\leq q-1}K\to\tau_{\leq q}K\to\mathcal
H^q(K)[-q]\to$ are the truncation couple of the spectral-sequence chapter, so
its truncation spectral sequence, applied in the dictionary of that chapter to
the left exact functor $f_*$, supplies the first displayed spectral sequence
with the image filtration, its $E_2$-page being $E_2^{p,q}=R^pf_*\mathcal
H^q(K)$ by the shift identification and the finite-filtration induction. The
second sequence is the same theorem applied to $g'^{-1}K$, exactness of
$g'^{-1}$ giving $\mathcal H^q(g'^{-1}K)=g'^{-1}\mathcal H^q(K)$ and hence the
displayed $E_2'$-page.

Unresolved dependencies: def:weil-pbc-derived-categories, def:sp-truncation-couple, thm:sp-truncation-e2, def:sp-etale-dictionary, def:weil-pbc-direct-image, lem:sp-shift-identification, lem:sp-finite-filtration-induction
