+++
id = "prop-pe-continuous-etale-cohomology"
kind = "proposition"
title = "Identification with continuous étale cohomology"
order = 1054
tags = ["not-formalized"]
uses = ["det-pe-continuous-cohomology-limit", "thm-weil-pbc-site-comparison"]
+++
Let $X$ be a scheme, let $\Sh(X_{\Et})^{\mathbf N}$ be the abelian category of
inverse systems $(G_n)_{n\geq1}$ of abelian étale sheaves, and let $\Delta\mathbf Z$
be the constant system on the constant sheaf $\mathbf Z$. The *continuous étale
cohomology* of a system is

$$
H^i_{\mathrm{cont}}\bigl(X,(G_n)\bigr)=\operatorname{Ext}^i_{\Sh(X_{\Et})^{\mathbf N}}\bigl(\Delta\mathbf Z,(G_n)\bigr);
$$

since $\operatorname{Hom}(\Delta\mathbf Z,(G_n))=\Gamma(X_{\Et},\varprojlim_nG_n)$, these
are the right derived functors of $(G_n)\mapsto\Gamma(X_{\Et},\varprojlim_nG_n)$.
For an inverse system $(F_{n,\Et})$ with epimorphic transitions and
$F_n=\nu_X^*F_{n,\Et}$, there are isomorphisms

$$
H^i_{\mathrm{cont}}\bigl(X,(F_{n,\Et})\bigr)\cong H^i\bigl(X_{\Proet},\varprojlim_nF_n\bigr)
\qquad(i\geq0).
$$

*Not formalized in Lean.* This is the continuous-étale clause of the tex proposition
"Continuous cohomology as pro-étale cohomology" (pe:continuous-cohomology), which nothing
else uses; it is recorded here and will not be formalized.
