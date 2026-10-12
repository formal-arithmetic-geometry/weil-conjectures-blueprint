+++
id = "def-weil-pbc-hypercohomology-filtrations"
kind = "definition"
title = "Hypercohomology filtrations"
order = 1374
uses = ["def-sp-etale-dictionary", "def-sp-truncation-couple", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange", "def-weil-pbc-direct-image", "lem-sp-finite-filtration-induction", "lem-sp-shift-identification", "thm-sp-truncation-e2"]
+++
Let $K\in\Dplus(X_{\Et})$ have torsion cohomology sheaves and choose
$a$ with $\mathcal H^q(K)=0$ for $q<a$. The canonical truncation tower
$\tau_{\leq q}K$ defines spectral sequences

$$
E_2^{p,q}=R^pf_*\mathcal H^q(K)\Longrightarrow
\mathcal H^{p+q}(Rf_*K),
$$

and

$$
{E'}_2^{p,q}=R^pf'_*g'^{-1}\mathcal H^q(K)\Longrightarrow
\mathcal H^{p+q}(Rf'_*g'^{-1}K).
$$

Their filtration in total degree $n$ is the image filtration induced by
$\mathcal H^n(Rf_*\tau_{\leq q}K)\to\mathcal H^n(Rf_*K)$; the second
filtration is induced by
$\mathcal H^n(Rf'_*g'^{-1}\tau_{\leq q}K)\to \mathcal H^n(Rf'_*g'^{-1}K)$.
