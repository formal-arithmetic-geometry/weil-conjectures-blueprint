+++
id = "thm-sp-truncation-e2"
kind = "theorem"
title = "The truncation hypercohomology spectral sequence"
order = 1987
lean = ["CategoryTheory.exists_truncationHypercohomology"]
uses = ["def-sp-convergence", "def-sp-etale-dictionary", "def-sp-exact-couple", "def-sp-image-filtration", "def-sp-injective-resolutions", "def-sp-truncation-couple", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange", "def-weil-pbc-direct-image", "lem-sp-shift-identification", "lem-sp-truncation-couple-exact", "thm-sp-half-plane-convergence"]
+++
Let $K$ be as in [def-sp-truncation-couple]. The spectral sequence of the
truncation couple [def-sp-truncation-couple] has

$$
 E_2^{p,q}=R^pv\bigl(\mathcal H^q(K)\bigr)
 \Longrightarrow\mathcal H^{p+q}(RvK),
$$

the abutment $\mathcal H^n(RvK)$ carrying the image filtration
[def-sp-image-filtration] of the maps $\mathcal H^n(Rv\,\tau_{\leq q}K)\to
\mathcal H^n(RvK)$; in each degree $n$ only $a\leq q\leq n$ occurs, so the
couple is regular and complete and the convergence is unconditional
([def-sp-convergence]).

In particular, in the dictionary [def-sp-etale-dictionary], let
$K\in\Dplus(X_{\Et})$ [def-weil-pbc-derived-categories] have torsion
cohomology sheaves, choose $a$ with $\mathcal H^q(K)=0$ for $q<a$, and let
$f\circ g'=g\circ f'$ be a square as in [def-weil-pbc-derived-exchange]. Taking
for $v$ the direct images [def-weil-pbc-direct-image] $f_*$, resp. $f'_*$
applied to $g'^{-1}K$, gives the *hypercohomology spectral sequences*

$$
E_2^{p,q}=R^pf_*\mathcal H^q(K)\Longrightarrow
\mathcal H^{p+q}(Rf_*K),
\qquad
{E'}_2^{p,q}=R^pf'_*g'^{-1}\mathcal H^q(K)\Longrightarrow
\mathcal H^{p+q}(Rf'_*g'^{-1}K),
$$

whose filtrations in total degree $n$ are the image filtrations of
$\mathcal H^n(Rf_*\tau_{\leq q}K)\to\mathcal H^n(Rf_*K)$, resp.
$\mathcal H^n(Rf'_*g'^{-1}\tau_{\leq q}K)\to \mathcal H^n(Rf'_*g'^{-1}K)$.
