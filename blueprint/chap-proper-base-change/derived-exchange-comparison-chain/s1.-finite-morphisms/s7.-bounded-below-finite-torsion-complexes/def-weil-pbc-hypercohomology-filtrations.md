+++
id = "def-weil-pbc-hypercohomology-filtrations"
kind = "definition"
title = "Hypercohomology filtrations"
order = 1729
uses = ["def-weil-pbc-derived-exchange"]
+++
Let $K\in D^+(X_{\mathrm{et}})$ have torsion cohomology sheaves and choose
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
