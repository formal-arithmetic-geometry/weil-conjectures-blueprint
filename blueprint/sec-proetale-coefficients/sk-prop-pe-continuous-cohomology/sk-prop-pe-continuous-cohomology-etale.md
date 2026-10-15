+++
id = "det-pe-continuous-cohomology-etale"
kind = "lemma"
title = "Identification with continuous étale cohomology"
uses = ["det-pe-continuous-cohomology-limit", "sk-prop-sf-comparison", "lem-weil-pbc-comparison-global-cohomology"]
+++
Let $X$ be a scheme, let $\Sh(X_{\Et})^{\mathbf N}$ be the abelian category of
inverse systems $(G_n)_{n\geq1}$ of abelian étale sheaves, and let
$\Gamma_{\mathrm{cont}}((G_n))=\Gamma(X_{\Et},\varprojlim_nG_n)=
\varprojlim_n\Gamma(X_{\Et},G_n)$. For an inverse system $(F_{n,\Et})$ with
epimorphic transitions and $F_n=\nu_X^*F_{n,\Et}$,

$$
R\Gamma_{\mathrm{cont}}((F_{n,\Et}))\simeq R\varprojlim_nR\Gamma(X_{\Et},F_{n,\Et})
\simeq R\varprojlim_nR\Gamma(X_{\Proet},F_n)\simeq R\Gamma(X_{\Proet},\varprojlim_nF_n).
$$
