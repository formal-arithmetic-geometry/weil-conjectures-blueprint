+++
id = "lem-kun-tensor-t-est"
kind = "lemma"
title = "Left t-exactness of derived direct image"
lean = ["CategoryTheory.Functor.isZero_homologyFunctor_rightDerivedFunctorPlus_obj_of_isGE"]
order = 3113
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "thm-sp-truncation-e2"]
+++
Let $f:X\to Y$ be a morphism of schemes and $E\in\Dplus(X_{\Et})$.
If $\mathcal H^i(E)=0$ for $i<b$, then
$\mathcal H^i(Rf_*E)=0$ for $i<b$.
