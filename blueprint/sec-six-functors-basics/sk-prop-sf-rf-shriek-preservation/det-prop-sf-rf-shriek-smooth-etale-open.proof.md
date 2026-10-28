+++
kind = "proof"
of = "det-prop-sf-rf-shriek-smooth-etale-open"
uses = ["lem-amb-etale-adjoint-locality", "prop-exc-finite-etale-adjoint", "thm-asd-smooth-tensor", "lem-sf-flat-model"]
+++
*(1).* For an open immersion, the étale localization of the exceptional adjoint
([lem-amb-etale-adjoint-locality], applied to $f=\mathrm{id}$) gives
$f^!\simeq f^*$; for a finite étale morphism this is
[prop-exc-finite-etale-adjoint]. Pullback is exact and carries a bounded flat
constructible model of $K$ in degrees $[a,b]$ ([lem-sf-flat-model]) to a model of
the same kind, so $f^*K$ is bounded constructible with Tor amplitude in $[a,b]$.

*(2).* By smooth duality ([thm-asd-smooth-tensor]),
$f^!K\simeq f^*K\otimes^{\mathbf L}_A\omega_f$ with $\omega_f[-2d]$ locally
constant, free of rank one. Locally on $X$ this is $f^*K[2d]$ up to a twist by a
locally free sheaf of rank one, which preserves bounded constructibility and shifts
the Tor interval of the flat model of $f^*K$ by $-2d$.
