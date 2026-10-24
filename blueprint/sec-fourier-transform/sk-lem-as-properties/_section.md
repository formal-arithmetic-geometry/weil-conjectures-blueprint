+++
id = "sk-lem-as-properties"
kind = "lemma"
title = "The Artin–Schreier character sheaf"
order = 3922
uses = ["sk-def-purity-conv", "sk-prop-sfb-finite-extension-compatibility", "sk-prop-ctf-finite-comparison", "sk-def-sfb-constructible", "sk-thm-frobenius"]
tags = ["sketch"]
+++
Let $\psi:k_0\to E^\times$ be a nontrivial additive character.
There is a lisse rank-one $E$-sheaf $\mathcal L_\psi$ on
$\mathbf A^1_{k_0}$, with a specified trivialization at zero, such that

$$
 m^*\mathcal L_\psi\simeq
 \operatorname{pr}_1^*\mathcal L_\psi\otimes
 \operatorname{pr}_2^*\mathcal L_\psi,
 \qquad
 \mathcal L_\psi^\vee\simeq\mathcal L_{\psi^{-1}}.
$$

Here $m$ is the addition map, and the isomorphisms respect the
trivializations at zero. For $x\in\mathbf F_{q^n}$, the Frobenius
trace is

$$
 t_{\mathcal L_\psi,n}(x)
   =\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}(x)\bigr).
$$

In particular $\mathcal L_\psi$ is pure of weight zero.

*Complement* (notation and the two models used later). For a $k_0$-scheme
$X_0$ and $f\in\Gamma(X_0,\mathcal O_{X_0})$, viewed as $f:X_0\to\mathbf A^1_{k_0}$,
put $\mathcal L_{\psi,f}=\mathcal L_{\psi(f)}:=f^*\mathcal L_\psi$. Then
$\mathcal L_{\psi,f}\otimes\mathcal L_{\psi,g}\cong\mathcal L_{\psi,f+g}$ and
$\mathcal L_{\psi,f}^\vee\cong\mathcal L_{\psi,-f}\cong\mathcal L_{\psi^{-1},f}$,
and the geometric Frobenius at a closed point $u$ acts on
$\mathcal L_{\psi,f}$ by $\psi(\operatorname{Tr}_{\kappa(u)/k_0}f(u))$. The
sheaf has two models, which agree together with their trivializations at
zero: the $\psi$-isotypic part of the direct image along the
$k_0$-Artin–Schreier map $y\mapsto y^q-y$, and, writing
$\psi(z)=\Psi(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$ with $\Psi$ a
nontrivial character of $\mathbf F_p$ and $a\in k_0^\times$, the
$\Psi$-isotypic part of the direct image along the cover $u^p-u=ax$ (the
construction of the proof, also used for the Fourier kernel); the map
$y\mapsto u=\operatorname{Tr}_{k_0/\mathbf F_p}(ay)$ identifies them. The
same construction works for every admissible condensed coefficient ring
containing the values of $\psi$ (on the pro-étale site, and on the étale site
for finite coefficients), compatibly with extension of scalars.
