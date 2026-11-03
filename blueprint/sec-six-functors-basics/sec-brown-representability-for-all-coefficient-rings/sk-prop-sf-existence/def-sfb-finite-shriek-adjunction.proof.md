+++
kind  = "proof"
of    = "def-sfb-finite-shriek-adjunction"
+++
Write $K=\nu_X^*K_0$ with $K_0$ a bounded below étale complex. The bijection is the chain
$$
\Hom(Rf_!\nu_X^*K_0,L)\simeq\Hom(\nu_Y^*Rf^{\et}_!K_0,L)\simeq\Hom(Rf^{\et}_!K_0,R\nu_{Y,*}L)
\simeq\Hom(K_0,f^\times R\nu_{Y,*}L)\simeq\Hom(\nu_X^*K_0,\nu_X^*f^\times R\nu_{Y,*}L).
$$
The first step is the compact-support comparison $Rf_!\nu_X^*\simeq\nu_Y^*Rf^{\et}_!$ on bounded
below objects, from extension by zero ([lem-cbc-proetale-extension-zero-comparison]) and proper
direct image. The second is the adjunction $\nu^*\dashv R\nu_*$, the third the étale adjunction
of [thm-sfb-finite-lower-shriek-left-adjoint], and the last the full faithfulness of $\nu_X^*$
on bounded below objects ([thm-weil-pbc-site-comparison]); here $f^\times R\nu_{Y,*}L$ is
bounded below by [lem-sfb-finite-upper-shriek-bounded-below]. The counit is the image of the
identity of $Rf^!L$, and the restriction to $P$ and $Q$ is formal.
