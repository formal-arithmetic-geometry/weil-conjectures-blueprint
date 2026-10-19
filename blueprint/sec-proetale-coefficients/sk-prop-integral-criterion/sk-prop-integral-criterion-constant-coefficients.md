+++
id = "det-prop-integral-criterion-constant-coefficients"
kind = "lemma"
title = "Constant versus completed integral coefficients"
uses = ["sk-def-sfb-pulled-back-coefficients", "det-prop-sfb-qlbar-colimit-x-integral-limit", "sk-def-pe-derived-completion"]
+++
Let $X$ be a scheme, $E/\mathbf Q_\ell$ finite, and let
$c\colon(\cO_E)_X\to\cO_{E,X}=\varprojlim_n(\cO_E/\pi_E^n)_X$ be the map from the constant
sheaf of rings to the pulled-back condensed ring $\cO_{E,X}=p_X^*\underline{\cO_E}$
([sk-def-sfb-pulled-back-coefficients]), identified with the limit of its finite levels by
[det-prop-sfb-qlbar-colimit-x-integral-limit].

1. $c$ is flat, and for every $n$ it induces an isomorphism
   $(\cO_E/\pi_E^n)_X=(\cO_E)_X/\pi_E^n\xrightarrow{\sim}\cO_{E,X}/\pi_E^n$.
2. Restriction of scalars along $c$ is an equivalence from the derived $\pi_E$-complete
   objects of $D(X_{\mathrm{proét}},\cO_{E,X})$ onto the derived $\pi_E$-complete objects of
   $D(X_{\mathrm{proét}},(\cO_E)_X)$, with inverse $L\mapsto$ derived completion of
   $\cO_{E,X}\otimes^{\mathbf L}_{(\cO_E)_X}L$.
3. It is compatible with reduction: for $K$ over $\cO_{E,X}$,
   $K\otimes^{\mathbf L}_{\cO_{E,X}}(\cO_E/\pi_E^n)_X$ and
   $K\otimes^{\mathbf L}_{(\cO_E)_X}(\cO_E/\pi_E^n)_X$ agree as complexes of
   $(\cO_E/\pi_E^n)_X$-modules.
