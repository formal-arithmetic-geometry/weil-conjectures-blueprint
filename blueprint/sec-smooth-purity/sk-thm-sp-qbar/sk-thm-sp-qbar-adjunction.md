+++
id = "det-sp-qbar-adjunction"
kind = "proposition"
title = "The $\\overline{\\mathbf Q}_\\ell$ purity adjunction and purity map"
order = 3018
uses = ["det-sp-qbar-finite-descent", "det-sp-rational-adjunction", "det-sp-field-extension-towers", "det-sp-unique-right-adjoint"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. For
$M\in\Dbc(X,\Qlb)$ and $K\in\Dbc(Y,\Qlb)$ with models $M_E,K_E$ over a finite
$E$, the composite

$$
\operatorname{Hom}(Rf_{!,\Qlb}M,K)\simeq\varinjlim_F\operatorname{Hom}(Rf_{!,F}M_F,K_F)
\simeq\varinjlim_F\operatorname{Hom}(M_F,f^*_FK_F(d)[2d])\simeq\operatorname{Hom}(M,f^*_{\Qlb}K(d)[2d])
$$

is a well-defined bijection, independent of the models and natural in $M,K$;
hence $Rf_{!,\Qlb}\dashv f^*_{\Qlb}(-)(d)[2d]$. By [det-sp-unique-right-adjoint]
applied to the Brown adjoint there is a counit-preserving isomorphism
$\gamma_{f,\Qlb}:f^*_{\Qlb}(-)(d)[2d]\xrightarrow{\sim}f^!_{\Qlb}$ of functors
$\Dbc(Y,\Qlb)\to\Dbc(X,\Qlb)$, and the unit $\eta_{f,\Qlb}$ and counit
$\varepsilon_{f,\Qlb}$ are identified with those transported from finite
extensions of $\Ql$.
