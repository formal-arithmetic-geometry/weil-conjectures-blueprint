+++
kind  = "proof"
of    = "det-compact-trace-point-objects"
uses  = ["det-thm-sf-ctf-stability-direct-images"]
+++
By [det-thm-sf-ctf-stability-direct-images] (3), applied to $f=a_X$, the
functor $Ra_{X!}$ maps $\Dctf(X,A)$ into $\Dctf(s,A)$.

For the stalk, inverse image to the geometric point $\bar x$ is exact and
commutes with derived tensor products. The cohomology sheaves of $K$ are
constructible and vanish outside a bounded range of degrees, so the cohomology
modules of $K_{\bar x}$ are finitely generated and vanish outside the same
range. If $K$ has Tor amplitude in $[a,b]$, then for every $A$-module $M$
one has $K_{\bar x}\dt_AM\simeq(K\dt_AM_X)_{\bar x}$, which is concentrated in
degrees $[a,b]$; so $K_{\bar x}$ has Tor amplitude in $[a,b]$.
