+++
kind = "proof"
of = "proposition-etale-implications--2"
order = 29005
uses = ["definition-ind-etale-pro-etale-weakly"]
+++
The Lean source proves this criterion on affine charts. For a weakly
étale ring map $R\to B$, the multiplication map $B\otimes_RB\to B$
is flat and surjective. Its kernel $I$ is therefore pure, so $I=I^2$.
Consequently $\Omega_{B/R}=I/I^2=0$, and $R\to B$ is formally
unramified.

By [definition-ind-etale-pro-etale-weakly], the maps on affine charts
of $f$ are weakly étale. Applying the preceding argument on every
such chart shows that $f$ is formally unramified. It is flat by
assumption, and locally of finite presentation, hence étale. Taking
$f:\operatorname{Spec}(B)\to\operatorname{Spec}(R)$ gives the
ring-map assertion.
