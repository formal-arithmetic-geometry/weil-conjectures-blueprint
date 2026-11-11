+++
id = "lemma-scheme-frobenius-geometric-frobenius"
kind = "lemma"
title = "Scheme Frobenius and geometric Frobenius"
order = 954
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "definition-frobenius-operator", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $\operatorname{Fr}_X$ be the semilinear geometric Frobenius
of Definition [definition-weil-structure], and for a morphism
$\phi:\operatorname{Fr}_X^*K\to K$ put
$\phi_m=\phi\circ \operatorname{Fr}_X^*\phi\circ\cdots\circ(\operatorname{Fr}_X^{m-1})^*\phi$.
There are natural isomorphisms

$$
\kappa_m:(\Phi_X^m)^*K\xrightarrow{\sim}(\operatorname{Fr}_X^m)^*K
$$

compatible with iteration. For a Weil structure
$\phi:\operatorname{Fr}_X^*K\xrightarrow{\sim}K$, put
$\psi=\phi\kappa_1$. Then

$$
\psi_m=\phi_m\kappa_m,
\qquad T_{c_m}(\psi_m)=\operatorname{Frob}_{X,K}^{m},
$$

where $\operatorname{Frob}_{X,K}$ is the geometric Frobenius operator
on compact cohomology of
Definition [definition-frobenius-operator]. The same identity of
operators holds for an arbitrary morphism $(\operatorname{Fr}_X^m)^*K\to K$ in place
of $\phi_m$.
