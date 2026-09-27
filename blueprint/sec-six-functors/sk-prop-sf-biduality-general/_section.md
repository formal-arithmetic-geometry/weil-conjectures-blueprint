+++
id = "sk-prop-sf-biduality-general"
kind = "section"
title = "General Verdier biduality"
order = 2113
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_verdierDual"]
+++
*Proposition (sketch).*

Let $Y$ be a separated finite-type $k$-scheme whose structure morphism $a_Y$
carries the ambient datum of [sk-def-sf-admissible], and let $\Lambda$ be a
coefficient stage. Then $\mathbb D_Y=\RHom_\Lambda(-,\omega_{Y,\Lambda})$
with $\omega_{Y,\Lambda}=Ra_Y^!\Lambda$ is a contravariant exact
anti-equivalence of $\Dctf(Y,\Lambda)$ with $\mathbb D_Y\mathbb D_Y\cong \mathrm{id}$: the double-dual morphism $\delta_K$ is an isomorphism for every
$K$.
Chapter 1 (framework chapter), prop:functor-package(7), restated
as thm:sf-biduality of `10b_six_functor_formalism.tex`, after
Deligne, *SGA $4\frac12$*, Ch. 5 (Dualité) 1.1–1.2 and Ch. 7
(Théorèmes de finitude) 4.1–4.6: locality, a finite smooth
stratification, the locally-free case on a stratum, and the restriction to a
stratum; the algebraic half of the coefficient hypothesis is that the
coefficient stages are quasi-Frobenius rings, so that finite modules are
reflexive over them.
the admissibility of $a_Y$, i.e. the same hypothesis as
prop:sf-existence(b).

Uses: `prop:functor-package`, `thm:sf-biduality`
