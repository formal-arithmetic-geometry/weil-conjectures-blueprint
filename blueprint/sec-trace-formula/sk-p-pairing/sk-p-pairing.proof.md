+++
kind  = "proof"
of    = "sk-p-pairing"
uses  = ["sk-d-corr", "sk-d-pairing", "sk-d-six", "sk-d-trace", "sk-d-trace-class", "sk-p-trace", "sk-thm-sf-kunneth-verdier", "sk-thm-sf-package"]
+++
Apply the construction to $P\boxtimes P^\vee$ on $s$: the diagonal is the
identity, its evaluation is the usual evaluation, and the symmetry is
precisely the symmetry in Definition [sk-d-trace].

*Complement.* The supported-class bijection of [sk-d-corr], followed by
[sk-thm-sf-kunneth-verdier], turns $u$ at a point into
$(u\otimes1)\mathrm{coev}_P:A\to P\otimes P^\vee$. For the diagonal identity,
the contraction in [sk-d-pairing] reduces by a triangle identity to symmetry
followed by evaluation. This is the composite of [sk-d-trace]; [sk-p-trace]
fixes its signs.

The same adjunction calculation identifies the trace class of
[sk-d-trace-class] on any $X$ with the displayed composite. Indeed, under
tensor–Hom adjunction and biduality from [sk-thm-sf-package], the class of the
diagonal identity maps to $1_K$. The supported cup product reduces by the
projection formula and $!$-base change in [sk-d-six] to the displayed
composite. This is the classical trace-class dictionary used by the proper
pushforward compatibility, on the specified fixed scheme.
