+++
id = "lem-trf-localization-normal-cone"
kind = "lemma"
title = "Normal-cone reduction for the trace"
order = 2483
uses = ["def-trf-admissibility", "def-trf-correspondence", "def-trf-etale-base-change", "def-trf-fixed-scheme", "def-trf-global-operator", "def-trf-integration", "def-trf-local-term", "def-trf-trace-class", "lem-trf-contracting-local-model", "lem-trf-contracting-normal-cone-evaluation", "lem-trf-contracting-trace-stalk", "lem-trf-etale-pullback-trace-class", "lem-trf-frobenius-formal-contraction", "lem-trf-local-term-locality", "lem-trf-localization-diagonal", "thm-pur-diagonal-dualizing-object", "thm-pur-dnc-invariance", "thm-trf-dualizing-complex-composition"]
+++
Let $c=(c_1,c_2):C\to X\times_sX$ be an admissible correspondence with
$c_2$ proper, fixed scheme $F=\operatorname{Fix}(c)$ proper over
$s$, and let $K\in D^b_{ctf}(X,A)$. Assume that the localization
identity of [thm-trf-fixed-point-localization] holds for the
diagonal correspondence in the sense of
[lem-trf-localization-diagonal]. Then it holds for $c$: the
devissage that replaces the diagonal $\Delta_X$ by the graph of $c$,
deforms the graph section along the deformation to the normal cone of
the diagonal, and computes the resulting class on the normal cone, does
not change either side of the identity.
This reduction is assembled in the proof below from the
deformation-to-the-normal-cone invariance of the section invariant proved in
the smooth-purity chapter of this manuscript
([thm-pur-dnc-invariance], [thm-pur-diagonal-dualizing-object]),
the normal-cone evaluation of the trace map established in
[lem-trf-contracting-normal-cone-evaluation], and the contracting
computation [lem-trf-contracting-trace-stalk]. (*Source:* SGA 5,
Exposé III, 4.3 and 4.4; [Varshavsky,
Lefschetz–Verdier trace formula and a generalization of a theorem of
Fujiwara](https://arxiv.org/pdf/math/0505564), 2.1.1.)

## Proof

Write $I(c,u)$ for the localization identity for the admissible
[def-trf-correspondence] $c$ with coefficient map $u$,
admissibility being in the sense of [def-trf-admissibility],
namely that the categorical trace of the global
operator of [def-trf-global-operator] equals the integral over the
fixed scheme of [def-trf-fixed-scheme] of the trace class of
[def-trf-trace-class], the integral being that of
[def-trf-integration] and the local terms those of
[def-trf-local-term]. We assume $I(\Delta_X,\mathrm{id})$, which is
[lem-trf-localization-diagonal], and deduce $I(c,u)$.

*Step 1 (etale locality).* Both sides of $I$ are compatible with
etale base change: the trace class pulls back by
[lem-trf-etale-pullback-trace-class], while the global operator, the
integration and the fixed scheme are compatible with the base change of
[def-trf-etale-base-change] (the fixed scheme of a base-changed
correspondence is the base change of the fixed scheme, and the integration is
the trace along the structure morphism of [def-trf-integration]). Hence
$I$ may be verified after base change along etale morphisms, in particular
after base change to the strict henselization of $X$ at a point.

*Step 2 (graph replacement).* After such a base change and shrinking to
a neighbourhood of a fixed point, the correspondence is the graph of an
endomorphism: this is the reduction carried out in
[lem-trf-contracting-local-model], where the comparison of the two legs
modulo the square of the maximal ideal identifies the first leg as etale and
exhibits $c$ as the graph of $g=c_2c_1^{-1}$, the coefficient map becoming
an endomorphism of the stalk. It therefore suffices to prove
$I(\Gamma_g,v)$ for a graph correspondence $(X,\mathrm{id},g)$ with the
induced coefficient map $v$.

*Step 3 (deformation to the normal cone).* Deform the graph
$\Gamma_g\subset X\times_sX$ to the normal cone of the diagonal
$\Delta_X\subset X\times_sX$. The invariance of the section invariant under
this deformation is [thm-pur-dnc-invariance], applied in the situation of
the relative diagonal $p_1:X\times_sX\to X$ and its section $\Delta_X$;
there the normal bundle of the diagonal is the tangent bundle $T_X$ by
[thm-pur-diagonal-dualizing-object], so the deformation identifies the
section invariant of the graph with that of the zero section of $T_X$. The
corresponding statement for the trace class is the normal-cone evaluation
[lem-trf-contracting-normal-cone-evaluation]: the trace map restricted to
a fixed point is the pairing of the class of the stalk endomorphism with the
Thom class of the normal cone, normalized by the section invariant, and this
pairing is built from the dualizing data, which the deformation transports by
the functoriality of [thm-trf-dualizing-complex-composition]. Hence
$I(\Gamma_g,v)$ holds if and only if it holds for the special fibre of the
deformation.

*Step 4 (the special fibre is contracting).* The special fibre is the
normal cone carrying the linear correspondence induced by the differential
$dg$; at its zero section the two legs agree modulo the square of the
maximal ideal, so the correspondence is contracting in the sense of
[lem-trf-frobenius-formal-contraction]. There the trace class is
concentrated on the fixed points and its restriction to a fixed point is the
stalk evaluation, by [lem-trf-contracting-trace-stalk] together with the
locality of the trace class at a fixed point
[lem-trf-local-term-locality]; the global operator on the special fibre
is computed by the same stalk data, the fixed point being isolated and the
coefficient map an endomorphism of the stalk. Comparing the two descriptions
through the local terms of [def-trf-local-term] gives $I$ on the
special fibre.

*Conclusion.* By Step 3 the identity for the graph is equivalent to the
identity on the special fibre, which is Step 4, and by Step 2 the identity for
$c$ reduces, after the etale localizations of Step 1, to the identity for
the graph. Hence $I(\Delta_X,\mathrm{id})$ implies $I(c,u)$, as
asserted.
