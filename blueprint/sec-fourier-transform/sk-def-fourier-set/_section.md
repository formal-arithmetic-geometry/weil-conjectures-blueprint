+++
id = "sk-def-fourier-set"
kind = "definition"
title = "The coefficient setting: six operations only"
order = 3013
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible"]
uses = ["sk-def-sf-setting", "sk-def-sfb-bounded-constructible", "sk-prop-sfb-finite-extension-compatibility", "sk-prop-ctf-finite-comparison"]
tags = ["sketch"]
+++
Fix a prime $p$, a power $q=p^a$, the fields $k_0=\Fq$ and $k=\bar k_0$, a
prime $\ell\ne p$, and a finite extension $E/\Ql$ with algebraic closure
$\Qlb$. All schemes are separated of finite type over $k_0$. We use:
the bounded constructible derived category
$D^b_c(X,E)\subset D(X_{\mathrm{proét}},E)$ of bounded complexes of
$E_X$-modules with constructible cohomology sheaves, $E_X=p_X^*E$ the
coefficient sheaf of the condensed ring $E$ ([sk-def-sf-setting],
[sk-def-sfb-bounded-constructible]) — *not* the derived category of
discrete sheaves of $E$-modules on the small étale site, on which the
base-change isomorphisms fail — and likewise
$D^b_c(X,\Qlb)\subset D(X_{\mathrm{proét}},\Qlb)$, which receives
$D^b_c(X,E)$ by the flat extension of scalars $\QbarX\otimes_{E_X}-$
([sk-prop-sfb-finite-extension-compatibility]); with the six operations
$Lf^*,Rf_*,Rf_!,Rf^!,\otimes^L, R\mathcal H om$ of the six-functor package
on these categories, the compact-support direct image
$Rf_!=Rf_*\circ j_!$ read through a compactification, ordinary and
compact-support cohomology, and the Tate twists. For a finite coefficient
ring $A$ the pro-étale categories are identified with the étale ones
([sk-prop-ctf-finite-comparison]), and torsion arguments may be made on the
small étale site. The additive character $\psi$ takes values in
$\mu_p\subset\Qlb^\times$, so the Artin–Schreier sheaf and the Fourier
kernel $\mathcal K_\psi$ are a priori $\Qlb$-sheaves; we assume throughout
that $\mu_p\subset E$, so that $\psi$ is $E$-valued, $\mathcal K_\psi$ is a
lisse $E_X$-module of rank one, and the tensor product $\otimes^L_E$ in the
definition of the transform makes sense on $\Dbc(V,E)$. (Without this
assumption the transform is defined with coefficients $\Qlb$, or over
$E(\mu_p)$ after extension of scalars.) No weight, no $L^2$-weight
parameter and no purity notion is used
anywhere in this file; the Tate twist is a coefficient normalization (the
blueprint records its definition among the weight foundations, but no weight
statement of that chapter is used below).
