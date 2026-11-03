+++
id = "lem-fd-as-characters"
kind = "lemma"
title = "Isotypic decomposition of the Artin–Schreier pushforward"
lean = ["AlgebraicGeometry.nonempty_iso_dual_artinSchreier", "AlgebraicGeometry.nonempty_iso_artinSchreierOf_zero"]
order = 4150
uses = ["def-fd-artin-schreier-sheaf", "def-weil-pbc-etale-sheaves", "def-weil-pbc-finite-torsors", "sk-def-sfb-constructible", "lem-fd-as-cover", "lem-fd-character-orthogonality", "lem-wft-as-comparison"]
+++
With the $\mathbf F_p$-action of [lem-fd-as-cover], there is a canonical decomposition

$$
\pi_*\overline{\mathbf Q}_\ell\cong\bigoplus_{\chi\in\widehat{\mathbf F}_p}\mathcal L_\chi,
$$

where each $\mathcal L_\chi$ is lisse of rank one on $X_0$, and $\mathcal L_0=1$ (for $\chi\neq0$ the summand $\mathcal L_\chi$ need not be nonconstant: all are constant when $f=0$). In particular, for $\psi=\Psi\circ\operatorname{Tr}_{k_0/\mathbf F_p}$ (so that $\mathcal L_{\psi,f}$ is the summand $\mathcal L_\chi$ with $\chi=\Psi$, by [lem-wft-as-comparison]),
$\mathcal L_{\psi,f}\otimes\mathcal L_{\psi,g}\cong\mathcal L_{\psi,f+g}$, $(\mathcal L_{\psi,f})^{-1}\cong\mathcal L_{\psi,-f}$, and $\mathcal L_{\psi^{-1},f}\cong\mathcal L_{\psi,-f}$.
