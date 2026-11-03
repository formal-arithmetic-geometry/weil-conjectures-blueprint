+++
id = "det-tf-fixed-point-equations"
kind = "lemma"
title = "Equations of the Frobenius fixed scheme"
order = 3761
uses = ["def-trf-fixed-scheme", "def-trf-scheme-frobenius"]
+++
Let $X_0=\operatorname{Spec}A_0$ with $A_0=k_0[t_1,\ldots,t_r]/\mathfrak a$, put
$X=X_0\times_{k_0}k=\operatorname{Spec}B$ with $B=k[t_1,\ldots,t_r]/\mathfrak a_B$,
$\mathfrak a_B=\mathfrak a\,k[t]$, and let $m\geq1$. The fixed scheme
$\operatorname{Fix}(\Phi_X^m)$ ([def-trf-fixed-scheme]) of the $q^m$-power Frobenius
$\Phi_X^m$ ([def-trf-scheme-frobenius]) is the closed subscheme of $X$ cut out by the ideal

$$
 \bigl(t_1^{q^m}-t_1,\ldots,t_r^{q^m}-t_r\bigr)B,
$$

that is,
$\operatorname{Fix}(\Phi_X^m)=\operatorname{Spec}k[t_1,\ldots,t_r]/\bigl(\mathfrak a_B+(t_i^{q^m}-t_i)_i\bigr)$.
These descriptions are compatible with restriction to affine opens of $X_0$.
