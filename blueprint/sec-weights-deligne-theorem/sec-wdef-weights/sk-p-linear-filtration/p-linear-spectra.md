+++
id = "p-linear-spectra"
kind = "theorem"
title = "Spectra of the operations"
order = 3965
uses = ["p-linear-triangular"]
tags = ["latex:proposition"]
lean = ["LinearMap.charpoly_roots_tensorProduct", "LinearMap.charpoly_roots_exteriorPower", "LinearMap.charpoly_roots_dualMap_symm"]
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
$i_1<\cdots<i_s$. Applied to $\rho_V(w)$ and $\rho_W(w)$, these compute the spectra of the
tensor products, exterior powers and determinants of representations.
