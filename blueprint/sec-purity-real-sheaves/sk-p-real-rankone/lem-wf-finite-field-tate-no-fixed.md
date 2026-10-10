+++
id = "lem-wf-finite-field-tate-no-fixed"
kind = "lemma"
title = "Arithmetic Frobenius has no fixed vector on the Jacobian Tate module"
order = 2622
uses = ["d-ab-field", "def-sc-jacobian", "def-tate-module-abelian-group", "def-wf-abelian-tate-module", "lem-wf-geometric-jacobian-galois-action", "prop-av-tate-no-frobenius-fixed", "thm-av-final", "thm-pd-jacobian-general-field"]
+++
Let $C_0/\mathbf F_Q$ be a smooth projective geometrically connected curve,
put $C=C_0\times_{\mathbf F_Q}\overline{\mathbf F}_Q$, and let $J$ be its
Jacobian, equipped with the canonical semilinear
action of arithmetic Frobenius $\sigma_Q:z\mapsto z^Q$
([lem-wf-geometric-jacobian-galois-action]). If $\ell\nmid Q$, then

$$
(T_\ell J)^{\sigma_Q=1}=0,
$$

and $\sigma_Q-1$ is an automorphism of the
rational Tate module $V_\ell J$.
