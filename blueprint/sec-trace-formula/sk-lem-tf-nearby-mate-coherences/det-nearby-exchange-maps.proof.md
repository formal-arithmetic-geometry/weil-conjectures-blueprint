+++
kind = "proof"
of = "det-nearby-exchange-maps"
uses = ["det-sp-nearby-cycles-exchanges", "thm-weil-pbc-bounded-below"]
+++
Let $f=ph=p'h'$ be two compactifications. They have a common proper refinement: a proper $q$ from a
third compactification $f=p''h''$ to both, compatible with the open immersions. For such $q$, with
$h=qh''$ say, proper base change [thm-weil-pbc-bounded-below] identifies $Rq_*h''_!$ with $h_!$ on
both fibres, and $\chi_q$ is invertible by the proper exchange of [det-sp-nearby-cycles-exchanges].
Taking open adjoints, compatibility of $\nu_h$ and $\chi_q^{-1}Rq_{s*}(\nu_{h''})$ with this
identification reduces to the composition law for $\alpha$ (which holds by
[det-sp-nearby-cycles-exchanges]) and the ordinary adjunction triangle identity. Hence the two
definitions of $\nu_f$ agree with the one obtained from the refinement, and so with each other.
The same common-refinement argument, applied to a compactification of a composite $gf$ built from
compactifications of $f$ and $g$, proves that $\nu$ is compatible with composition.
