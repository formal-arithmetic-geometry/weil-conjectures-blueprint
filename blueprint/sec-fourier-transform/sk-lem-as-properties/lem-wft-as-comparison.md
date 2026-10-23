+++
id = "lem-wft-as-comparison"
kind = "lemma"
title = "The two Artin–Schreier models of $\\mathcal L_\\psi$"
order = 3931
uses = ["def-fd-additive-character", "def-fd-artin-schreier-sheaf", "lem-fd-as-cover"]
+++
Let $k_0=\mathbf F_q$ with $m=[k_0:\mathbf F_p]$, let $\Lambda$ be a
coefficient ring as in [def-fd-artin-schreier-sheaf], and let
$\Psi:\mathbf F_p\to\Lambda^\times$ be a nontrivial character.

1. If $\Lambda$ is a field (for instance $E\supset\mu_p$ or
   $\overline{\mathbf Q}_\ell$), every additive character
   $\psi:k_0\to\Lambda^\times$ is of the form
   $\psi(z)=\Psi(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$ for a unique
   $a\in k_0$, and $\psi$ is nontrivial exactly when $a\neq0$.
2. Let $\psi(z)=\Psi(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$ with
   $a\in k_0^\times$, let $X_0$ be a $k_0$-scheme and
   $f\in\Gamma(X_0,\mathcal O_{X_0})$. Let
   $\pi_q:Y_q=\operatorname{Spec}\mathcal O_{X_0}[y]/(y^q-y-f)\to X_0$ be the
   pullback along $f$ of $\mathrm{AS}_q$, with the translations $\sigma_c$,
   $c\in k_0$, and let $\pi_p:Y_p\to X_0$ be the Artin–Schreier covering of
   [lem-fd-as-cover] for the function $af$, with the translations
   $\sigma_b$, $b\in\mathbf F_p$. The $X_0$-morphism
   $h_a:Y_q\to Y_p$, $u\mapsto\operatorname{Tr}(ay):=\sum_{0\le i<m}(ay)^{p^i}$,
   satisfies $h_a\circ\sigma_c=\sigma_{\operatorname{Tr}(ac)}\circ h_a$, and
   pullback along it induces an isomorphism

   $$
   e_\Psi\,\pi_{p*}\Lambda\xrightarrow{\ \sim\ }e_\psi\,\pi_{q*}\Lambda=\mathcal L_{\psi,f}
   $$

   from the $\Psi$-isotypic part of $\pi_{p*}\Lambda$ onto the Artin–Schreier
   sheaf of [def-fd-artin-schreier-sheaf] (for $k=k_0$ and the character
   $\psi$).
3. On $\mathbf A^1_{k_0}$ with $f=x$, the morphism $h_a$ sends the root
   $y=0$ over $x=0$ to the root $u=0$, so the trivializations of the stalks at
   zero given by evaluation at these roots correspond under the isomorphism
   of (2).

For $a=1$, i.e. $\psi=\Psi\circ\operatorname{Tr}_{k_0/\mathbf F_p}$, this
identifies $\mathcal L_{\psi,f}$ with the summand $e_\Psi\pi_{p*}\Lambda$ of
the $\mathbf F_p$-covering of $f$ itself.
