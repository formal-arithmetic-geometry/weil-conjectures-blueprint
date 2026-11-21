+++
id = "dag-lem-route-sp-integers-map-exists-unique"
kind = "dag-lemma"
title = "The integral coefficient inclusion is the unique ring map over E_X -> F_X."
name_showing = false
order = 187543
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-route-sp-integers-map-exists-unique"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spIntegersMap_existsUnique"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $\ell$ be a prime, fix an algebraic closure $\Omega=\overline{\mathbf Q}_\ell$ with its extending absolute value, and let $\mathbf Q_\ell\subseteq E\subseteq F\subseteq\Omega$ be finite subextensions, with their restricted absolute values and topologies `def-sfb-padic-subfield-condensed-ring`. Write $\mathcal O_H=\{x\in H:|x|\le1\}$ with its subspace topology, for $H=E,F$, and $\underline{\mathcal O_H}(S)=C(S,\mathcal O_H)$ for its condensed ring `def-sfb-padic-integers-condensed-ring`. Let $X$ be any scheme, using the small pro-étale site and universes of [def-weil-pbc-proetale-site, def-weil-size-convention]. Put $\mathcal O_{H,X}=p_X^*\underline{\mathcal O_H}$ and $H_X=p_X^*\underline H$, with the transported ring-object structures `sk-def-sfb-pulled-back-coefficients`. Let $a_{H,X}:\mathcal O_{H,X}\to H_X$ be the canonical integral inclusion `def-sfb-integers-to-subfield`, and let $i_{E,F,X}:E_X\to F_X$ be the coefficient map induced by the specified field inclusion `def-sfb-subfield-coefficient-map`. There exists exactly one morphism $\varphi:\mathcal O_{E,X}\to\mathcal O_{F,X}$ of underlying abelian sheaves such that it preserves the unit and multiplication of these ring objects and
$$a_{F,X}\circ\varphi=i_{E,F,X}\circ a_{E,X}.$$
Here preservation of the ring-object structure is the Lean predicate $\mathrm{IsMonHom}(\varphi)$, not the categorical monomorphism predicate.

(SHEAF DAG node `lem-route-sp-integers-map-exists-unique`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sfb-padic-subfield-condensed-ring`, `def-sfb-padic-integers-condensed-ring`, `def-weil-size-convention`, `sk-def-sfb-pulled-back-coefficients`, `def-sfb-integers-to-subfield`, `def-sfb-subfield-coefficient-map`.
