+++
id = "thm-fd-transform-well-defined"
kind = "theorem"
title = "Well-definedness of the Fourier–Deligne transform"
order = 3041
lean = ["AlgebraicGeometry.Etale.boundedConstructible_fourierTransform_obj_of_boundedConstructible", "AlgebraicGeometry.Etale.fourierTransformBoundedConstructible"]
uses = ["def-fd-kernel", "def-fd-transform", "def-weil-pbc-scheme-conventions", "prop-functor-package", "prop-kernel-lisse", "sk-def-sfb-bounded-constructible", "sk-thm-sf-ctf-stability", "sk-prop-ctf-finite-comparison"]
+++
Let $\pi:V\to S$, $\pi':V'\to S$, $b$, $\Psi$, $r\in\mathbf Z$ and the
projections $p_1,p_2$ be as in [def-fd-transform], with
$p_2:V\times_SV'\to V'$ of finite type and admitting a compactification.

1. *Finite coefficients.* Let $\Lambda$ be a finite commutative ring in
   which $p$ is invertible and whose exponent is invertible on $S$, and
   assume that $V'$ is locally of finite type over some field $k$. Let
   $D^b_c(-,\Lambda)$ denote the full subcategory of the derived category of
   étale sheaves of $\Lambda$-modules consisting of the bounded complexes
   with constructible cohomology sheaves. Then for every
   $K\in D^b_c(V,\Lambda)$ one has
   $\operatorname{FT}^{\mathrm{ét}}_\psi(K)\in D^b_c(V',\Lambda)$, so that
   $\operatorname{FT}^{\mathrm{ét}}_\psi$ restricts to a functor
   $D^b_c(V,\Lambda)\to D^b_c(V',\Lambda)$. For finite admissible $\Lambda$
   the same holds for $\operatorname{FT}_\psi$ on the pro-étale categories.
2. *$\ell$-adic coefficients.* Let $\Lambda\in\{\mathcal O_E,E,\Qlb\}$ be
   regarded as a condensed ring, with $\Psi$ valued in $\Lambda(*)^\times$,
   and let $V,V',S$ be schemes of finite type over a finite or algebraically
   closed field. Then $\operatorname{FT}_\psi$ restricts to an exact functor

   $$
   \operatorname{FT}_\psi:
   D^b_c(V,\Lambda)\longrightarrow D^b_c(V',\Lambda)
   $$

   between the bounded constructible subcategories of
   $D(V_{\mathrm{proét}},\Lambda)$ and $D(V'_{\mathrm{proét}},\Lambda)$
   ([sk-def-sfb-bounded-constructible]).
