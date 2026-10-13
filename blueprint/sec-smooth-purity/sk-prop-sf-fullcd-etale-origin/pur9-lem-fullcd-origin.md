+++
id = "pur9-lem-fullcd-origin"
kind = "lemma"
title = "Proper direct images of sheaves of étale origin"
order = 2130
tags = ["latex:bplemma"]
uses = ["pur7710-input-affine-cd"]
+++
Assume Inputs “Forgetting finite coefficient actions in direct images” (`pur7710-input-cohomology-coefficients`, see [sk-thm-sf-comp-composition]), [pur7710-input-affine-cd] and “The qcqs direct-image comparison theorem” (`pur7710-input-qcqs-comparison`, see [sk-prop-sf-comp-coherence]). Let $p:\overline X\to Y$ be a proper morphism of $k$-schemes of finite type, and let $e\geq0$ be an integer such that every geometric fibre of $p$ has dimension at most $e$. Let $v:Y'\to Y$ be a morphism of $k$-schemes of finite type, with base change $p':\overline X'=\overline X\times_YY'\to Y'$. Then for every sheaf $M$ of $\mathcal O_E/\varpi^n$-modules on $\overline X'_{\Et}$, placed in degree zero,

$$
\mathcal H^r\bigl(Rp'_{*,\mathcal O_E/\varpi^n}L\nu^*_{\overline X',\mathcal O_E/\varpi^n}M\bigr)=0\qquad(r>2e),
$$

with $Rp'_{*,\mathcal O_E/\varpi^n}$ of Definition “Finite-coefficient derived direct image” (`pur713-def-derived-push`) and $L\nu^*$ of Definition “The derived site inverse image” (`pur456-def-site-inverse-derived`, see [sk-prop-sf-comp-coherence]). The bound $2e$ is independent of $v$ and $M$.
