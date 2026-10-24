+++
id = "sk-p-real-integral"
kind = "proposition"
title = "Lattices and representations on a regular scheme"
order = 3782
uses = ["sk-lem-finite", "sk-lem-stratified-lattice", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-pe-constructible-comparison"]
lean = ["AlgebraicGeometry.ProEtale.exists_lisseMonodromy"]
tags = ["sketch"]
+++
Let $X$ be a nonempty connected regular Noetherian scheme, that is,
locally Noetherian and quasi-compact (for instance a connected smooth
scheme of finite type over a field), and fix a geometric point $\bar x$.
The fibre functor $\mathcal F\mapsto\mathcal F_{\bar x}$, formed from the
finite reductions of a lattice, is an equivalence between lisse
$\overline{\mathbf Q}_{\ell,X}$-modules, in the pro-étale coefficient
category, and continuous finite-dimensional
$\overline{\mathbf Q}_\ell$-representations of the profinite group
$\pi_1(X,\bar x)$ ([thm-lisse-qlbar-representations]). Each of these
representations is defined over a finite extension $E/\Ql$ inside
$\overline{\mathbf Q}_\ell$. A continuous representation of a compact group
on a finite-dimensional $E$-vector space stabilizes an $\mathcal O_E$-lattice.

*Complement.* On a smooth geometrically connected curve
$C_0/\Fq$ with a nonempty open $U_0\subseteq C_0$, every lisse
$\overline{\mathbf Q}_{\ell,U}$-module on $U$, with geometric representation
$(V,\rho)$, for instance the sheaf underlying a lisse Weil sheaf on $U_0$,
has, after a finite extension of $E$, an
$\mathcal O_E$-lattice $L\subset V$ with $\rho(\pi_1(U))L=L$, whose
reductions $L/\mathfrak m_E^nL$ have finite images of $\pi_1(U)$ and are the
stalks of the finite reductions of a lisse $\mathcal O_{E,U}$-lattice in the
underlying sheaf ([p-real-integral]).
