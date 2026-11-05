+++
id = "lemma-proper-direct-image-unbounded-complexes"
kind = "lemma"
title = "Proper direct image of unbounded complexes"
order = 487
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.ProperLowerStarHeartHypotheses.preservesColimitsOfShape"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "definition-constructible-sheaves"]
+++
Let $p:X\to Y$ be proper, and let $d$ bound the dimensions of the geometric
fibres of $p$. For integers $a$ and $b$, write $\Dic^{\leq b}(X,\Lambda)$ and
$\Dic^{\geq a}(X,\Lambda)$ for the objects of $\Dic(X,\Lambda)$
(Corollary [corollary-ambient-ind-derived]) with cohomology in degrees
$\leq b$, respectively $\geq a$.

1. $Rp_*$ maps $\Dic(X,\Lambda)$ into $\Dic(Y,\Lambda)$, with
   $Rp_*\Dic^{\leq b}(X,\Lambda)\subset\Dic^{\leq b+2d+1}(Y,\Lambda)$ and
   $Rp_*\Dic^{\geq a}(X,\Lambda)\subset\Dic^{\geq a}(Y,\Lambda)$.
2. For $K\in\Dic(X,\Lambda)$ and every integer $q$, the truncation maps
   $K\leftarrow\tau_{\leq q}K\to\tau_{\geq q-2d-1}\tau_{\leq q}K$ induce an
   isomorphism in $\IndCons(Y,\Lambda)$
   $$
   \mathcal H^q(Rp_*K)\simeq
   \mathcal H^q\bigl(Rp_*\tau_{\geq q-2d-1}\tau_{\leq q}K\bigr).
   \tag{5.6}
   $$
3. $Rp_*:\Dic(X,\Lambda)\to\Dic(Y,\Lambda)$ preserves arbitrary direct sums.
