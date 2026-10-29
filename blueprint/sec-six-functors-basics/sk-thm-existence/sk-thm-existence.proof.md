+++
kind  = "proof"
of    = "sk-thm-existence"
uses = ["sk-prop-sf-existence", "sk-prop-ctf-finite-compact", "sk-prop-ctf-finite-proper", "sk-thm-constructible-compactness", "sk-prop-proper-image-localizing", "sk-prop-int-compactness", "sk-prop-sf-rf-shriek-preservation", "sk-thm-restriction"]
+++
Parts (1) and (2) are the two finiteness facts that Brown representability needs to produce
$f^!$ in part (3); part (4) is geometric and uses the cohomology of the projective line. To
define $Rf_!$ one chooses, by Nagata's theorem, a compactification $f=pj$ and puts
$Rf_!=Rp_*j_!$; for (4) one factors $f$ locally as a closed immersion followed by the
projection of an affine space.

The functor $Rf_!\colon\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$ and its right adjoint
$f^!$ are constructed for all $\Lambda$ at once in [sk-prop-sf-existence]. Its hypotheses on
compactness and direct images are verified for finite $A$ in [sk-prop-ctf-finite-compact] and
[sk-prop-ctf-finite-proper], for fields in [sk-thm-constructible-compactness] and
[sk-prop-proper-image-localizing], and for $\cO_E$ in [sk-prop-int-compactness].

The fact that $f^!$ preserves $\Dctf(-,\Lambda)$ is [sk-prop-sf-rf-shriek-preservation] for
finite $A$ and [sk-thm-restriction] for $\cO_E$, $E$ and $\Qlb$ (recall that in the integral and
rational cases $\Dctf=\Dbc$).
