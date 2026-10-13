+++
kind  = "proof"
of    = "sk-rem-sf-matrix"
uses = ["sk-prop-sf-finiteness", "sk-thm-sf-ctf-stability", "sk-thm-sf-hom-ctf", "sk-prop-sf-rf-shriek-preservation", "sk-prop-sf-biduality-general"]
+++
Each cell is one of the results already proved, used on the domain stated
there. The $\Dbc$ cells for $Lf^*$, $Rf_*$ and $Rf_!$ are
[sk-prop-sf-finiteness]. The $\Dctf$ cells for $Lf^*$, $\otimes^L$, $Rf_*$
and $Rf_!$ are clauses of [sk-thm-sf-ctf-stability]. The $\RHom$ cell is
[sk-thm-sf-hom-ctf]: on the étale site for arbitrary objects, through the
dimension-dependent bound, and on the pro-étale site for pulled-back pairs.
The $Rf^!$ cell, for every separated finite-type $f$ with no admissibility
hypothesis, is [sk-prop-sf-rf-shriek-preservation]. The $\mathbb D_X$ cell
follows: $\omega_X=Ra_X^!\Lambda$ lies in $\Dctf$ by the $Rf^!$ cell, and
$\mathbb D_X=\RHom(-,\omega_X)$ preserves $\Dctf$ by the $\RHom$ cell. The
perfect case is the one used in [sk-prop-sf-biduality-general].
