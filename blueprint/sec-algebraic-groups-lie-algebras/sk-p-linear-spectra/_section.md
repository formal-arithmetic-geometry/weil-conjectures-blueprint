+++
id = "sk-p-linear-spectra"
kind = "proposition"
title = "Spectra of the operations"
order = 2550
uses = ["sk-d-linear", "sk-d-weights"]
lean = ["LinearMap.charpoly_roots_tensorProduct", "LinearMap.charpoly_roots_exteriorPower", "LinearMap.charpoly_roots_dualMap_symm"]
tags = ["sketch"]
+++
If $f$ has eigenvalue multiset
$\operatorname{eig}(f)=\{\alpha_1,\ldots,\alpha_r\}$ and $g$ has
$\{\beta_1,\ldots,\beta_t\}$, both with multiplicity, then

$$
\operatorname{eig}(f\otimes g)=\{\alpha_i\beta_j\},\quad
\operatorname{eig}\bigl(\textstyle\bigwedge^sf\bigr)
=\{\alpha_{i_1}\cdots\alpha_{i_s}:i_1<\cdots<i_s\},\quad
\operatorname{eig}(f^\vee)=\{\alpha_i^{-1}\}
$$

(the last for invertible $f$, where $f^\vee=(f^{-1})^*$ is the
contragredient on the dual space); in particular $\alpha^n$ is an eigenvalue of
$f^{\otimes n}$. Concretely, in an exterior basis a diagonal map with
entries $c_1,\ldots,c_r$ has entries $c_{i_1}\cdots c_{i_s}$ with
$i_1<\cdots<i_s$.
