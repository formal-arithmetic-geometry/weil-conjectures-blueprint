+++
id = "thm-lisse-qlbar-representations"
kind = "theorem"
title = "Lisse $\\overline{\\mathbf Q}_\\ell$-sheaves and continuous representations"
lean = ["AlgebraicGeometry.ProEtale.exists_lisseMonodromy"]
order = 3416
uses = ["cor-galois-lisse-representations", "def-galois-fibre-functor", "thm-galois-fundamental", "sk-def-sfb-constructible", "det-def-sfb-module-pushforward-pullback", "sk-prop-pe-condensed-point", "sk-prop-pe-finite-local-systems", "sk-prop-sfb-qlbar-colimit-x", "sk-lem-stratified-lattice", "det-lem-stratified-lattice-rank", "det-lem-stratified-lattice-scheme", "sk-thm-sfb-qlbar-two-colimit", "det-lem-coefficient-finite-descent-lisse", "det-lem-coefficient-finite-descent-sections"]
+++
Let $X$ be a connected Noetherian (locally Noetherian and quasi-compact)
scheme with a geometric point
$\bar x:\Spec\kappa\to X$, and let $\pi_1=\pi_1(X,\bar x)$ be the profinite
fundamental group of [def-galois-fibre-functor]. Let $E\subset\Qlb$ be a
finite extension of $\Ql$ with uniformizer $\pi_E$, and regard
$\Lambda\in\{\mathcal O_E,E,\Qlb\}$ as a condensed ring, with
$\Lambda_X=p_X^*\Lambda$ on $X_{\mathrm{pro\acute et}}$.

A $\Lambda_X$-module $L$ is *lisse* if it has a finite constant local model
which is free, that is, $L|_{U_i}\cong\Lambda_{U_i}^{\oplus r_i}$ on a
pro-étale cover $\{U_i\to X\}$ ([sk-def-sfb-constructible] (1)). Its
*fibre* at $\bar x$ is $L_{\bar x}=\Gamma(\Spec\kappa,\bar x^*L)$, a finite
free $\Lambda$-module, since every pro-étale cover of $\Spec\kappa$ has a
section ([sk-prop-pe-condensed-point]). A lisse $E_X$-module $L$ is
*integral* if it contains a lisse $\mathcal O_{E,X}$-submodule $L_0$ with
$L_0[1/\ell]=L$, a *lattice*. A lisse $\QbarX$-module is *integral* if it is
isomorphic to $\QbarX\otimes_{E_X}L$ for some finite $E$ and some integral
lisse $E_X$-module $L$. A continuous representation of $\pi_1$ on a
finite-dimensional $\Qlb$-vector space $V$ is *defined over* $E$ if there is
a $\pi_1$-stable $E$-subspace $V_E$ with $\Qlb\otimes_EV_E=V$ on which
$\pi_1$ acts continuously for the $\ell$-adic topology.

**Theorem.** Let $X$ be connected, regular and Noetherian, that is, locally
Noetherian, regular and quasi-compact. Then every lisse
$\QbarX$-module is integral, and $L\mapsto L_{\bar x}$, with the action of
$\pi_1$ of (1)–(3) below, is an equivalence between lisse $\QbarX$-modules
and continuous finite-dimensional $\Qlb$-representations of $\pi_1$; each of
these representations is defined over some finite $E$. It is compatible with
tensor products and with extension of scalars along $E\subset F\subset\Qlb$.

More precisely, for every connected Noetherian $X$:

1. *Integral coefficients.* For a lisse $\mathcal O_{E,X}$-module $L_0$ the
   reductions $L_0/\pi_E^nL_0$ are classical locally constant sheaves of finite
   $\mathcal O_E/\pi_E^n$-modules ([sk-prop-pe-finite-local-systems]), so
   [cor-galois-lisse-representations] gives continuous actions of $\pi_1$ on
   their fibres, and $L_{0,\bar x}=\varprojlim_n(L_0/\pi_E^nL_0)_{\bar x}$
   carries the limit action. Then $L_0\mapsto L_{0,\bar x}$ is an equivalence
   between lisse $\mathcal O_{E,X}$-modules and continuous representations of
   $\pi_1$ on finite free $\mathcal O_E$-modules. Its reduction modulo
   $\pi_E^n$ is the equivalence of [cor-galois-lisse-representations] for the
   finite ring $\mathcal O_E/\pi_E^n$, applied to $L_0/\pi_E^nL_0$.
2. *Rational coefficients.* For an integral lisse $E_X$-module $L$ with
   lattice $L_0$, $L_{\bar x}=L_{0,\bar x}[1/\ell]$ with the action of (1).
   Then $L\mapsto L_{\bar x}$ is an equivalence between
   integral lisse $E_X$-modules and continuous representations of $\pi_1$ on
   finite-dimensional $E$-vector spaces. The action does not depend on the
   lattice used to define it.
3. *$\Qlb$-coefficients.* For $L\cong\QbarX\otimes_{E_X}L'$ with $L'$
   integral, $L_{\bar x}=\Qlb\otimes_EL'_{\bar x}$ with the action of (2).
   Then $L\mapsto L_{\bar x}$ is an equivalence between
   integral lisse $\QbarX$-modules and continuous finite-dimensional
   $\Qlb$-representations of $\pi_1$ defined over some finite $E$.
4. *Normality.* If $X$ is normal, every lisse $E_X$-module has a lattice, so
   every lisse $E_X$-module and every lisse $\QbarX$-module is integral, and
   (2), (3) apply to all of them. A regular $X$ is normal.
5. *Fields of definition.* Every continuous finite-dimensional
   $\Qlb$-representation of the profinite group $\pi_1$ is defined over some
   finite $E$.

By (3), (4) and (5) the conclusion of the theorem holds more generally for
every connected normal $X$.

Without normality (4) fails: the rank-one lisse module on the nodal curve
of [sk-lem-stratified-lattice] has no lattice, so it lies outside (2) and
(3); its monodromy, multiplication by $\ell$ on a $\mathbf Z$-torsor, does
not extend to the profinite completion.
