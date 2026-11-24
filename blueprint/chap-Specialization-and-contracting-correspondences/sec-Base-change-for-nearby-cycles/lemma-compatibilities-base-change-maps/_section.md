+++
id = "lemma-compatibilities-base-change-maps"
kind = "lemma"
title = "Base change maps and the projection formula"
order = 1664
lean = ["CategoryTheory.whiskerRight_comp_μ_comp_map_comp_mateEquiv_app"]
+++
Let $f:V\to W$ be a morphism of separated $S$-schemes of finite type,
and let $M,N\in \href{@definition-constructible-sheaves}{D^b_c(W_\eta,A)}$. Then the two maps
$\Psi_V\href{@theorem-existence-exceptional-inverse-image}{f_\eta^!M}\otimes^{\mathbf L} f_s^*\Psi_WN\to \href{@theorem-existence-exceptional-inverse-image}{f_s^!}\Psi_W(M\otimes^{\mathbf L} N)$

$$
\beta_f \Psi_V(t_{f_\eta})\mu_V(1\otimes\alpha_f)
=\href{@theorem-existence-exceptional-inverse-image}{f_s^!}\mu_W\ t_{f_s}(\beta_f\otimes1)
\tag{E.8}
$$

are equal.
