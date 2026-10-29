+++
id = "def-fourier-set"
kind = "definition"
title = "The coefficient setting of the Fourier transform"
order = 4142
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible"]
uses = ["def-sf-setting", "det-def-sfb-bounded-constructible", "det-prop-sfb-finite-extension-compatibility", "sk-prop-ctf-finite-comparison", "prop-functor-package"]
+++
Fix a prime $p$, a power $q=p^a$, the fields $k_0=\Fq$ and $k=\bar k_0$, a
prime $\ell\ne p$, and a finite extension $E/\Ql$ with algebraic closure
$\Qlb$. All schemes are separated of finite type over $k_0$. We use:
the bounded constructible derived category
$D^b_c(X,E)\subset D(X_{\mathrm{proét}},E)$ of bounded complexes of
$E_X$-modules with constructible cohomology sheaves, $E_X=p_X^*E$ the
coefficient sheaf of the condensed ring $E$ ([def-sf-setting],
[det-def-sfb-bounded-constructible]) — *not* the derived category of
discrete sheaves of $E$-modules on the small étale site, on which the
base-change isomorphisms fail — and likewise
$D^b_c(X,\Qlb)\subset D(X_{\mathrm{proét}},\Qlb)$, which receives
$D^b_c(X,E)$ by the flat extension of scalars $\QbarX\otimes_{E_X}-$
([det-prop-sfb-finite-extension-compatibility]); with the six operations
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
$E(\mu_p)$ after extension of scalars.) Fix a field embedding
$\iota:\Qlb\hookrightarrow\mathbf C$. Cohomology is taken after base change
to $k$, with the action of geometric Frobenius; the six operations are used
first with coefficients in $E$ and then, after extension of scalars, with
coefficients in $\Qlb$. The Tate twist is that of the weight foundations; the
only weight statements of this section are the purity of weight zero of the
character sheaf and the shift of the $L^2$ growth parameter under the
transform, both read off from trace functions.
