+++
kind  = "proof"
of    = "cor-zl-rfshriek-sheaf"
uses = ["lem-zl-composition-weight-bound"]
+++
Regard $\mathcal F$ as a complex concentrated in degree zero. The
definition [def-weil-complex-weights] identifies its upper bound
with membership in $D_{\le w}$. Noetherian induction and the localization rule
[lem-zl-open-closed-weight], in its morphism-level form
[lem-zl-morphism-open-closed-reduction] (source strata, target strata
and coefficient filtrations), reduce to the source and target strata
of [thm-zl-relative-noether]. The finite first arrow
$\nu$ preserves the upper weight bound by
[lem-zl-finite-pushforward] (on every refined quasi-finite piece, by
[lem-zl-quasi-finite]); every subsequent affine-line
projection preserves it by [thm-zl-relative-line-step]. Repeated
use of the composition isomorphism [lem-zl-shriek-composition],
in the form of the inheritance of the weight bound under composition
[lem-zl-composition-weight-bound] (stated for sheaves; for a sheaf in
degree zero the bound $R^if_!\mathcal F$ of weights at most $w+i$ is
the same as $Rf_!\mathcal F\in D_{\le w}$ by
[def-weil-complex-weights], so the complex-level steps supply its
hypotheses),
gives the bound for the whole factorization. The same localization
induction glues all strata, so $Rf_!\mathcal F\in D_{\le w}(Y_0)$;
reading the $i$th cohomology
sheaf gives the asserted bound $w+i$ (in the punctual sense of
[def-weil-punctual-weights]).
