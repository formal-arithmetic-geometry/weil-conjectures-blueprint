+++
id = "lem-wft-as-unit-trivialization"
kind = "lemma"
title = "The trivialization of $\\mathcal L_\\psi$ at zero"
order = 4152
uses = ["def-fd-artin-schreier-sheaf", "lem-wft-as-comparison", "lem-fd-as-characters", "lem-fd-as-lisse"]
+++
Let $\psi:k_0\to\Lambda^\times$ be a nontrivial additive character, with
$\Lambda=E\supset\mu_p$ or $\overline{\mathbf Q}_\ell$, and let
$\mathcal L_\psi$ be the Artin–Schreier sheaf on $\mathbf A^1_{k_0}$ of
[def-fd-artin-schreier-sheaf]. Evaluation of isotypic functions at the root
$y=0$ of $y^q-y=0$ gives a trivialization
$\varepsilon:0^*\mathcal L_\psi\xrightarrow{\sim}\Lambda$ of the stalk at the
origin. With $m,\operatorname{pr}_1,\operatorname{pr}_2:\mathbf A^2\to\mathbf A^1$
the addition and the projections, there are isomorphisms

$$
\mu:\ m^*\mathcal L_\psi\xrightarrow{\ \sim\ }
\operatorname{pr}_1^*\mathcal L_\psi\otimes\operatorname{pr}_2^*\mathcal L_\psi,
\qquad
\delta:\ \mathcal L_\psi^\vee\xrightarrow{\ \sim\ }\mathcal L_{\psi^{-1}},
$$

such that $(\varepsilon\otimes\varepsilon)\circ\mu_{(0,0)}=\varepsilon$ at
the origin, $\delta$ at the origin carries $(\varepsilon^{\vee})^{-1}$ to
$\varepsilon$ (for $\psi^{-1}$), $\mu$ is associative on $\mathbf A^3$, and the
restriction of $\mu$ along $\{0\}\times\mathbf A^1$ is the identity of
$\mathcal L_\psi$ through $\varepsilon$ (unit compatibility). Under
[lem-wft-as-comparison] (3), $\varepsilon$ is the trivialization given by
the root $u=0$ of the $\mathbf F_p$-model. Consequently, for every
$k_0$-scheme $X_0$, the sheaf $\mathcal L_{\psi,0}$ attached to the zero
function is canonically $\Lambda_{X_0}$, and for $f\in\Gamma(X_0,\mathcal O)$
the pairing
$\mathcal L_{\psi,f}\otimes\mathcal L_{\psi^{-1},f}\cong
\mathcal L_{\psi,f}\otimes\mathcal L_{\psi,-f}\cong\mathcal L_{\psi,0}
\cong\Lambda_{X_0}$ is the evaluation pairing of $\delta$.
