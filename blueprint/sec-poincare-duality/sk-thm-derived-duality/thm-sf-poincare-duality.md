+++
id = "thm-sf-poincare-duality"
kind = "theorem"
title = "Poincare duality, framework form"
order = 2581
uses = ["cor-sf-trace", "cor-sf-trace-isomorphism", "cor-sf-trace-pairing", "cor-sf-trace-similitude", "def-sf-datum", "def-sf-orientation", "def-sf-pairing", "prop-sf-pf-coherence", "prop-sf-pf-reduction", "rem-sf-orientation-pointer", "thm-sf-identification", "thm-sf-pf-adic", "thm-sf-pf-field", "thm-sf-pf-finite", "thm-sf-pf-proetale"]
+++
In the setting of [def-sf-datum] and [def-sf-orientation], let
$X$ be smooth, proper and geometrically connected of pure dimension $d$,
and let $K\in D^b_{ctf}(X,\Lambda)$ be perfect over $\Lambda_X$. Then the
derived pairing $\beta_K$ of [def-sf-pairing] is perfect, the
isomorphism $R\Gamma_c(X,K)^\vee\cong R\Gamma(X,K^\vee(d))[2d]$ holds, and
for the constant sheaf the conclusions of [cor-sf-trace],
[cor-sf-trace-pairing], [cor-sf-trace-isomorphism] and
[cor-sf-trace-similitude] hold. (This
is the content of the duality chapter of the compiled blueprint, now
derived from [def-sf-datum] and [def-sf-orientation] alone; the
chapter's remaining nodes are the bookkeeping of the coefficient stages and
of the Weil structures.)

## Proof

Immediate from [def-sf-pairing], [thm-sf-identification] and
[cor-sf-trace], [cor-sf-trace-pairing], [cor-sf-trace-isomorphism], [cor-sf-trace-similitude]; the
only inputs are the axioms of [def-sf-datum], verified in [thm-sf-pf-finite], [prop-sf-pf-reduction], [thm-sf-pf-adic], [thm-sf-pf-field], [thm-sf-pf-proetale] and [prop-sf-pf-coherence] and in the base-change chapters, and the orientation, whose
construction is the content of the purity chapter (see
[rem-sf-orientation-pointer]).
